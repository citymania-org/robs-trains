import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_120_PROPS = dict(
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
    max_speed=Train.kmhish(200),
    power=7614,
    weight=84,
)

de_e_120_1 = Train(
    id='de_e_120_1',
    **COMMON_120_PROPS,
    name='DB 120',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DBRED"],
        cc2_replace=colours["DCREAM"]
    ),
    introduction_date=date(1979, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)

de_e_120_2 = Train(
    id='de_e_120_2',
    **COMMON_120_PROPS,
    name='DB 120',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1986, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)

de_e_120_3 = Train(
    id='de_e_120_3',
    **COMMON_120_PROPS,
    name='DB 120',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)

COMMON_101_PROPS = dict(
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
    max_speed=Train.kmhish(220),
    power=8702,
    weight=84,
)

de_e_101_1 = Train(
    id='de_e_101_1',
    **COMMON_101_PROPS,
    name='DB 101',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)

de_e_101_2 = Train(
    id='de_e_101_2',
    **COMMON_101_PROPS,
    name='DB 101',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)

de_e_101_3 = Train(
    id='de_e_101_3',
    **COMMON_101_PROPS,
    name='DB 101',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["DCREAM"]
    ),
    introduction_date=date(2017, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)

de_e_101_4 = Train(
    id='de_e_101_4',
    **COMMON_101_PROPS,
    name='DB 101',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DBRED"],
        cc2_replace=colours["DCREAM"]
    ),
    introduction_date=date(2018, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)

de_e_101_5 = Train(
    id='de_e_101_5',
    **COMMON_101_PROPS,
    name='DB 101',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2021, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)
