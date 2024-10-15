import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_X1_A_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(120),
    power=1500,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=78,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=148,
    loading_speed=5,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_X1_1_sj = Train(
    **COMMON_X1_A_PROPS,
    id='s_e_X1_1_sj',
    name='SJ/SL X1',
    liveries=make_psd_cc_liveries(
        'pp/1968_SE_X1-A.psd',
        shading='X1',
        paint='SJ',
        overlay=('Lights', 'Electrical equipment'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["BLUE"]
    ),
    company='sj_70s',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SJ',
        'Use': 'Commuter trains',
        'Builder': 'ASEA',
        'Trivia': '''Developed from the X6. One unit was modified for tilt and high speed research''',
    }),
).add_articulated_part(
    id='s_e_X1_1_sj_car2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/1968_SE_X1-B.psd',
        shading='X1',
        paint='SJ',
        overlay=['Lights', 'Details'],
        cc_replace=colours['BLUE'],
        cc2_replace=colours['BLUE'],
    ),
    cargo_capacity=148,
    loading_speed=5,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_X1_2_sl = Train(
    **COMMON_X1_A_PROPS,
    id='s_e_X1_2_sl',
    name='SL X1',
    liveries=make_psd_cc_liveries(
        'pp/1968_SE_X1-A.psd',
        shading='X1 1988 rebuild',
        paint='SL_1',
        overlay=('Lights', 'Electrical equipment'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    introduction_date=date(1988, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Commuter trains',
        'Builder': 'ASEA',
        'Trivia': '''Rebuilt to increase reliability in cold weather.''',
    }),
).add_articulated_part(
    id='s_e_X1_2_sl_car2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/1968_SE_X1-B.psd',
        shading='X1',
        paint='SL_1',
        overlay=['Lights', 'Details'],
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=148,
    loading_speed=5,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_X1_3_sl = Train(
    **COMMON_X1_A_PROPS,
    id='s_e_X1_3_sl',
    name='SL X1',
    liveries=make_psd_cc_liveries(
        'pp/1968_SE_X1-A.psd',
        shading='X1 1988 rebuild',
        paint='SL_2',
        overlay=('Lights', 'Electrical equipment'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Commuter trains',
        'Builder': 'ASEA',
        'Trivia': '''Two sets that were given the same livery as contemporary metro stock.''',
    }),
).add_articulated_part(
    id='s_e_X1_3_sl_car2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/1968_SE_X1-B.psd',
        shading='X1',
        paint='SL_2',
        overlay=['Lights', 'Details'],
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=148,
    loading_speed=5,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)