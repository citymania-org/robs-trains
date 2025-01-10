import os
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw
import numpy as np
from psd_tools import PSDImage

from nml.grfstrings import NewGRFString, default_lang

import grf

CC_DEFAULT, CC_SWAPPED = 1, 2

CC_START = 0xC6
CC_COLOURS = (
    (8, 24, 88, 255),
    (12, 36, 104, 255),
    (20, 52, 124, 255),
    (28, 68, 140, 255),
    (40, 92, 164, 255),
    (56, 120, 188, 255),
    (72, 152, 216, 255),
    (100, 172, 224, 255)
)

CC2_START = 0x50
CC2_COLOURS = (
    (8, 52, 0, 255),
    (16, 64, 0, 255),
    (32, 80, 4, 255),
    (48, 96, 4, 255),
    (64, 112, 12, 255),
    (84, 132, 20, 255),
    (104, 148, 28, 255),
    (128, 168, 44, 255),
)


def make_remap_range(colours, remap):
    if len(colours) != 8:
        raise ValueError(f'CC replacement range should contain exactly 8 colours but {len(colours)} were found')
    if len(remap) != 8:
        raise ValueError(f'CC replacement range should contain exactly 8 colours but {len(remap)} were found')
    res = {}
    for (r, g, b, a), k in zip(colours, remap):
        # v = (a << 24) | (b << 16) | (g << 8) | r
        v = (r, g, b)
        res[v] = k
    return res

AUTO_REMAP = {}
AUTO_REMAP.update(make_remap_range(CC_COLOURS, range(CC_START, CC_START + 8)))
AUTO_REMAP.update(make_remap_range(CC2_COLOURS, range(CC2_START, CC2_START + 8)))

AUTO_REMAP_SWAPPED = {}
AUTO_REMAP_SWAPPED.update(make_remap_range(CC2_COLOURS, range(CC_START, CC_START + 8)))
AUTO_REMAP_SWAPPED.update(make_remap_range(CC_COLOURS, range(CC2_START, CC2_START + 8)))

THIS_FILE = grf.PythonFile(__file__)
IMAGE_FILES = {}


def _get_image_file(file):
    f = IMAGE_FILES.get(file)
    if f is None:
        f = IMAGE_FILES[file] = grf.ImageFile('sprites/' + file)
    return f


def read_palette_file(file):
    rgb = np.array(Image.open(file).convert('RGB'))
    h, w, _ = rgb.shape
    res = []
    for i in range(h * 8):
        res.append(tuple(map(int, rgb[i // 8, i % 8])))
    return res


class AutoMaskingFileSprite(grf.FileSprite):
    def __init__(self, file, cc_mode, *args, **kw):
        super().__init__(file, *args, **kw)
        self.cc_mode = cc_mode

    def get_data_layers(self, context):
        w, h, rgb, alpha, mask = super().get_data_layers(context)
        assert mask is None
        timer = context.start_timer()

        mask = np.zeros((h, w), dtype=np.uint8)
        remap = AUTO_REMAP_SWAPPED if self.cc_mode == CC_SWAPPED else AUTO_REMAP
        for k, v in remap.items():
            mask[np.all(np.equal(rgb, k), axis=2)] = v

        timer.count_custom('Generating auto CC masks')

        return w, h, rgb, alpha, mask

    def get_fingerprint(self):
        return dict(
            **super().get_fingerprint(),
            cc_mode=self.cc_mode,
        )


class CCReplacingFileSprite(grf.FileSprite):
    def __init__(self, file, cc_replace, cc2_replace, *args, **kw):
        super().__init__(file, *args, **kw)
        self._image = None
        remap = {}
        if cc_replace:
            remap.update(make_remap_range(CC_COLOURS, cc_replace))
        if cc2_replace:
            remap.update(make_remap_range(CC2_COLOURS, cc2_replace))
        self.remap = remap

    def get_data_layers(self, context):
        w, h, rgb, alpha, mask = super().get_data_layers(context)
        assert mask is None
        timer = context.start_timer()

        rgb = grf.np_make_writable(rgb)
        for k, v in self.remap.items():
            rgb[np.all(np.equal(rgb, k), axis=2)] = v

        timer.count_custom('Processing CC replacement')

        return w, h, rgb, alpha, mask

    def get_fingerprint(self):
        return dict(
            **super().get_fingerprint(),
            remap=tuple(self.remap.items()),
        )


class Livery:
    def __init__(self, template, image, *, mask=None, intro_year=None, auto_cc=None, cc_replace=None, cc2_replace=None):
        self.template = template
        self.image = image
        self.mask = mask
        self.intro_year = intro_year
        self.auto_cc = auto_cc
        self.cc_replace = cc_replace
        self.cc2_replace = cc2_replace
        has_cc_replace = (cc_replace is not None or cc2_replace is not None)
        if self.auto_cc is not None and has_cc_replace:
            raise ValueError('cc_replace/cc2_replace and auto_cc can''t be used together')
        if self.auto_cc and self.mask is not None:
            raise ValueError('mask and auto_cc can''t be used together')
        if has_cc_replace and self.mask is not None:
            raise ValueError('cc_replace/cc2_replace and mask can''t be used together')

    def _get_sprite_func(self):
        image_obj = _get_image_file(self.image)
        if self.auto_cc is not None:
            return lambda *args, **kw: AutoMaskingFileSprite(image_obj, self.auto_cc, *args, **kw)
        if self.cc_replace or self.cc2_replace:
            return lambda *args, **kw: CCReplacingFileSprite(image_obj, self.cc_replace, self.cc2_replace, *args, **kw)
        mask_obj = None
        if self.mask is not None:
            mask_obj = _get_image_file(self.mask)

        def f(x, y, w, h, *args, **kw):
            sprite = grf.FileSprite(
                image_obj,
                x, y, w, h,
                *args,
                **kw,
            )
            if mask_obj is None:
                return sprite
            return grf.WithMask(
                sprite,
                grf.FileSprite(
                    mask_obj,
                    x, y, w, h,
                ),
                mode=grf.MaskMode.OVERDRAW,
            )

        return f

    def get_sprites(self):
        return self.template(self._get_sprite_func())


class LiveryFactory:
    def __init__(self, template):
        self.template = template

    def __call__(self, image, *, mask=None, intro_year=None, auto_cc=None, cc_replace=None, cc2_replace=None):
        return Livery(self.template, image, mask=mask, intro_year=intro_year, auto_cc=auto_cc, cc_replace=cc_replace, cc2_replace=cc2_replace)


def _make_sprite_func(image_file, mask_file=None):
    mask = None
    if mask_file is not None:
        mask = grf.FileMask(
            _get_image_file(mask_file),
            mode=grf.Mask.Mode.OVERDRAW,
        )
    image = _get_image_file(image_file)
    return lambda *args, **kw: grf.FileSprite(image, *args, **kw, mask=mask)


def _make_liveries(liveries, is_articulated=False):
    # Currently unused vox stuff
    # sprites = lib.VoxTrainFile(filename).make_sprites()
    # if DEBUG_DIR is not None:
    #     debug_fname = os.path.join(DEBUG_DIR, os.path.basename(filename)[:-4]) + '.png'
    #     lib.make_debug_sprite_sheet(debug_fname, sprites, scale=5)

    res = []
    for name, l in liveries.items():
        data = {
            'name': f' ({name})',
            'sprites': l.get_sprites(),
        }
        if l.intro_year is not None:
            if is_articulated:
                raise ValueError('Articulated part livery can''t have intro_year')
            data['intro_year'] = l.intro_year
        res.append(data)

    return res


class Train(grf.Train):
    def __init__(self, *, liveries, country=None, company=None, power_type=None, purchase_sprite_towed_id=None, **kw):
        # Sort needed for intro year switch
        liveries = _make_liveries(liveries)
        # TODO make it a check instead of sorting, livery order is important for version compatibility
        liveries.sort(key=lambda l: l.get('intro_year', 0))

        super().__init__(
            liveries=liveries,
            default_cargo_type=grf.DEFAULT_CARGO_FIRST_REFITTABLE,
            **kw
        )
        self.country = country
        self.company = company
        self.power_type = power_type
        self.purchase_sprite_towed_id = purchase_sprite_towed_id

    def _gen_livery_callback(self, g, callbacks, liveries):
        if len(self.liveries) <= 1:
            return

        year_count = Counter(l.get('intro_ryear', 0) for l in liveries)

        cur_count = year_count.get(0, 0)
        code = []

        if len(self.liveries) == cur_count:
            code.append('cargo_subtype')
        else:
            code.append(f'TEMP[0] = {cur_count}')
            for year, count in year_count.items():
                if year == 0:
                    continue
                if count == 1:
                    code.append(f'TEMP[0] = (current_year >= {year}) + TEMP[0]')
                else:
                    code.append(f'TEMP[0] = (current_year >= {year}) * {count} + TEMP[0]')
            code.append('(cargo_subtype >= TEMP[0]) * -1000 + cargo_subtype')

        callbacks.cargo_subtype_text = grf.Switch(
            ranges={i: g.strings.add(l['name']).get_global_id() for i, l in enumerate(self.liveries)},
            default=0x400,
            code=code,
        )

    def add_articulated_part(self, liveries=None, **props):
        if liveries is not None:
            liveries = _make_liveries(liveries, True)
        if self._props.get('misc_flags') != None: # we don't want to add this is the main definition so that it is consistent for length > 8 and < 8
            props['misc_flags']=self._props.get('misc_flags')
        return super().add_articulated_part(
            liveries=liveries,
            default_cargo_type=grf.DEFAULT_CARGO_FIRST_REFITTABLE,
            **props
        )

    def _set_callbacks(self, g):
        res = super()._set_callbacks(g)
        self._gen_livery_callback(g, self.callbacks, self.liveries)
        return res


# TODO write it better
class PurchaseSprite(grf.SpriteWrapper):

    def __init__(self, xofs, yofs, parts, effects, train, towed, debug_dir):
        self.leading_sprite = train.liveries[0]['sprites'][6]   # get the - view for the default livery
        self.train = train
        self.towed = towed
        self.effects = effects
        self.debug_dir = debug_dir
        failed = False

        def property_image(name, sprites):
            value = getattr(self.train, name)
            if value is None:
                raise RuntimeError(f'No purchase sprite for {self.train.name}(#{self.train.id}): {name} is not specified')

            sprite = sprites.get(value)
            if sprite is None:
                raise RuntimeError(f'No purchase sprite for {self.train.name}(#{self.train.id}): no sprite for {name} "{value}"')

            return sprite
            # im = sprite.get_image()[0]
            # assert im.mode == 'RGBA'
            # return im

        self.parts = []
        sprites = [self.leading_sprite]
        for p in parts:
            dx, dy = p['offset']
            if p['property'] == 'self':
                sprite = self.leading_sprite
                is_train = True
            elif p['property'].startswith('towed'):
                s = p['property']
                if '[' in s:
                    index = int(s[s.find('[') + 1: s.find(']')])
                else:
                    index = 0
                if index >= len(self.towed):
                    continue
                sprite = self.towed[index]
                is_train = True
            else:
                sprite = property_image(p['property'], p['sprites'])
                is_train = False

            if sprite is None:
                failed = True
                break

            self.parts.append((is_train, sprite, dx, dy, p.get('effects')))
            sprites.append(sprite)

        super().__init__(sprites)
        self.w = self.h = None
        self.xofs = xofs
        self.yofs = yofs

    @staticmethod
    def _make_checker_effect(img, start, length):
        if start < 0:
            start = img.size[0] + start
        img = img.crop((0, 0, start + length, img.size[1]))
        npimg = np.array(img)
        for x in range(start, start + length):
            # add start to make sure it's consistent for any start
            npimg[(x + start) % 2::2, x] = (0, 0, 0, 0)
        return Image.fromarray(npimg)

    @staticmethod
    def _make_fade_effect(img, start, length):
        if start < 0:
            start = img.size[0] + start
        img = img.crop((0, 0, start + length, img.size[1]))
        npimg = np.array(img)
        step = 1.0 / (length + 1)
        for x in range(start, start + length):
            opacity = (length + start - x) * step
            npimg[:, x, 3] = npimg[:, x, 3] * opacity
        return Image.fromarray(npimg)

    @staticmethod
    def _make_opaque(img, opacity):
        npimg = np.asarray(img).copy()
        npimg[:, :, 3] = npimg[:, :, 3] * opacity
        return Image.fromarray(npimg)

    @staticmethod
    def apply_effects(img, effects):
        for e, args in (effects or {}).items():
            if e == 'checker':
                img = PurchaseSprite._make_checker_effect(img, *args)
            elif e == 'fade_out':
                img = PurchaseSprite._make_fade_effect(img, *args)
            elif e == 'opacity':
                img = PurchaseSprite._make_opaque(img, args)
            elif e == 'crop_x':
                max_width = args
                img = img.crop((0, 0, max_width, img.size[1]))
            else:
                raise ValueError(f'Unknown effect "{e}"')
        return img

    @staticmethod
    def train_image(sprite):
        img = sprite.make_rgba_image()
        assert img.mode == 'RGBA'
        w, h = img.size
        npimg = np.asarray(img)
        x_has_data = [np.any(npimg[:, x, 3]) for x in range(w)]
        x_first_data = min(i for i, x in enumerate(x_has_data) if x)
        x_last_data = max(i for i, x in enumerate(x_has_data) if x)
        y_has_data = [np.any(npimg[y, :, 3]) for y in range(h)]
        # y_first_data = min(i for i, x in enumerate(y_has_data) if x)
        y_last_data = max(i for i, x in enumerate(y_has_data) if x)
        return img.crop((x_first_data, 0, x_last_data + 1, y_last_data + 1))

    def get_image(self):
        w, h = 0, 0
        part_imgs = []

        for is_train, sprite, dx, dy, effects in self.parts:
            if is_train:
                img = PurchaseSprite.train_image(sprite)
                dy += sprite.yofs
            else:
                img = sprite.get_image()[0]
            w += dx
            part_imgs.append((img, (w, dy)))
            w += img.size[0]
            h = max(h, img.size[1] + dy)

        # FIXME
        # if failed:
        #     print(self.leading_sprite)
        #     return self.leading_sprite.get_image()

        im = Image.new('RGBA', (w, h))
        for img, dst in part_imgs:
            im.paste(img, dst)

        im = PurchaseSprite.apply_effects(im, self.effects)

        max_width = 98 - self.xofs
        if im.size[0] > max_width:
            print(f'Warning: purchase sprite for {self.train.name}(#{self.train.id}) is too wide: {im.size[0]}px (max {max_width})')

        if self.debug_dir:
            fname = os.path.join(debug_dir, f'purchase_{self.train.id}.png')
            im.save(fname, 'PNG')

        self.w, self.h = im.size
        return im, grf.BPP_32


def make_purchase_sprites(*, newgrf, xofs, yofs, parts, effects=None, debug_dir=None):
    if debug_dir:
        os.makedirs(debug_dir, exist_ok=True)

    train_idx = {}
    for t in newgrf.generators:
        if isinstance(t, Train):
            # print(t.id, t.liveries[0]['sprites'][6].file.path)
            train_idx[t.id] = t.liveries[0]['sprites'][6]
            for apid, _, liveries, _, _ in t._articulated_parts or []:
                train_idx[apid] = liveries[0]['sprites'][6]

    for t in newgrf.generators:
        if not isinstance(t, Train):
            continue

        towed_list = t.purchase_sprite_towed_id
        if towed_list is None:
            towed_list = []
        elif not isinstance(towed_list, (list, tuple)):
            towed_list = [towed_list]

        towed_sprites = []
        for towed_id in towed_list:
            towed = train_idx.get(towed_id)
            if towed is None:
                print(f'No purchase sprite for {t.name}(#{t.id}): Towed vehicle with id={towed_id} does not exist')
                failed = True
                break
            if not isinstance(towed, (grf.FileSprite, grf.ImageSprite)):
                print(f'No purchase sprite for {t.name}(#{t.id}): Towed vehicle with id={towed_id} has no usable graphics')
                failed = True
                break
            towed_sprites.append(towed)

        try:
            t.purchase_sprite = PurchaseSprite(xofs, yofs, parts, effects, t, towed_sprites, debug_dir)
        except RuntimeError as e:
            print(str(e))


def make_debug_sprite_sheet(filename, sprites, scale=1):
    rx, ry = 0, 0

    for s in sprites:
        rx += s.w
        ry = max(ry, s.h)

    im = Image.new('RGBA', (rx + 10 * len(sprites) - 10, ry))
    x = 0
    for s in sprites:
        im.paste(s.get_image()[0], (x, 0))
        x += s.w + 10
    if scale != 1:
        im = im.resize((im.size[0] * scale, im.size[1] * scale), Image.NEAREST)
    im.save(filename)


VOX_SIDE_ZL, VOX_SIDE_ZR, VOX_SIDE_X, VOX_SIDE_Y = 0, 0x100, 0x200, 0x300
VOX_SIDE_Z, VOX_SIDE_XY = 0, 0x100


class VoxTrainFile:

    class PreciseView:
        def __init__(self, x_axis, y_axis, z_axis):
            self.x_axis = x_axis
            self.y_axis = y_axis
            self.z_axis = z_axis
            self.data = None

        def load(self, reader, palette):
            S = 4
            S2 = S * 2
            S4 = S * 4
            XY = 15 #7
            stretched_x = self.x_axis.copy()
            stretched_x[1] *= 1.5
            xx = reader.voxels @ stretched_x
            yy = reader.voxels @ self.y_axis
            zz = reader.voxels @ self.z_axis
            cc = reader.voxels[:, 3]

            xmin, xmax = np.amin(xx), np.amax(xx)
            ymin, ymax = np.amin(yy), np.amax(yy)
            self.w = int(xmax - xmin + 2 + .5) * S2
            self.h = int(ymax - ymin + 2 + .5) * S2
            im = Image.new('RGBA', (self.w, self.h), color=(0, 0, 0, 0))
            draw = ImageDraw.Draw(im)

            def cube(x, y, cx, cy, cz):
                x2 = x + S2
                x4 = x + S4
                y1 = y + S
                y2 = y + S2
                draw.polygon(((x, y1 - 1), (x2 - 2, y), (x2 + 1, y), (x4 - 1, y1 - 1), (x2 + 1, y2 - 2), (x2 - 2, y2 - 2)), fill=cz)
                draw.polygon(((x, y1), (x + 1, y1), (x2 - 1, y2 - 1), (x2 - 1, y2 - 1 + XY), (x2 - 2, y2 - 1 + XY), (x, y1 + XY)), fill=cx)
                draw.polygon(((x4 - 1, y1), (x4 - 2, y1), (x2, y2 - 1), (x2, y2 - 1 + XY), (x2 + 1, y2 - 1 + XY), (x4 - 1, y1 + XY)), fill=cy)


            for i in np.argsort(zz):
                x = int((xx[i] - xmin) * S2 + .5)
                y = int((yy[i] - ymin) * S2 + .5)
                c = cc[i]
                cube(
                    x, y,
                    tuple(palette[c | VOX_SIDE_X]),
                    tuple(palette[c | VOX_SIDE_Y]),
                    tuple(palette[c | VOX_SIDE_Z]),
                )

            origin = int(.5 - xmin) // 8, int(.5 - ymin) // 8
            # im.show()
            return im.resize((self.w // S2 // 8, self.h // S2 // 8), Image.BOX), origin


    class DiagView:
        def __init__(self, x_axis, y_axis, z_axis):
            self.x_axis = x_axis
            self.y_axis = y_axis
            self.z_axis = z_axis
            self.data = None
            self.x_view = (self.y_axis[0] == 0)

        def load(self, reader, palette):
            xx = reader.voxels @ self.x_axis
            yy = reader.voxels @ self.y_axis
            zz = reader.voxels @ self.z_axis
            cc = reader.voxels[:, 3]

            xmin, xmax = np.amin(xx), np.amax(xx)
            ymin, ymax = np.amin(yy), np.amax(yy)
            # print(reader.size)
            # reader.size[2]
            self.w = xmax - xmin + 1
            h0 = self.h = ymax - ymin + 3
            self.w = (self.w + 3) // 4 * 4
            self.h = (self.h + 7) // 4 * 4 + 3
            #ymin += self.h - h0 # - 3 * (not self.x_view)
            ymin -= 2 * (not self.x_view)

            zbuf = np.full((self.h, self.w), -1e100)
            data = np.zeros((self.h, self.w), dtype=np.uint16)

            def set_pixel(x, y, z, c):
                if zbuf[y, x] >= z:
                    return
                zbuf[y, x] = z
                data[y, x] = c

            for x, y, z, c in zip(xx, yy, zz, cc):
                x -= xmin
                y = int(y - ymin + .5)
                set_pixel(x, y, z, c | VOX_SIDE_Z)
                set_pixel(x, y + 1, z, c | VOX_SIDE_XY)
                set_pixel(x, y + 2, z, c | VOX_SIDE_XY)

            data = palette[data]
            im = Image.fromarray(data, mode='RGBA')
            im = im.resize((im.size[0] // 4, im.size[1] // 8), Image.BOX)
            origin = -xmin // 4, int(.5 - ymin) // 8
            return im, origin

    def __init__(self, path, *,
                 xy_colour_func=lambda c: c.darken(20),
                 x_colour_func=lambda c: c.darken(40),
                 y_colour_func=None,
                 z_colour_func=lambda c: c.brighten(10)):
        if isinstance(path, grf.VoxReader):
            self.reader = path
            self.path = None
        else:
            self.path = path
            self.reader = grf.VoxReader(path)

        self.xy_colour_func = xy_colour_func
        self.x_colour_func = x_colour_func
        self.y_colour_func = y_colour_func
        self.z_colour_func = z_colour_func

        self.data = None

    def get_image(self):
        pass

    def _make_palette(self, reader):
        def make_remap(func):
            if func is None:
                return reader.vox_palette
            l = map(func, reader.palette)
            palette = np.array(tuple(x.rgb for x in l))
            palette[palette > 1.] = 1.
            palette = np.rint(palette * 255).astype(np.uint8)
            transparency = reader.vox_palette[:,3]
            transparency.shape = (len(transparency), 1)
            palette = np.concatenate((palette, transparency), axis=1)
            return palette

        REMAP_XY = make_remap(self.xy_colour_func)
        REMAP_X = make_remap(self.x_colour_func)
        REMAP_Y = make_remap(self.y_colour_func)
        REMAP_Z = make_remap(self.z_colour_func)
        palette = np.concatenate((REMAP_Z, REMAP_XY, REMAP_X, REMAP_Y))
        palette[0] = (0, 0, 0, 0)

        return palette.astype(np.uint8)

    def _debug_sprites(self, sprites):
        rx, ry = 0, 0

        for s in sprites:
            rx += s.w
            ry = max(ry, s.h)
        im = Image.new('RGBA', (rx + 10 * len(sprites) - 10, ry))
        x = 0
        for s in sprites:
            im.paste(s.get_image()[0], (x, 0))
            x += s.w + 10
        im = im.resize((im.size[0] * 10, im.size[1] * 10), Image.NEAREST)
        im.show()

    def make_sprites(self):
        self.reader.read()
        palette = self._make_palette(self.reader)

        ROTATE = np.array((
            ( 0, 1, 0, 0),
            (-1, 0, 0, 0),
            ( 0, 0, 1, 0),
            ( 0, 0, 0, 1)
        ), dtype=int)
        x = np.array((1, -1, 0, 0), dtype=float)
        y = np.array((.5, .5, -2, 0), dtype=float)
        z = np.array((1., 1, 2 / 3**.5, 0))

        sprites = []

        def add_sprite(v):
            sprites.append(v.load(self.reader, palette))

        for i in range(4):
            add_sprite(self.PreciseView(x, y, z))
            x = x @ ROTATE
            y = y @ ROTATE
            z = z @ ROTATE

        add_sprite(self.DiagView(
            np.array((1, 0, 0, 0), dtype=int),
            np.array((0, 1, -2, 0), dtype=int),
            np.array((2, 0, 1, 0), dtype=int),
        ))
        add_sprite(self.DiagView(
            np.array((-1, 0, 0, 0), dtype=int),
            np.array((0, 1, -2, 0), dtype=int),
            np.array((-2, 0, 1, 0), dtype=int),
        ))
        add_sprite(self.DiagView(
            np.array((0, -1, 0, 0), dtype=int),
            np.array((1, 0, -2, 0), dtype=int),
            np.array((1, 0, 1, 0), dtype=int),
        ))
        add_sprite(self.DiagView(
            np.array((0, 1, 0, 0), dtype=int),
            np.array((1, 0, -2, 0), dtype=int),
            np.array((1, 0, 1, 0), dtype=int),
        ))

        def make_sprite(i, xofs, yofs):
            im, (ox, oy) = sprites[i]
            # return ImageSprite(im, xofs=ox + xofs, yofs=oy + yofs
            # TODO offset to model center instead of origin
            return grf.ImageSprite(im, xofs=xofs - ox, yofs=yofs - oy)

        # sprites = [sprites[x] for x in (7, 1, 4, 0, 6, 3, 5, 2)]
        res = (
            # 4 / 8 (+ox)
            # make_sprite(7, 1, -14),  # |
            # make_sprite(1, 4, -24),  # /
            # make_sprite(4, 11, 16),  # -
            # make_sprite(0, -1, -10),  # \
            # make_sprite(6, -21, -6),  # |
            # make_sprite(3, -34, -16),  # /
            # make_sprite(5, -41, -16),  # -
            # make_sprite(2, -17, -29),  # \
            make_sprite(7, -25, -9),  # |
            make_sprite(1, -31, 4),  # /
            make_sprite(4, -21, -9),  # -
            make_sprite(0, 11, -6),  # \
            make_sprite(6, 26, -7),  # |
            make_sprite(3, 26, 6),  # /
            make_sprite(5, 20, -9),  # -
            make_sprite(2, -6, 17),  # \
        )
        # self._debug_sprites(res)
        return res


class PSDImageFile(grf.ImageFile):
    _INDEX = {}

    @classmethod
    def get(cls, path):
        spath = str(Path(path).resolve())
        f = cls._INDEX.get(spath)
        if f is None:
            f = cls(path)
            cls._INDEX[spath] = f
        return f

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._images = None
        self._kw_requested = set()

    @staticmethod
    def _make_kw_key(layers=None):
        if isinstance(layers, str):
            layers = (layers,)
        return tuple(layers or ())

    def prepare(self, **kw):
        self._kw_requested.add(self._make_kw_key(**kw))

    def _load_frame(self, fname):
        img = Image.open(fname)
        if img.mode == 'P':
            return (img, grf.BPP_8)
        elif img.mode == 'RGB':
            return (img, grf.BPP_24)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        return (img, grf.BPP_32)

    def load(self):
        if self._images is not None:
            return

        psd = PSDImage.open(self.path)
        self._images = {}
        layers = set(l.name for l in psd)

        for kw in self._kw_requested:
            for l in kw:
                if l not in layers:
                    raise ValueError(f'Unknown layer `{l}` requested.')

            def layer_filter(layer):
                return layer.name in kw
            self._images[kw] = psd.composite(layer_filter=layer_filter)

    def get_image(self, **kw):
        self.load()
        key = self._make_kw_key(**kw)
        return self._images[key], grf.BPP_32


class SpriteWrapper(grf.Sprite):
    def __init__(self, sprites, *, name=None):
        self.sprites = sprites
        try:
            f = next(iter(self._iter_sprites()))
        except StopIteration:
            raise ValueError('SpriteWrapper sprites to wrap')

        self.sprite = None
        if len(sprites) == 1:
            self.sprite = next(self._iter_sprites())

        super().__init__(w=f.w, h=f.h, xofs=f.xofs, yofs=f.yofs, zoom=f.zoom, bpp=f.bpp, crop=f.crop)

    def _iter_sprites(self):
        if isinstance(self.sprites, dict):
            i = self.sprites.values()
        else:
            i = self.sprites
        for s in i:
            if s is not None:
                yield s

    def get_image_files(self):
        return ()

    def get_resource_files(self):
        # TODO add wrapped class __file__, possibly traversing mro (do that globally?)
        res = super().get_resource_files() + (THIS_FILE,)
        for s in self._iter_sprites():
            res += s.get_resource_files()
        return res

    def get_fingerprint(self):
        res = {'class': self.__class__.__name__}
        if isinstance(self.sprites, dict):
            sf = {}
            for k, s in self.sprites.items():
                if s is None:
                    sf[k] = None
                else:
                    f = s.get_fingerprint()
                    if f is None:
                        return None
                    sf[k] = f
        else:
            sf = []
            for s in self.sprites:
                if s is None:
                    sf.append(None)
                    continue
                f = s.get_fingerprint()
                if f is None:
                    return None
                sf.append(f)
        res['sprites'] = sf
        return res

    def prepare_files(self):
        for s in self._iter_sprites():
            s.prepare_files()


class CompositeSprite(SpriteWrapper):
    def __init__(self, sprites, **kw):
        if len(sprites) == 0:
            raise ValueError('CompositeSprite requires a non-empty list of sprites to compose')
        if len(set(s.zoom for s in sprites)) > 1:
            sprite_list = ', '.join(f'{s.name}<zoom={s.zoom}>' for s in sprites)
            raise ValueError(f'CompositeSprite requires a list of sprites of same zoom level: {sprite_list}')
        super().__init__(sprites, **kw)

    def get_data_layers(self, context):
        npimg = None
        npalpha = None
        npmask = None
        nw, nh = self.w, self.h
        for s in self.sprites:
            w, h, ni, na, nm = s.get_data_layers(context)
            timer = context.start_timer()

            if nw is None:
                nw = w
            if nh is None:
                nh = h
            if nw != w or nh != h:
                raise RuntimeError(f'CompositeSprite layers have different size: {self.sprites[0].name}({nw}, {nh}) vs {s.name}({w}, {h})')

            if ni is not None:
                if npimg is None or na is None:
                    npimg = ni.copy()
                    if na is not None:
                        npalpha = na.copy()
                    else:
                        npalpha = None
                else:
                    full_mask = (na[:, :] == 255)
                    partial_mask = (na[:, :] > 0) & ~full_mask

                    npimg[full_mask] = ni[full_mask]
                    if npalpha is not None:
                        npalpha[full_mask] = 255

                    if npalpha is None:
                        npalpha_norm_mask = np.full(partial_mask.sum(), 1.0)
                    else:
                        npalpha_norm_mask = npalpha[partial_mask] / 255.0

                    na_norm_mask = na[partial_mask] / 255.0
                    resa = npalpha_norm_mask + na_norm_mask * (1 - npalpha_norm_mask)

                    npimg[partial_mask] = (
                        npimg[partial_mask] * npalpha_norm_mask[..., np.newaxis] +
                        ni[partial_mask] * (na_norm_mask * (1.0 - npalpha_norm_mask))[..., np.newaxis]
                    ) / resa[..., np.newaxis]
                    if npalpha is not None:
                        npalpha[partial_mask] = (resa * 255).astype(np.uint8)

            if nm is not None:
                if npmask is None:
                    npmask = nm.copy()
                else:
                    mask = (nm[:, :] != 0)
                    npmask[mask] = nm[mask]

            timer.count_custom('Layering')

        return w, h, npimg, npalpha, npmask



class AutoMask(SpriteWrapper):
    def __init__(self, sprite, cc_mode):
        self.sprite = sprite
        self.cc_mode = cc_mode
        super().__init__(dict(sprite=sprite))

    def get_data_layers(self, context):
        w, h, rgb, alpha, mask = self.sprite.get_data_layers(context)
        assert mask is None
        timer = context.start_timer()

        mask = np.zeros((h, w), dtype=np.uint8)
        remap = AUTO_REMAP_SWAPPED if self.cc_mode == CC_SWAPPED else AUTO_REMAP
        rgb = grf.np_make_writable(rgb)
        for k, v in remap.items():
            m = np.all(np.equal(rgb, k), axis=2)
            mask[m] = v
            rgb[m] = (grf.DEFAULT_BRIGHTNESS, 0, 0)

        timer.count_custom('Generating auto CC masks')

        return w, h, rgb, alpha, mask

    def get_fingerprint(self):
        return dict(
            **super().get_fingerprint(),
            cc_mode=self.cc_mode,
        )


class CCReplace(SpriteWrapper):
    def __init__(self, sprite, cc_replace, cc2_replace):
        remap = {}
        if cc_replace:
            remap.update(make_remap_range(CC_COLOURS, cc_replace))
        if cc2_replace:
            remap.update(make_remap_range(CC2_COLOURS, cc2_replace))
        self.remap = remap
        super().__init__(dict(sprite=sprite))

    def get_data_layers(self, context):
        w, h, rgb, alpha, mask = self.sprite.get_data_layers(context)
        assert mask is None
        timer = context.start_timer()

        rgb = grf.np_make_writable(rgb)
        for k, v in self.remap.items():
            rgb[np.all(np.equal(rgb, k), axis=2)] = v

        timer.count_custom('Processing CC replacement')

        return w, h, rgb, alpha, mask

    def get_fingerprint(self):
        return dict(
            **super().get_fingerprint(),
            remap=tuple(self.remap.items()),
        )


class PSDLivery:

    class Sprite(SpriteWrapper):
        def __init__(self, *, shading, paint, palette):
            self.palette = palette
            super().__init__(dict(shading=shading, paint=paint))

        def get_data_layers(self, context):
            shading, paint = self.sprites['shading'], self.sprites['paint']

            sw, sh, srgb, salpha, smask = shading.get_data_layers(context)
            pw, ph, prgb, palpha, pmask = paint.get_data_layers(context)

            assert smask is None and pmask is None
            assert palpha is not None

            assert sw == pw and ph == ph
            rgb = srgb.copy()
            # rgb = np.zeros((sh, sw, 3), dtype=np.uint8)
            left_mask = (palpha > 0)
            for k, l in self.palette.items():
                pmask = np.all(np.equal(prgb, k), axis=2) & left_mask
                if not np.any(pmask):
                    continue

                left_mask ^= pmask
                for i, cc in enumerate(CC_COLOURS):
                    smask = np.all(np.equal(srgb[pmask], cc[:3]), axis=1)
                    pcopy = pmask.copy()
                    pcopy[pcopy] = smask
                    rgb[pcopy] = l[i]

            unused_pixels = np.where(left_mask)
            if len(unused_pixels[0]) > 0:
                x, y = unused_pixels[0][0], unused_pixels[1][0]
                raise RuntimeError(f'No-main colour used in paint layer, first pixel at ({x}, {y}) in the croped square: {tuple(prgb[x, y])}')

            return sw, sh, rgb, salpha, None

        def get_fingerprint(self):
            return dict(
                **super().get_fingerprint(),
                palette=tuple(self.palette.items()),
            )


    def __init__(self, template, paint_palette, path, *, shading=None, paint=None, overlay=None, intro_year=None, auto_cc=None, cc_replace=None, cc2_replace=None):
        if shading is None and overlay is None:
            raise ValueError('Sprite must use shading or overlay')
        self.template = template

        if len(paint_palette) % 8 != 0:
            raise ValueError('Paint palette must have exactly 8 shades for each colour')
        self._paint_palette = {}

        for i, ccp in enumerate((CC_COLOURS, CC2_COLOURS)):
            pal = [c[:3] for c in ccp]
            if pal != paint_palette[i * 8: i * 8 + 8]:
                raise ValueError(f'Row {i} in the paint palette doesn''t match CC colours')
            for c in pal:
                self._paint_palette[c] = pal

        for i in range(16, len(paint_palette), 8):
            main_colour = paint_palette[i + 4]
            if main_colour in self._paint_palette:
                raise ValueError(f'Colour {main_colour} is used as the main colour more than once in the paint palette (row {i})')
            self._paint_palette[main_colour] = paint_palette[i: i + 8]

        self.file = PSDImageFile.get(path)

        mklist = lambda l: l if isinstance(l, (tuple, list)) else (None if l is None else (l,))
        self.shading = mklist(shading)
        self.paint = mklist(paint)
        self.overlay = mklist(overlay)

        self.intro_year = intro_year
        self.auto_cc = auto_cc
        self.cc_replace = cc_replace
        self.cc2_replace = cc2_replace
        self._has_cc_replace = (cc_replace is not None or cc2_replace is not None)
        if self.auto_cc is not None and self._has_cc_replace:
            raise ValueError('cc_replace/cc2_replace and auto_cc can''t be used together')

    def _get_sprite_func(self):
        def f(x, y, w, h, *args, **kw):
            def mksprite(layers):
                if layers is None:
                    return None
                return grf.FileSprite(
                    self.file,
                    x, y, w, h,
                    *args,
                    **kw,
                    layers=layers,
                )

            if self.shading is None:
                return mksprite(self.overlay)

            sprite = mksprite(self.shading)

            if self.paint is not None:
                sprite = self.Sprite(
                    shading=sprite,
                    paint=mksprite(self.paint),
                    palette=self._paint_palette,
                )

            if self.overlay is not None:
                sprite = CompositeSprite((sprite, mksprite(self.overlay)))

            if self.auto_cc is not None:
                return AutoMask(sprite, self.auto_cc)

            if self._has_cc_replace:
                return CCReplace(sprite, self.cc_replace, self.cc2_replace)

            return sprite

        return f

    def get_sprites(self):
        return self.template(self._get_sprite_func())
    
class SetPurchaseOrder(grf.SetPurchaseOrder): # we want to have the name of top level contain the lowest level one this is not suported by grf-py nativly.

    def set_variant_callbacks(self, g):
        for _, (x, names) in self._variant_callbacks.items():
            c = x.callbacks.name = grf.Switch(
                code='extra_callback_info1',
                ranges = {
                    0x20 | (level << 8): g.strings.add(name + " - {SILVER}" + x.name).get_global_id()
                    for level, name in names.items()
                },
                default=0x400,
            )
        self._variant_callbacks_set = True
        return self
