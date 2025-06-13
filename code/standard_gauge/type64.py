import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_type64_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(50),
    power=632,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=35,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=158,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='norway',
)

n_e_type64_1_nsb = Train(
    **COMMON_type64_PROPS,
    id='n_e_type64_1_nsb',
    name='NSB Type 64',
    liveries=make_psd_cc_liveries(
        'pp/type64.psd',
        shading=['type64', 'type64roof'],
        paint='type64nsb',
        overlay=('type64light',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["YELLOW"]
    ),
    company='',
    introduction_date=date(1935, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'NSB',
        'Use': 'Local trains',
        'Builder': 'Strømmen',
    }),
)