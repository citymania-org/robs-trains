import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge, badges

COMMON_cc_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    max_speed=Train.kmhish(80),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_cc_1 = Train(
    **COMMON_cc_PROPS,
    id='dk_p_cc_1',
    name='DSB CC II/III', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    cargo_capacity=48,
    weight=18,
    introduction_date=date(1916, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as CU I/II',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['DK/dsb'],
        'manufacturer': [],
    }),
)

dk_p_cc_2 = Train(
    **COMMON_cc_PROPS,
    id='dk_p_cc_2',
    name='DSB CC II/III', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    cargo_capacity=48,
    weight=18,
    introduction_date=date(1917, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as CU I/II',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['DK/dsb'],
        'manufacturer': [],
    }),
)

dk_p_cc_3 = Train(
    **COMMON_cc_PROPS,
    id='dk_p_cc_3',
    name='DSB CU I/II', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    cargo_capacity=48,
    weight=18,
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Vehicles in this class could also appear like the previous 2 in this list',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['DK/dsb'],
        'manufacturer': [],
    }),
)

dk_p_cc_4 = Train(
    **COMMON_cc_PROPS,
    id='dk_p_cc_4',
    name='DSB CD III', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    cargo_capacity=40,
    weight=28,
    introduction_date=date(1916, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as CUK',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['DK/dsb'],
        'manufacturer': [],
    }),
)

dk_p_cc_5 = Train(
    **COMMON_cc_PROPS,
    id='dk_p_cc_5',
    name='DSB CD III', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    cargo_capacity=40,
    weight=28,
    introduction_date=date(1919, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as CUK',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['DK/dsb'],
        'manufacturer': [],
    }),
)

dk_p_cc_6 = Train(
    **COMMON_cc_PROPS,
    id='dk_p_cc_6',
    name='DSB CUK', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    cargo_capacity=40,
    weight=28,
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Vehicles in this class could also appear like the previous 2 in this list, later classed as CU III',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['DK/dsb'],
        'manufacturer': [],
    }),
)
