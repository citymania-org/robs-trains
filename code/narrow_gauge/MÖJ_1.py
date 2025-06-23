import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, extra_narrow_gauge_15kv

COMMON_MÖJ1_PROPS = dict(
    length=4,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(35),
    power=34   ,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=15,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=22,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_MÖJ_1_1_möj = Train(
    **COMMON_MÖJ1_PROPS,
    id='s_e_MÖJ_1_1_möj',
    name='MÖJ 1 "Ankan"',
    liveries=make_psd_cc_liveries(
        'pp/MÖJ_1.psd',
        shading='MÖJ 1',
        paint=['möj'],
        overlay=('möjlights'),
        cc_replace=colours["SJBROWN"],
        cc2_replace=colours["SJBROWN"]
    ),
    company='na',
    introduction_date=date(1907, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'MÖJ',
        'Use': 'Universal',
        'Builder': 'ASEA'
    }),
)