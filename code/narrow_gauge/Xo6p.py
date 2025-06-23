import grf, lib

from datetime import date

from common import Train, Livery, extra_narrow_gauge, colours, make_psd_cc_liveries

COMMON_Xo6p_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge, 
    max_speed=Train.kmhish(85),
    power=440,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=33,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=72,
    loading_speed= 10,
    cost_factor=25, #balance later
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_d_Xo6p_1_srj = Train(
    **COMMON_Xo6p_PROPS,
    id='s_d_Xo6p_1_srj',
    name='њSRJ 3110-3112 "Rydbergare"',
    liveries=make_psd_cc_liveries(
        'pp/Xo6p.psd', 
        shading=['Xo6p', 'srjroof'], 
        paint='srj', 
        overlay='srjlights', 
        cc_replace=colours["DCREAM"], 
        cc2_replace=colours["SEBROWN"],
    ),
    country='sweden',
    company='na',
    introduction_date=date(1957, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SRJ',
        'Use': 'Universal',
        'Builder': 'ASJ'
    }),
)