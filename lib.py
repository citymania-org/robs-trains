import os
from collections import Counter

from PIL import Image, ImageDraw
import numpy as np

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
        v = (a << 24) | (b << 16) | (g << 8) | r
        res[v] = k
    return res

AUTO_REMAP = {}
AUTO_REMAP.update(make_remap_range(CC_COLOURS, range(CC_START, CC_START + 8)))
AUTO_REMAP.update(make_remap_range(CC2_COLOURS, range(CC2_START, CC2_START + 8)))

AUTO_REMAP_SWAPPED = {}
AUTO_REMAP_SWAPPED.update(make_remap_range(CC2_COLOURS, range(CC_START, CC_START + 8)))
AUTO_REMAP_SWAPPED.update(make_remap_range(CC_COLOURS, range(CC2_START, CC2_START + 8)))

IMAGE_FILES = {}

def _get_image_file(file):
    f = IMAGE_FILES.get(file)
    if f is None:
        f = IMAGE_FILES[file] = grf.ImageFile('sprites/' + file)
    return f


def read_palette_file(file):
    npimg = np.array(Image.open(file).convert('RGBA'))
    h, w, _ = npimg.shape
    npview = npimg.view(dtype=np.uint32).reshape((h, w))
    res = []
    for i in range(h * 8):
        res.append(npview[i // 8, i % 8])
    return res


class AutoMaskingFileSprite(grf.FileSprite):

    class Mask(grf.Mask):
        def __init__(self, sprite):
            super().__init__(mode=grf.Mask.Mode.OVERDRAW)
            self.sprite = sprite
            self._image = None

        def get_image(self):
            if self._image is not None:
                return self._image

            image, bpp = self.sprite.get_image()
            if bpp != grf.BPP_32:
                raise RuntimeError('Only 32-bit RGBA sprites are currently supported with auto-masking')

            npimg = np.asarray(image)
            h, w, _ = npimg.shape
            npview = npimg.view(dtype=np.uint32).reshape(w * h)
            npmask = np.zeros(len(npview), dtype=np.uint8)
            remap = AUTO_REMAP_SWAPPED if self.sprite.cc_mode == CC_SWAPPED else AUTO_REMAP
            for k, v in remap.items():
                npmask[npview == k] = v

            img = Image.fromarray(npmask.reshape((h, w)))
            img.putpalette(grf.PALETTE)
            self._image = img, grf.BPP_8
            return self._image

        def get_resource_files(self):
            return ()

        def get_fingerprint(self):
            return {
                'class': self.__class__.__name__
            }

    def __init__(self, file, cc_mode, *args, **kw):
        super().__init__(file, *args, **kw, mask=self.Mask(self))
        self._image = None
        self.cc_mode = cc_mode

    def get_image(self):
        if self._image is None:
            self._image = super().get_image()
        return self._image

    def get_fingerprint(self):
        return grf.combine_fingerprint(
            super().get_fingerprint(),
            cm_mode=self.cc_mode,
        )


class CCReplacingFileSprite(grf.FileSprite):
    def __init__(self, file, cc_replace, cc2_replace, *args, **kw):
        super().__init__(file, *args, **kw, mask=None)
        self._image = None
        remap = {}
        if cc_replace:
            remap.update(make_remap_range(CC_COLOURS, cc_replace))
        if cc2_replace:
            remap.update(make_remap_range(CC2_COLOURS, cc2_replace))

        if remap and isinstance(next(iter(remap.values())), tuple):
            remap = {
                k: (a << 24) | (b << 16) | (g << 8) | r
                for k, (r, g, b, a) in remap.items()
            }
        else:
            remap = {
                k: int(v)
                for k, v in remap.items()
            }

        self.remap = remap

    def get_image(self):
        if self._image is not None:
            return self._image
        image, bpp = super().get_image()

        if bpp != grf.BPP_32:
            raise RuntimeError('Only 32-bit RGBA sprites are currently supported for CC replacement')

        npimg = np.asarray(image).copy()
        h, w, _ = npimg.shape
        npview = npimg.view(dtype=np.uint32).reshape(w * h)
        for k, v in self.remap.items():
            npview[npview == k] = v

        img = Image.fromarray(npimg, 'RGBA')
        self._image = img, grf.BPP_32
        return self._image

    def get_fingerprint(self):
        return grf.combine_fingerprint(
            super().get_fingerprint(),
            remap=self.remap,
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
            mask = None
            if mask_obj is not None:
                mask = grf.FileMask(
                    mask_obj,
                    x, y, w, h,
                    mode=grf.Mask.Mode.OVERDRAW,
                )
            return grf.FileSprite(
                image_obj,
                x, y, w, h,
                *args,
                **kw,
                mask=mask,
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
        return super().add_articulated_part(
            liveries=liveries,
            default_cargo_type=grf.DEFAULT_CARGO_FIRST_REFITTABLE,
            **props
        )

    def _set_callbacks(self, g):
        res = super()._set_callbacks(g)
        self._gen_livery_callback(g, self.callbacks, self.liveries)
        return res


def _make_checker_effect(img, start, length):
    if start < 0:
        start = img.size[0] + start
    img = img.crop((0, 0, start + length, img.size[1]))
    npimg = np.array(img)
    for x in range(start, start + length):
        # add start to make sure it's consistent for any start
        npimg[(x + start) % 2::2, x] = (0, 0, 0, 0)
    return Image.fromarray(npimg)


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


def _make_opaque(img, opacity):
    npimg = np.asarray(img).copy()
    npimg[:, :, 3] = npimg[:, :, 3] * opacity
    return Image.fromarray(npimg)


def apply_effects(img, effects):
    for e, args in (effects or {}).items():
        if e == 'checker':
            img = _make_checker_effect(img, *args)
        elif e == 'fade_out':
            img = _make_fade_effect(img, *args)
        elif e == 'opacity':
            img = _make_opaque(img, args)
        elif e == 'crop_x':
            max_width = args
            img = img.crop((0, 0, max_width, img.size[1]))
        else:
            raise ValueError(f'Unknown effect "{e}"')
    return img


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

        def property_image(name, sprites):
            value = getattr(t, name)
            if value is None:
                print(f'No purchase sprite for {t.name}(#{t.id}): {name} is not specified')
                return None

            sprite = sprites.get(value)
            if sprite is None:
                print(f'No purchase sprite for {t.name}(#{t.id}): no sprite for {name} "{value}"')
                return None

            im = sprite.get_image()[0]
            assert im.mode == 'RGBA'
            return im
            # im.paste(image, pos)
            # return True

        def train_image(sprite):
            img = sprite.get_image()[0]
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

        towed_list = t.purchase_sprite_towed_id
        if towed_list is None:
            towed_list = []
        elif not isinstance(towed_list, (list, tuple)):
            towed_list = [towed_list]

        part_imgs = []
        w, h = 0, 0
        failed = False
        res_yofs = None
        for p in parts:
            dx, dy = p['offset']
            if p['property'] == 'self':
                sprite = t.liveries[0]['sprites'][6]
                img = train_image(sprite)
                dy += sprite.yofs
            elif p['property'].startswith('towed'):
                s = p['property']
                if '[' in s:
                    index = int(s[s.find('[') + 1: s.find(']')])
                else:
                    index = 0
                if index >= len(towed_list):
                    continue
                towed_id = towed_list[index]
                towed = train_idx.get(towed_id)
                if towed is None:
                    print(f'No purchase sprite for {t.name}(#{t.id}): Towed vehicle with id={towed_id} does not exist')
                    failed = True
                    break
                if not isinstance(towed, (grf.FileSprite, grf.ImageSprite)):
                    print(f'No purchase sprite for {t.name}(#{t.id}): Towed vehicle with id={towed_id} has no usable graphics')
                    failed = True
                    break
                img = train_image(towed)
                dy += towed.yofs
            else:
                img = property_image(p['property'], p['sprites'])
                if img is None:
                    failed = True
                    break

            img = apply_effects(img, p.get('effects'))

            w += dx
            part_imgs.append((img, (w, dy)))
            w += img.size[0]
            h = max(h, img.size[1] + dy)

        if failed:
            continue

        im = Image.new('RGBA', (w, h))
        for img, dst in part_imgs:
            im.paste(img, dst)

        im = apply_effects(im, effects)

        t.purchase_sprite = grf.ImageSprite(im, xofs=xofs, yofs=yofs)

        max_width = 98 - t.purchase_sprite.xofs
        if im.size[0] > max_width:
            print(f'Warning: purchase sprite for {t.name}(#{t.id}) is too wide: {im.size[0]}px (max {max_width})')

        if debug_dir:
            fname = os.path.join(debug_dir, f'purchase_{t.id}.png')
            im.save(fname, 'PNG')


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
