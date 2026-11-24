import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, badges

COMMON_661_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 6),
    max_speed=Train.kmhish(125),
    power=1951,
    weight=112,
)

yu_d_661_1 = Train(
    id='yu_d_661_1',
    **COMMON_661_PROPS,
    name='JŽ 661.0',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as HŽ 2061',
    }),
    badges=badges.set_train_badges({
        'flag': ['YU'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['YU/jzh'],
    }),
)

yu_d_661_2 = Train(
    id='yu_d_661_2',
    **COMMON_661_PROPS,
    name='JŽ 661.4', #low bonnet
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(1972, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['YU'],
        'role': ['freight'],
        'power': ['diesel'],
        'operator': ['YU/jzh'],
    }),
)

yu_d_661_3 = Train(
    id='yu_d_661_3',
    **COMMON_661_PROPS,
    name='HŽ 2061',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['HR'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['HR/hzh'],
    }),
)
