import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_XOA3_A_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(90),
    power=500,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=80,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=50, # and 2t luggage
    loading_speed=5,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_Xoa3_1_bj = Train(
    **COMMON_XOA3_A_PROPS,
    id='s_e_Xoa3_1_bj',
    name='BJ Xoa3',
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Xoa3-A.psd',
        shading='Xoa3-A',
        paint='BJ',
        overlay=('Lights', 'Electrical equipment'),
        cc_replace=colours["RPURPLE"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1939, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'BJ',
        'Use': 'Local trains, 3rd class',
        'Builder': 'ASEA'
    }),
).add_articulated_part(
    id='s_e_Xoa3_1_bj_car2',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Xoa3-B.psd',
        shading='Xoa3-B',
        paint='BJ',
        overlay='Lights',
        cc_replace=colours['RPURPLE'],
        cc2_replace=colours['CREAM'],
    ),
    cargo_capacity=72,
    loading_speed=5,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_Xoa3_2_sj = Train(
    **COMMON_XOA3_A_PROPS,
    id='s_e_Xoa3_2_sj',
    name='SJ Xoa3',
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Xoa3-A.psd',
        shading='Xoa3-A',
        paint='SJ_brown',
        overlay=('Lights', 'Electrical equipment'),
        cc_replace=colours["REDBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    company='na',
    introduction_date=date(1948, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SJ',
        'Use': 'Local trains, 3rd class',
        'Builder': 'ASEA'
    }),
).add_articulated_part(
    id='s_e_Xoa3_2_sj_car2',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Xoa3-B.psd',
        shading='Xoa3-B',
        #paint='',
        overlay='Lights',
        cc_replace=colours['REDBROWN'],
        cc2_replace=colours['REDBROWN'],
    ),
    cargo_capacity=72,
    loading_speed=5,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)