from collections import Counter

from nml.grfstrings import NewGRFString, default_lang

import grf


class VehicleSpriteTable(grf.VehicleSpriteTable):
    def add_layout(self, sprites):
        return self.get_layout(self.add_row(sprites))


class Train(grf.Train):

    def _gen_livery_sprites(self, liveries):
        sprites = VehicleSpriteTable(grf.TRAIN)

        layouts = [sprites.add_layout(l['sprites']) for l in self.liveries]

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

        callbacks = grf.CallbackManager(grf.Callback.Vehicle)

        veh_sprites, layout = self._gen_liveries(g, callbacks, self.liveries)

        if self.additional_text:
            callbacks.purchase_text = g.strings.add(self.additional_text).get_global_id()

        if self.sound_effects:
            callbacks.sound_effect = grf.Switch(
                ranges=self.sound_effects,
                default=layout,
                code='extra_callback_info1 & 255',
            )

        if self._articulated_parts:
            callbacks.articulated_part = grf.Switch(
                ranges={i + 1: ap[0] for i, ap in enumerate(self._articulated_parts)},
                default=0x7fff,
                code='extra_callback_info1 & 255',
            )

        if callbacks.get_flags():
            self._props['cb_flags'] = self._props.get('cb_flags', 0) | callbacks.get_flags()

        res = [
            grf.DefineStrings(
                feature=grf.TRAIN,
                offset=self.id,
                is_generic_offset=False,
                strings=[self.name.encode('utf-8')]
            ),
        ]

        res.append(grf.Define(
            feature=grf.TRAIN,
            id=self.id,
            props={
                'sprite_id': 0xfd,  # magic value for newgrf sprites
                'max_speed': self.max_speed,
                **self._props
            }
        ))

        res.append(veh_sprites)

        default, maps = callbacks.make_switch(layout)
        res.append(grf.Action3(
            feature=grf.TRAIN,
            ids=[self.id],
            maps=maps,
            default=default,
        ))

        for apid, liveries, props in self._articulated_parts:
            res.append(grf.Define(
                feature=grf.TRAIN,
                id=apid,
                props={
                    'sprite_id': 0xfd,  # magic value for newgrf sprites
                    'engine_class': self._props.get('engine_class'),
                    **props
                }
            ))

            veh_sprites, layout = self._gen_livery_sprites(liveries)
            res.append(veh_sprites)

            res.append(grf.Action3(
                feature=grf.TRAIN,
                ids=[apid],
                maps={},
                default=layout,
            ))
        return res


set_global_train_y_offset = lambda ofs: grf.ComputeParameters(target=0x8e, operation=0x00, if_undefined=False, source1=0xff, source2=0xff, value=ofs)

set_global_train_misc_flag = lambda pos: grf.ComputeParameters(target=0x9e, operation=0x08, if_undefined=False, source1=0x9e, source2=0xff, value=1 << pos)
set_global_train_depot_width_32 = lambda: set_global_train_misc_flag(3)
