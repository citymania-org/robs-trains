import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_Yd_PROPS = dict(
    length=5,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=130,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=7,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=24,
    loading_speed=5,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_d_Yd_1_sj = Train(
    **COMMON_Yd_PROPS,
    id='s_d_Yd_1_sj',
    name='SJ Yd',
    liveries=make_psd_cc_liveries(
        'pp/1935_SE_Yd.psd',
        shading='Yd',
        paint='SJ',
        overlay=('Lights', 'Details'),
        cc_replace=colours["CREAM"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1935, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SJ',
        'Use': 'Local trains, 3rd class',
        'Builder': 'Hilding Carlsson'
    }),
)
s_d_Yd_2_hnj = Train(
    **COMMON_Yd_PROPS,
    id='s_d_Yd_2_hnj',
    name='HNJ Yd',
    liveries=make_psd_cc_liveries(
        'pp/1935_SE_Yd.psd',
        shading='Yd',
        paint='HNJ',
        overlay=('Lights', 'Details'),
        cc_replace=colours["RED"],
        cc2_replace=colours["BLACK1"]
    ),
    company='na',
    introduction_date=date(1937, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'HNJ',
        'Use': 'Local trains, 3rd class',
        'Builder': 'Hilding Carlsson'
    }),
)