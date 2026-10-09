
from datetime import date

import grf, lib

from common import g

class RandomTrain(lib.Train):
    def __init__(self, *, liveries, country=None, company=None, power_type=None, purchase_sprite_towed_id=None, visual_effect=None, mid_stats=None, end_stats=None, track_type=None, default_cargo_type=None, shorten_by=None, **kw):
        
        kw['misc_flags'] = kw.get('misc_flags', 0) | self.Flags.USE_CARGO_MULT
        
        if visual_effect != None:
            if visual_effect[1] >= 24:
                raise Exception("Train visual effect may not be outside the train")
        self.visual_effect = visual_effect
            
        self.mid_stats = mid_stats
        self.end_stats = end_stats
        if kw['length'] <= 8 and (mid_stats or end_stats) != None:
            raise Exception('length must (currently) be more than 8 for multi-capacity trains')

        if kw.get('intermediate_graphics_chain') is not None:
            del kw['intermediate_graphics_chain']
            print(kw['name'], 'weird code???????')

        if track_type is not None:
            if isinstance(track_type, (tuple, list)):
                track_type = tuple(track_type)
                if len(track_type) == 1:
                    kw['track_type'] = track_type[0]
                else:
                    kw['track_types'] = track_type
            else:
                kw['track_type'] = track_type
        
        grf.Train.__init__(self,
            liveries=liveries,
            default_cargo_type=grf.DEFAULT_CARGO_FIRST_REFITTABLE,
            **kw
        )
        
        self.country = country
        self.company = company
        self.power_type = power_type
        self.purchase_sprite_towed_id = purchase_sprite_towed_id
        
        # Add visual effect to this part if it is specified in the front. We add it to the other parts further down
        mid_shorten, art_shorten, art_liveries = self._calc_length_articulation(
            kw['length'], kw.get('shorten_by'), liveries)
        if visual_effect is not None:
            if visual_effect[1] <= (8 - art_shorten):
                self._props['visual_effect_and_powered'] = self.visual_effect_and_powered(visual_effect[0], position=visual_effect[1], wagon_power=False)
            else :
                self._props['visual_effect_and_powered'] = self.visual_effect_and_powered(self.VisualEffect.DISABLE, wagon_power=False)

        
RandomTrain = g.bind(RandomTrain)

def create_random_train(id, name, subtrains):
    main = subtrains[0][0]
    train_tree = {}
    for i, stm in enumerate(subtrains):
        train_tree[i] = {}
        for j, train in enumerate(stm):
            train_tree[i][j] = train

    # todo add date based random switches / reverse order?
    # random switch ✅
    #   date ✅
    # fix date being when the previus one stoped
    

    def fun_sw_graphics(layout):
        
        switches = []
        for tm in train_tree.values():
            if len(tm) != 1:
                ranges = []
                for i in tm:
                    if i == len(tm) - 1:
                        sw_service = grf.Switch('date_of_last_service', ranges=ranges, default=layout[tm[i].id + '_sprites'])
                        sw_current = grf.Switch('current_date', ranges=ranges, default=layout[tm[i].id + '_sprites'])
                    else:
                        ranges.append(grf.Range(grf.date_to_days(tm[i]._props['introduction_date']), grf.date_to_days(tm[i + 1]._props['introduction_date']), layout[tm[i].id + '_sprites']))
                        
                switches.append(grf.Switch('vehicle_is_in_depot', ranges={
                    1: sw_current
                }, default = sw_service))
            else:
                switches.append(layout[tm[0].id + '_sprites'])
        
        
        return grf.RandomSwitch(scope='self', triggers=0, cmp_all=False, lowest_bit=16 - len(switches).bit_length(), groups=switches)
    
    # merge liveries from all train into one combined property value
    
    capacities = []
    weights = []
    
    liveries = {}
    for tm in train_tree.values():
        for train in tm.values():
            for livery in train.liveries:
                subtype = livery['name']
                for ls in livery['livery_sprites']:
                    if liveries.get(subtype) == None:
                        liveries[subtype] = {
                            'name': subtype,
                            'sprites': ls.sprites[0], # we need this for purchase sprites
                            'livery_sprites': [],
                            'intermediate_graphics_chain': fun_sw_graphics,
                        }
                    if ls not in liveries[subtype]['livery_sprites']:
                        ls.name = train.id + '_' + ls.name
                        liveries[subtype]['livery_sprites'].append(ls)
        capacity = list(tm.values())[0]._props['cargo_capacity']
        if list(tm.values())[0].callbacks.properties.cargo_capacity is not None:
            if list(tm.values())[0].callbacks.properties.cargo_capacity.default is not None:
                capacity = list(tm.values())[0].callbacks.properties.cargo_capacity.default
        capacities.append(capacity)
        weights.append(list(tm.values())[0].weight)
    
    liveries = list(liveries.values())
    
    sw_cargo_capacity = grf.RandomSwitch(scope='relative', count=1, triggers=0, cmp_all=False, lowest_bit=16 - len(capacities).bit_length(), groups=capacities, feature=grf.TRAIN)
    sw_cargo_capacity = grf.Switch('TEMP[100] = 1', ranges={1: sw_cargo_capacity}, default=sw_cargo_capacity)
    
    sw_weight = grf.RandomSwitch(scope='relative', count=1, triggers=0, cmp_all=False, lowest_bit=16 - len(weights).bit_length(), groups=weights, feature=grf.TRAIN)
    sw_weight = grf.Switch('TEMP[100] = 1', ranges={1: sw_weight}, default=sw_weight)
    
    callbacks = {
        'cargo_capacity': sw_cargo_capacity,
        'properties': {'weight': sw_weight}
        }

    res = RandomTrain(liveries=liveries, id=id, name=name, max_speed=main.max_speed, weight=main.weight, length=main.length, callbacks=callbacks, **main._props)
    
    return res
            
                
        
                