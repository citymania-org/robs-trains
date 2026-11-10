import grf

from grf.lib.callback import make_callback_manager

BADGES = grf.dev.add_feature(0x15, 'badges', 'Badge', variables={'intro_date': {'var': 0x40, 'start':  0, 'size': 32},}, is_vehicle_feature=True)

class Badge(grf.SpriteGenerator):

    class Flags():
        COPY_TO_RELATED_ENTITY = 0x01
        NAME_LIST_STOP = 0x02
        NAME_LIST_FIRST_ONLY = 0x04
        USE_COMPANY_COLOUR = 0x08
        NAME_SKIP = 0x16

    def __init__(self, label, name=None, icon=(None, None), **props):
        self.name = name
        self.label = label
        self.icon = icon
        self._props = props

    def _gen_name_sprites(self, g, bid):
        if isinstance(self.name, grf.StringRef):
            return self.name.get_actions(BADGES, bid)
        else:
            return g.strings.add(self.name).get_actions(BADGES, bid)

    def get_sprites(self, g):
        
        res = []
        
        if self.icon[0] is not None:
            res = self.icon[0]

        if self.icon[1] is not None:
            self.callbacks = make_callback_manager(BADGES, None)
            self.callbacks.graphics.default = self.icon[1]

        bid = g.resolve_id(BADGES, self.label)

        res.append(definition := grf.Define(
            feature=BADGES,
            id=bid,
            props={
                'label': self.label,
                **self._props
            }
        ))
        if self.name is not None:
            res.extend(self._gen_name_sprites(g, bid))

        if self.icon[1] is not None:
            res.extend(self.callbacks.make_map_action(definition))
                
        return res