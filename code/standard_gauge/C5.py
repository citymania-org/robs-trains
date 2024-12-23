import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro

COMMON_C5_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=metro,
    max_speed=Train.kmhish(80),
    power=708,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=20,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=156,
    loading_speed=20,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C5_1_ss = Train(
    **COMMON_C5_PROPS,
    id='s_e_C5_1_ss',
    name='њSS/SL C5 "Silverpilen"',
    liveries=make_psd_cc_liveries(
        'pp/1960_SE_C4-A.psd',
        shading='C4',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREY5"],
        cc2_replace=colours["GREY5"]
    ),
    company='ss',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS/SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASJ',
        'Trivia': '''Lightweight test train with a aliminium body, commonly known as 'Silverpilen' (silver arrow). Only one set of 8 cars were built. The unconventional look of the train spawned many urban legends surrounding it and the abonded station of Kymlinge.''',
    }),
).add_articulated_part(
    id='s_e_C5_2_ss_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/1960_SE_C4-B.psd',
        shading='C4',
        paint='SS',
        overlay=['Lights'],
        cc_replace=colours['GREY5'],
        cc2_replace=colours['GREY5'],
    ),
    cargo_capacity=156,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
