import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges, standard_gauge_25kv_15kv

COMMON_5210_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(160),
    power=3535,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=120,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=115, #161 seats, 0 collapsible seats, ca 297 standing = 458
    loading_speed=20,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabe5210_1 = Train(
    id='ch_e_rabe5210_1',
    **COMMON_5210_PROPS,
    purchase_sprite_towed_id='ch_e_rabe52102_1',
    name='SBB RABe 521.0',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2004, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabe52102_1',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=114,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52103_1',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=114,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52104_1',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=115,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabe5210_2 = Train(
    id='ch_e_rabe5210_2',
    **COMMON_5210_PROPS,
    purchase_sprite_towed_id='ch_e_rabe52102_2',
    name='SBB RABe 521.0', #full red doors
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2017, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabe52102_2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=114,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52103_2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=114,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52104_2',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=115,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_5212_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(160),
    power=3535,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=120,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=112, #163 seats, 0 collapsible seats, ca 284 standing = 447
    loading_speed=15,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabe5212_1 = Train(
    id='ch_e_rabe5212_1',
    **COMMON_5212_PROPS,
    purchase_sprite_towed_id='ch_e_rabe52122_1',
    name='SBB RABe 521.2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '15',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabe52122_1',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=112,
    loading_speed=15,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52123_1',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=112,
    loading_speed=15,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52124_1',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=111,
    loading_speed=15,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_5222_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_25kv_15kv,
    max_speed=Train.kmhish(160),
    power=3535,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=120,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=92, #156 seats, 0 collapsible seats, ca 209 standing = 365
    loading_speed=20,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabe5222_1 = Train(
    id='ch_e_rabe5222_1',
    **COMMON_5222_PROPS,
    purchase_sprite_towed_id='ch_e_rabe52222_1',
    name='SBB RABe 522.2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2011, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv_25kv', 'electric/ac/15kv', 'electric/ac/25kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabe52222_1',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=91,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52223_1',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=91,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52224_1',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=91,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabe5222_2 = Train(
    id='ch_e_rabe5222_2',
    **COMMON_5222_PROPS,
    purchase_sprite_towed_id='ch_e_rabe52222_2',
    name='SBB RABe 522.2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2017, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv_25kv', 'electric/ac/15kv', 'electric/ac/25kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabe52222_2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=91,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52223_2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=91,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabe52224_2',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=91,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
