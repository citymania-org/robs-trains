import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, extra_narrow_gauge_15kv

COMMON_MÖJ1_PROPS = dict(
    length=5,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(40),
    power=140   ,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=24,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    country='sweden',
)

s_e_MÖJ_2to5_1_möj = Train(
    **COMMON_MÖJ1_PROPS,
    id='s_e_MÖJ_2to5_1_möj',
    name='MÖJ 2-5 (early)',
    liveries=make_psd_cc_liveries(
        'pp/MÖJ_2to5.psd',
        shading='MÖJ 2-5',
        paint=['möj', 'Wood'],
        overlay=('möjlights'),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    company='na',
    introduction_date=date(1915, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'MÖJ',
        'Use': 'Universal',
        'Builder': 'ASJ/NEFA'
    }),
)

COMMON_MÖJ2_PROPS = dict(
    length=5,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(70),
    power=280,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=24,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    country='sweden',
)

s_e_MÖJ_2to5_2_möj = Train(
    **COMMON_MÖJ2_PROPS,
    id='s_e_MÖJ_2to5_2_möj',
    name='MÖJ 2-5',
    liveries=make_psd_cc_liveries(
        'pp/MÖJ_2to5.psd',
        shading=['MÖJ 2-5', 'Wood', 'möj1936'],
        paint='möj',
        overlay=('möjlights'),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    company='na',
    introduction_date=date(1936, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'MÖJ',
        'Use': 'Local passenger',
        'Builder': 'ASJ/NEFA'
    }),
)
