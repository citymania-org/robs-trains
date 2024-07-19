import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_XOA4_PROPS = dict(
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
    weight=46,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=75,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_Xoa4_1_dj = Train(
    **COMMON_XOA4_PROPS,
    id='s_e_Xoa4_1_dj',
    name='DJ Xoa4',
    liveries=make_psd_cc_liveries( # improve later
        'pp/Xoa4.psd',
        overlay=('sj/dj_original', 'Electrical equipment'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1939, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'DJ, SJ',
        'Use': '',
        'Builder': ''
    }),
)

s_e_Xoa4_2_sj = Train(
    **COMMON_XOA4_PROPS,
    id='s_e_Xoa4_2_sj',
    name='SJ Xoa4',
    liveries=make_psd_cc_liveries( # improve later
        'pp/Xoa4.psd',
        overlay=('sj/dj_original', 'sj_brown_mask', 'Electrical equipment'),
        cc_replace=colours["REDBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    company='na',
    introduction_date=date(1950, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SJ',
        'Use': '',
        'Builder': ''
    }),
)