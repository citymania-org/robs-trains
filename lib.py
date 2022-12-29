from collections import Counter

from nml.grfstrings import NewGRFString, default_lang

import grf


class VehicleSpriteTable(grf.VehicleSpriteTable):
    def add_layout(self, sprites):
        if not sprites:
            return self.add_empty_layout()
        return self.get_layout(self.add_row(sprites))

    def add_empty_layout(self):
        return self.add_layout([
            grf.EmptyGraphicsSprite(),
            grf.EmptyGraphicsSprite(),
            grf.EmptyGraphicsSprite(),
            grf.EmptyGraphicsSprite(),
            grf.EmptyGraphicsSprite(),
            grf.EmptyGraphicsSprite(),
            grf.EmptyGraphicsSprite(),
            grf.EmptyGraphicsSprite()
        ])


class Train(grf.Train):

    def __init__(self, **kw):
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

        super().__init__(**kw)

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

        layouts = [sprites.add_layout(l.get('sprites')) for l in self.liveries]

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

    def _gen_liveries(self, g, callbacks, liveries):
        # TODO check for single livery

        liveries.sort(key=lambda l: l.get('intro_year', 0))
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

        return self._gen_livery_sprites(liveries)


    def get_sprites(self, g):
        # Check in case property was changed after add_articulated
        if self._props.get('is_dual_headed') and self._articulated_parts:
            raise RuntimeError('Articulated parts are not allowed for dual-headed engines (vehicle id {self.id})')

        # Sort needed for intro year switch
        self.liveries.sort(key=lambda l: l.get('intro_year', 0))

        veh_sprites, self.callbacks.graphics = self._gen_liveries(g, self.callbacks, self.liveries)

        if self.additional_text:
            self.callbacks.purchase_text = g.strings.add(self.additional_text).get_global_id()

        if self.sound_effects:
            self.callbacks.sound_effect = grf.Switch(
                ranges=self.sound_effects,
                default=self.callbacks.graphics,
                code='extra_callback_info1 & 255',
            )

        if self._articulated_parts:
            self.callbacks.articulated_part = grf.Switch(
                ranges={i + 1: ap[0] for i, ap in enumerate(self._articulated_parts)},
                default=0x7fff,
                code='extra_callback_info1 & 255',
            )

        if self.callbacks.get_flags():
            self._props['cb_flags'] = self._props.get('cb_flags', 0) | self.callbacks.get_flags()

        res = [
            grf.DefineStrings(
                feature=grf.TRAIN,
                offset=self.id,
                is_generic_offset=False,
                strings=[self.name.encode('utf-8')]
            ),
        ]

        res.append(definition := grf.Define(
            feature=grf.TRAIN,
            id=self.id,
            props={
                'sprite_id': 0xfd,  # magic value for newgrf sprites
                'max_speed': self.max_speed,
                **self._props
            }
        ))

        if veh_sprites:
            res.append(veh_sprites)

        res.append(self.callbacks.make_map_action(definition))

        for apid, liveries, initial_callbacks, props in self._articulated_parts:
            callbacks = grf.CallbackManager(grf.Callback.Vehicle, initial_callbacks)

            res.append(definion := grf.Define(
                feature=grf.TRAIN,
                id=apid,
                props={
                    'sprite_id': 0xfd,  # magic value for newgrf sprites
                    'engine_class': self._props.get('engine_class'),
                    **props
                }
            ))

            veh_sprites, callbacks.graphics = self._gen_livery_sprites(liveries)
            if veh_sprites:
                res.append(veh_sprites)

            res.append(callbacks.make_map_action(definition))
        return res


set_global_train_y_offset = lambda ofs: grf.ComputeParameters(target=0x8e, operation=0x00, if_undefined=False, source1=0xff, source2=0xff, value=ofs)

set_global_train_misc_flag = lambda pos: grf.ComputeParameters(target=0x9e, operation=0x08, if_undefined=False, source1=0x9e, source2=0xff, value=1 << pos)
set_global_train_depot_width_32 = lambda: set_global_train_misc_flag(3)
