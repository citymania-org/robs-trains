import os
from collections import Counter

from PIL import Image, ImageDraw
import numpy as np

from nml.grfstrings import NewGRFString, default_lang

import grf


class VehicleSpriteTable(grf.VehicleSpriteTable):
    def add_layout(self, sprites):
        if not sprites:
            return self.add_empty_layout()
        return self.get_layout(self.add_row(sprites))

    def add_empty_layout(self):
        return self.add_layout([
            grf.EMPTY_SPRITE,
            grf.EMPTY_SPRITE,
            grf.EMPTY_SPRITE,
            grf.EMPTY_SPRITE,
            grf.EMPTY_SPRITE,
            grf.EMPTY_SPRITE,
            grf.EMPTY_SPRITE,
            grf.EMPTY_SPRITE,
        ])


class Train(grf.Train):
    def __init__(self, country=None, company=None, power_type=None, purchase_sprite_towed_id=None, **kw):
        self._articulated_length = 0
        if 'length' in kw:
            self.length = kw.pop('length')
            if self.length > 8:
                if self.length > 24:
                    raise ValueError("Max Train length is 24")
                self._head_liveries = []
                if self.length % 2 == 1:
                    self._central_length = 7
                    self._articulated_length = (self.length - 7) // 2
                else:
                    self._central_length = 8
                    self._articulated_length = (self.length - 8) // 2
                kw['shorten_by'] = 8 - self._articulated_length
            else:
                self._central_length = self.length
                kw['shorten_by'] = 8 - self.length

        super().__init__(
            # default_cargo_type=grf.DEFAULT_CARGO_FIRST_REFITTABLE,
            **kw
        )
        self.country = country
        self.company = company
        self.power_type = power_type
        self.purchase_sprite_towed_id = purchase_sprite_towed_id
        self.purchase_sprite = None
        self.liveries.sort(key=lambda l: l.get('intro_year', 0))
        if self._articulated_length > 0:
            self.add_articulated_part(
                id=kw['id'] + 1,
                liveries=self.liveries,
                shorten_by=8 - self._central_length
            )
            self._head_liveries = [{'name': l['name']} for l in self.liveries]
            self.add_articulated_part(
                id=kw['id'] + 2,
                liveries=self._head_liveries,
                shorten_by=8 - self._articulated_length
            )
        else:
            self._head_liveries = self.liveries


    def _gen_livery_sprites(self, liveries):
        sprites = VehicleSpriteTable(grf.TRAIN)

        layouts = [sprites.add_layout(l.get('sprites')) for l in (liveries or {})]

        if len(layouts) == 0:
            layout = sprites.add_empty_layout()
        elif len(layouts) == 1:
            layout = layouts[0]
        else:
            layout = grf.Switch(
                related_scope=True,
                ranges=dict(enumerate(layouts)),
                default=layouts[0],
                code='cargo_subtype',
            )

        return sprites, layout

    def _gen_livery_callback(self, g, callbacks, liveries):
        # TODO check for single livery

        year_count = Counter(l.get('intro_year', 0) for l in liveries)

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

        callbacks.cargo_subtype = grf.Switch(
            ranges={i: g.strings.add(l['name']).get_global_id() for i, l in enumerate(self.liveries)},
            default=0x400,
            code=code,
        )


    def get_sprites(self, g):
        # Check in case property was changed after add_articulated
        if self._props.get('is_dual_headed') and self._articulated_parts:
            raise RuntimeError('Articulated parts are not allowed for dual-headed engines (vehicle id {self.id})')

        res = []

        # Sort needed for intro year switch
        self.liveries.sort(key=lambda l: l.get('intro_year', 0))

        if self.purchase_sprite:
            # Make sure purchase layouts go before main action 1
            res.append(grf.SpriteSet(feature=grf.TRAIN, count=1))
            res.append(self.purchase_sprite)
            res.append(layout := grf.GenericSpriteLayout(ent1=(0,), ent2=(0,)))
            self.callbacks.purchase_graphics = layout

        veh_sprites, self.callbacks.graphics = self._gen_livery_sprites(self._head_liveries)

        if veh_sprites:
            res.append(veh_sprites)

        self._gen_livery_callback(g, self.callbacks, self.liveries)

        if self.additional_text:
            self.callbacks.purchase_text = g.strings.add(self.additional_text).get_global_id()

        if self.sound_effects:
            self.callbacks.sound_effect = grf.Switch(
                ranges=self.sound_effects,
                default=self.callbacks.graphics,
                code='extra_callback_info1_byte',
            )

        if self._articulated_parts:
            self.callbacks.articulated_part = grf.Switch(
                ranges={i + 1: ap[0] for i, ap in enumerate(self._articulated_parts)},
                default=0x7fff,
                code='extra_callback_info1_byte',
            )

        if self.callbacks.get_flags():
            self._props['cb_flags'] = self._props.get('cb_flags', 0) | self.callbacks.get_flags()

        res.append(
            grf.DefineStrings(
                feature=grf.TRAIN,
                offset=self.id,
                is_generic_offset=False,
                strings=[self.name.encode('utf-8')]
            ),
        )

        res.append(definition := grf.Define(
            feature=grf.TRAIN,
            id=self.id,
            props={
                'sprite_id': 0xfd,  # magic value for newgrf sprites
                'max_speed': self.max_speed,
                **self._props
            }
        ))

        res.append(self.callbacks.make_map_action(definition))

        for apid, liveries, initial_callbacks, props in self._articulated_parts:
            callbacks = grf.CallbackManager(grf.Callback.Vehicle, initial_callbacks)

            res.append(definition := grf.Define(
                feature=grf.TRAIN,
                id=apid,
                props={
                    'sprite_id': 0xfd,  # magic value for newgrf sprites
                    'engine_class': self._props.get('engine_class'),
                    'default_cargo_type': grf.DEFAULT_CARGO_FIRST_REFITTABLE,
                    **props
                }
            ))

            veh_sprites, callbacks.graphics = self._gen_livery_sprites(liveries)
            if veh_sprites:
                res.append(veh_sprites)

            res.append(callbacks.make_map_action(definition))

        return res


def _make_checker_effect(img, start, length):
    if start < 0:
        start = img.size[0] + start
    img = img.crop((0, 0, start + length, img.size[1]))
    npimg = np.asarray(img)
    for x in range(start, start + length):
        # add start to make sure it's consistent for any start
        npimg[(x + start) % 2::2, x] = (0, 0, 0, 0)
    return Image.fromarray(npimg)


def _make_fade_effect(img, start, length):
    if start < 0:
        start = img.size[0] + start
    img = img.crop((0, 0, start + length, img.size[1]))
    npimg = np.asarray(img)
    step = 1.0 / (length + 1)
    for x in range(start, start + length):
        opacity = (length + start - x) * step
        npimg[:, x, 3] = npimg[:, x, 3] * opacity
    return Image.fromarray(npimg)


def _make_opaque(img, opacity):
    npimg = np.asarray(img)
    npimg[:, :, 3] = npimg[:, :, 3] * opacity
    return Image.fromarray(npimg)


def apply_effects(img, effects):
    for e, args in (effects or {}).items():
        if e == 'checker':
            return _make_checker_effect(img, *args)
        elif e == 'fade_out':
            return _make_fade_effect(img, *args)
        elif e == 'opacity':
            return _make_opaque(img, args)
        else:
            raise ValueError(f'Unknown effect "{e}"')
    return img


def make_purchase_sprites(*, newgrf, xofs, yofs, parts, effects=None, debug_dir=None):
    if debug_dir:
        os.makedirs(debug_dir, exist_ok=True)

    train_idx = {}
    for t in newgrf.generators:
        if isinstance(t, Train):
            train_idx[t.id] = t.liveries[0]
            for apid, liveries, _, _ in t._articulated_parts or []:
                train_idx[apid] = liveries[0]

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
            y_last_data = max(i for i, x in enumerate(y_has_data) if x)
            return img.crop((x_first_data, 0, x_last_data + 1, y_last_data + 1))

        towed_list = t.purchase_sprite_towed_id
        if isinstance(towed_list, int):
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
                sprite = towed['sprites'][6]
                img = train_image(sprite)
                dy += sprite.yofs
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


set_global_train_y_offset = lambda ofs: grf.ComputeParameters(target=0x8e, operation=0x00, if_undefined=False, source1=0xff, source2=0xff, value=ofs)

set_global_train_misc_flag = lambda pos: grf.ComputeParameters(target=0x9e, operation=0x08, if_undefined=False, source1=0x9e, source2=0xff, value=1 << pos)
set_global_train_depot_width_32 = lambda: set_global_train_misc_flag(3)


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
