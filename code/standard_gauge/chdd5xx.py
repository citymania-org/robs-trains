import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_514_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(140),
    power=4351,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=225,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=245, #378 seats, 0 collapsible seats, ca 600 standing = 978
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabe514_1 = Train(
    **COMMON_514_PROPS,
    id='ch_e_rabe514_1',
    purchase_sprite_towed_id='ch_e_rabe5142_1',
    name='SBB RABe 514',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(2005, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabe5142_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=245,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe5143_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=244,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe5144_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=244,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
