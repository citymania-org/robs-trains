import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro

COMMON_C4_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=metro,
    max_speed=Train.kmhish(80),
    power=435,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=23,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=156,
    loading_speed=5,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C4_1_ss = Train(
    **COMMON_C4_PROPS,
    id='s_e_C4_1_ss',
    name='SS/SL C4',
    liveries=make_psd_cc_liveries(
        'pp/1960_SE_C4-A.psd',
        shading='C4',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS/SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASJ',
        'Trivia': ''' ''',
    }),
).add_articulated_part(
    id='s_e_C4_2_ss_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/1960_SE_C4-B.psd',
        shading='C4',
        paint='SS',
        overlay=['Lights'],
        cc_replace=colours['GREEN'],
        cc2_replace=colours['GREEN'],
    ),
    cargo_capacity=0,
    loading_speed=5,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_C4_2_sl = Train(
    **COMMON_C4_PROPS,
    id='s_e_C4_2_sl',
    name='SL C4',
    liveries=make_psd_cc_liveries(
        'pp/1960_SE_C4-A.psd',
        shading='C4',
        paint='SL',
        overlay=('Lights',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    introduction_date=date(1985, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS/SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASJ',
        'Trivia': ''' ''',
    }),
).add_articulated_part(
    id='s_e_C4_2_ss_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/1960_SE_C4-B.psd',
        shading='C4',
        paint='SL',
        overlay=['Lights'],
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=0,
    loading_speed=5,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)