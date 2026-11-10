import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_103_PROPS = dict(
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
)

de_e_103_1 = Train(
    id='de_e_103_1',
    **COMMON_103_PROPS,
    name='DB E 03', #prototype
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DBRED"],
        cc2_replace=colours["DCREAM"]
    ),
    power=8729,
    weight=112,
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as 103',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
)

de_e_103_2 = Train(
    id='de_e_103_2',
    **COMMON_103_PROPS,
    name='DB 103.1', #production
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DBRED"],
        cc2_replace=colours["DCREAM"]
    ),
    power=10578,
    weight=114,
    introduction_date=date(1970, 1, 1),
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

de_e_103_3 = Train(
    id='de_e_103_3',
    **COMMON_103_PROPS,
    name='DB 103.1', #orient red
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    power=10578,
    weight=114,
    introduction_date=date(1987, 1, 1),
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

de_e_103_4 = Train(
    id='de_e_103_4',
    **COMMON_103_PROPS,
    name='DB 103.1', #lufthansa
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY1"]
    ),
    power=10578,
    weight=114,
    introduction_date=date(1991, 1, 1),
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

de_e_103_5 = Train(
    id='de_e_103_5',
    **COMMON_103_PROPS,
    name='DB 103.1', #tourism 220
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["SKY"]
    ),
    power=10578,
    weight=114,
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

de_e_103_6 = Train(
    id='de_e_103_6',
    **COMMON_103_PROPS,
    name='DB 103.1', #traffic red 233
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    power=10578,
    weight=114,
    introduction_date=date(2000, 1, 1),
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

de_e_103_7 = Train(
    id='de_e_103_7',
    **COMMON_103_PROPS,
    name='DB 103', #prototype 001
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["DCREAM"]
    ),
    power=8729,
    weight=112,
    introduction_date=date(2014, 1, 1),
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

de_e_103_8 = Train(
    id='de_e_103_8',
    **COMMON_103_PROPS,
    name='RADVE 103.1', #radve 222
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["GREY1"]
    ),
    power=10578,
    weight=114,
    introduction_date=date(2015, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['DE/radve'],
        'manufacturer': [],
    }),
)

de_e_103_9 = Train(
    id='de_e_103_9',
    **COMMON_103_PROPS,
    name='DB 103.1', #ocean blue 233
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DTURQUOISE"],
        cc2_replace=colours["DCREAM"]
    ),
    power=10578,
    weight=114,
    introduction_date=date(2025, 1, 1),
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
