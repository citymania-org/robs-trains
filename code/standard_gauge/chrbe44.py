import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_44_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(125),
    power=2703,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=68,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=64,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rbe44_1 = Train(
    **COMMON_44_PROPS,
    id='ch_e_rbe44_1',
    name='SBB RBe 4/4',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1959, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as RBe 540',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['passengers'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_e_rbe44_2 = Train(
    **COMMON_44_PROPS,
    id='ch_e_rbe44_2',
    name='SBB RBe 4/4',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as RBe 540',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['passengers'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_e_rbe44_3 = Train(
    **COMMON_44_PROPS,
    id='ch_e_rbe44_3',
    name='SBB RBe 4/4',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as RBe 540',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['passengers'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

COMMON_1212_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(125),
    power=3323,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=170,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=120, #200 seats, 0 collapsible seats, ca 160 standing = 360
    loading_speed=20,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabde1212_1 = Train(
    **COMMON_1212_PROPS,
    id='ch_e_rabde1212_1',
    name='SBB RABDe 12/12',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["NSBRED"]
    ),
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Info': 'Up to 4 can be coupled together into a train set',
        'Trivia': 'Later classed as RABDe 510',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabde12122_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['NSBRED'],
        cc2_replace=colours['NSBRED'],
    ),
    cargo_capacity=120,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabde12123_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['NSBRED'],
        cc2_replace=colours['NSBRED'],
    ),
    cargo_capacity=120,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabde1212_2 = Train(
    **COMMON_1212_PROPS,
    id='ch_e_rabde1212_2',
    name='SBB RABDe 12/12',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Info': 'Up to 4 can be coupled together into a train set',
        'Trivia': 'Later classed as RABDe 510',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabde12122_2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=120,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabde12123_2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=120,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
