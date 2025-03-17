import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro

COMMON_C6_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=metro,
    max_speed=Train.kmhish(90),
    power=1087,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=46,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=156,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C6_1_sl = Train(
    **COMMON_C6_PROPS,
    id='s_e_C6_1_sl',
    name='њSL C6"',
    liveries=make_psd_cc_liveries(
        'pp/1970_SE_C6-A.psd',
        shading='C6',
        paint='SL_1',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='sl',
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASJ',
        'Trivia': '''Improved design based on previous metro stock but still compatible. Some were rebuilt to C16 for service on Saltsjöbanan.''',
    }),
).add_articulated_part(
    id='s_e_C6_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/1970_SE_C6-B.psd',
        shading='C6',
        paint='SL_1',
        overlay=['Lights',],
        cc_replace=colours['GREEN'],
        cc2_replace=colours['GREEN'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_C6_2_sl = Train(
    **COMMON_C6_PROPS,
    id='s_e_C6_2_sl',
    name='њSL C6"',
    liveries=make_psd_cc_liveries(
        'pp/1970_SE_C6-A.psd',
        shading='C6',
        paint='SL_2',
        overlay=('Lights', 'Yellow',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASJ',
        'Trivia': '''Improved design based on previous metro stock but still compatible. Some were rebuilt to C16 for service on Saltsjöbanan.''',
    }),
).add_articulated_part(
    id='s_e_C6_2_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/1970_SE_C6-B.psd',
        shading='C6',
        paint='SL_2',
        overlay=['Lights', 'Yellow',],
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)