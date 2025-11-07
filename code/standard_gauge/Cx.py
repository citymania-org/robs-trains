import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro


COMMON_C2_PROPS = dict(
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
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=138,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C2_1_ss = Train(
    **COMMON_C2_PROPS,
    id='s_e_C2_1',
    name='SS C2',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C1roof'],
        paint=['C1ss'],
        overlay=('C1lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    introduction_date=date(1949, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS',
        'Use': 'Sockholm Metro trains',
        'Builder': 'ASEA, ASJ',
        'Trivia': '''348 units were built, the largest series of any swedish metro train''',
    }),
)

COMMON_C3_PROPS = dict(
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
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=146,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C3_1_ss = Train(
    **COMMON_C3_PROPS,
    id='s_e_C3_1',
    name='SS C3',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C3', 'C1roof'],
        paint=['C1ss'],
        overlay=('C3lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    introduction_date=date(1957, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS',
        'Use': 'Sockholm Metro trains',
        'Builder': 'ASEA, ASJ',
        'Trivia': '''The C3 lacked proper cabs and were therefore always sandwiched  between other units''',
    }),
)

COMMON_C4_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=metro,
    max_speed=Train.kmhish(80),
    power=870,
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

s_e_C4_1_ss = Train(
    **COMMON_C4_PROPS,
    id='s_e_C4_1_ss',
    name='SS C4',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C4A', 'C4Aroof'],
        paint='C4Ass',
        overlay=('C4Alights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASEA, ASJ',
        'Trivia': '''200 were built between 1960 and 1967. They were lighter than their predecessors''',
    }),
).add_articulated_part(
    id='s_e_C4_1_ss_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C4B', 'C4Broof'],
        paint='C4Bss',
        overlay=['C4Blights'],
        cc_replace=colours['GREEN'],
        cc2_replace=colours['GREEN'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_C4_2_sl = Train(
    **COMMON_C4_PROPS,
    id='s_e_C4_2_sl',
    name='SL C4',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C4A', 'C4Aroof'],
        paint='C4Asl',
        overlay=('C4Alights',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    introduction_date=date(1985, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASEA, ASJ',
        'Trivia': '''200 were built between 1960 and 1967. They were lighter than their predecessors''',
    }),
).add_articulated_part(
    id='s_e_C4_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C4B', 'C4Broof'],
        paint='C4Bsl',
        overlay=['C4Blights'],
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

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
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=156,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C5_1_ss = Train(
    **COMMON_C5_PROPS,
    id='s_e_C5_1_ss',
    name='SS C5',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C4A', 'C4Aroof'],
        paint='C4Asl',
        overlay=('C4Alights',),
        cc_replace=colours["GREY5"],
        cc2_replace=colours["GREY5"]
    ),
    company='ss',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS',
        'Use': 'Stockholm Metro trains',
        'Builder': 'Hägglund',
        'Trivia': '''Its unusual look spawned multiple urban legends, often involving the abonded Kymlinge station''',
    }),
).add_articulated_part(
    id='s_e_C5_1_ss_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C4B', 'C4Broof'],
        paint='C4Bsl',
        overlay=['C4Blights'],
        cc_replace=colours['GREY5'],
        cc2_replace=colours['GREY5'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
