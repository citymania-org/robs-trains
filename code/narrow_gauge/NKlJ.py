import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, extra_narrow_gauge_15kv

COMMON_AEG_PROPS = dict(
    length=4,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(60),
    power=476,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    country='sweden',
)

s_e_NKlJ_AEG_1_nklj = Train(
    **COMMON_AEG_PROPS,
    id='s_e_NKlJ_AEG_1_nklj',
    name='NKlJ AEG',
    liveries=make_psd_cc_liveries(
        'pp/NKlJ_AEG.psd',
        shading='base',
        paint='1_nklj',
        overlay=('lights', 'electric', 'windows'),
        cc_replace=colours["REDBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    company='na',
    introduction_date=date(1920, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'NKlJ',
        'Use': 'Universal',
        'Builder': 'AEG'
    }),
)

s_e_NKlJ_AEG_2_nklj = Train(
    **COMMON_AEG_PROPS,
    id='s_e_NKlJ_AEG_2_nklj',
    name='NKlJ AEG',
    liveries=make_psd_cc_liveries(
        'pp/NKlJ_AEG.psd',
        shading='base',
        paint='2_nklj',
        overlay=('lights', 'electric'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1920, 1, 1), # needs further investigation
    additional_text=grf.fake_vehicle_info({
        'Operator': 'NKlJ',
        'Use': 'Universal',
        'Builder': 'AEG'
    }),
)
