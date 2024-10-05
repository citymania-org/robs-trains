import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro

COMMON_C1_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=metro,
    max_speed=Train.kmhish(80),
    power=500,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=152,
    loading_speed=5,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C1_1_ss = Train(
    **COMMON_C1_PROPS,
    id='s_e_C1_1',
    name='SS/SL C1',
    liveries=make_psd_cc_liveries(
        'pp/1949_SE_C1.psd',
        shading='C1',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    introduction_date=date(1949, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS/SL',
        'Use': 'Sockholm Metro trains',
        'Builder': 'ASJ',
        'Trivia': '''First metro train for Stockholm.''',
    }),
)