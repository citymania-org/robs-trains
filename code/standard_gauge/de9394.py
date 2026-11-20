import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_dre93_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    max_speed=Train.kmhish(70),
    power=3399,
    weight=117,
)

de_e_dre93_1_dr = Train(
    id='de_e_dre93_1_dr',
    **COMMON_dre93_PROPS,
    name='DR E 93',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1933, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
        'Trivia': 'Later classed as DB 193',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/dr'],
        'manufacturer': []
    }),
)

COMMON_dre94_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    weight=119,
)

de_e_dre94_1_dr = Train(
    id='de_e_dre94_1_dr',
    **COMMON_dre94_PROPS,
    name='DR E 94',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    max_speed=Train.kmhish(90),
    power=4487,
    introduction_date=date(1940, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as DB 194 & DR 254',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/dr'],
        'manufacturer': []
    }),
)

de_e_dre94_2_dr = Train(
    id='de_e_dre94_2_dr',
    **COMMON_dre94_PROPS,
    name='DR E 94', #red wheels
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    max_speed=Train.kmhish(90),
    power=4487,
    introduction_date=date(1940, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as DB 194 & DR 254',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/dr'],
        'manufacturer': []
    }),
)

de_e_dre94_3_dr = Train(
    id='de_e_dre94_3_dr',
    **COMMON_dre94_PROPS,
    name='DB 194.5',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    max_speed=Train.kmhish(100),
    power=6363,
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': []
    }),
)

de_e_dre94_4_dr = Train(
    id='de_e_dre94_4_dr',
    **COMMON_dre94_PROPS,
    name='DB 194.5', #red wheels
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    max_speed=Train.kmhish(100),
    power=6363,
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': []
    }),
)

de_e_dre94_5_dr = Train(
    id='de_e_dre94_5_dr',
    **COMMON_dre94_PROPS,
    name='DB 194',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DTURQUOISE"],
        cc2_replace=colours["CREAM"]
    ),
    max_speed=Train.kmhish(90),
    power=4487,
    introduction_date=date(1974, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': []
    }),
)
