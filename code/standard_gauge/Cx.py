import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro, standard_gauge, standard_gauge_1500v


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
        'Trivia': '''The C3 lacked proper cabs and were therefore always sandwiched  between other units though they had a small control panel it was only used for swtiching''',
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
    purchase_sprite_towed_id='s_e_C4_1_ss_car2',
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
    purchase_sprite_towed_id='s_e_C4_1_sl_car2',
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
    purchase_sprite_towed_id='s_e_C5_1_ss_car2',
    company='ss',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS',
        'Use': 'Stockholm Metro trains',
        'Builder': 'Hägglund',
        'Trivia': '''Its unusual appearance spawned multiple urban legends, often involving the abonded Kymlinge station''',
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

COMMON_9239_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='dual',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(70),
    power=435,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=34,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    country='sweden',
)

s_e_9239_1_sl = Train(
    **COMMON_9239_PROPS,
    id='s_e_9239_1_sl',
    name='SL 9239',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C1roof', '9239'],
        paint=['9239sl'],
        overlay=('9239lights+props',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Works unit',
        'Builder': 'ASEA, ASJ',
        'Trivia': '''In 1977 a C2 was damaged in a fire and rebuilt into a battery driven works unit''',
    }),
)

#2nd generation of Cx - new front

COMMON_C6_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=metro,
    max_speed=Train.kmhish(90),
    power=1090,
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

#original destination board
s_e_C6_1_sl = Train(
    **COMMON_C6_PROPS,
    id='s_e_C6_1_sl',
    name='SL C6',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A'),
        paint=('C6Ass'),
        overlay=('C6Alights', 'destination1'),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    purchase_sprite_towed_id='s_e_C6_1_sl_car2',
    company='sl',
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASEA, Hägglund',
        'Trivia': '''2789-2790 were rebuilt into C16 for use on Saltsjöbanan'''
    }),
).add_articulated_part(
    id='s_e_C6_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
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
    name='SL C6',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A'),
        paint=('C6Asl1'),
        overlay=('C6Alights', 'destination1'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C6_2_sl_car2',
    company='sl',
    introduction_date=date(1972, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASEA, Hägglund',
        'Trivia': '''2789-2790 were rebuilt into C16 for use on Saltsjöbanan'''
    }),
).add_articulated_part(
    id='s_e_C6_2_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

#new destination board
s_e_C6_3_sl = Train(
    **COMMON_C6_PROPS,
    id='s_e_C6_3_sl',
    name='SL C6',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A'),
        paint=('C6Asl2'),
        overlay=('C6Alights', 'destination2'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C6_3_sl_car2',
    company='sl',
    introduction_date=date(2009, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASEA, Hägglund',
        'Trivia': '''Rebuilt in 2009 to try new seating arrangements with more standing spaces'''
    }),
).add_articulated_part(
    id='s_e_C6_3_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_C8_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=metro,
    max_speed=Train.kmhish(90),
    power=946,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=46,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=158,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C8_1_sl = Train(
    **COMMON_C8_PROPS,
    id='s_e_C8_1_sl',
    name='SL C8',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C8_1_sl_car2',
    company='sl',
    introduction_date=date(1974, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASEA, Hägglund',
        'Trivia': '''Units 2819 and 2821 were rebuilt into C10, units 2820 and 2822 were rebuilt into C11, both for use on Saltsjöbanan''',
    }),
).add_articulated_part(
    id='s_e_C8_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=158,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_C8_2_sl = Train(
    **COMMON_C8_PROPS,
    id='s_e_C8_2_sl',
    name='SL C8',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C8_2_sl_car2',
    company='sl',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro trains',
        'Builder': 'ASEA, Hägglund',
    }),
).add_articulated_part(
    id='s_e_C8_2_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=158,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_C10_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(70),
    power=600,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=46,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=144,
    loading_speed=30,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

#Saltsjöbanan

s_e_C10_1_sl = Train(
    **COMMON_C10_PROPS,
    id='s_e_C10_1_sl',
    name='SL C10',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C11_1_sl_car2',
    company='sl',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Local passenger',
        'Builder': 'ASEA, Hägglund',
    }),
).add_articulated_part(
    id='s_e_C11_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=144,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_C10_2_sl = Train(
    **COMMON_C10_PROPS,
    id='s_e_C10_2_sl',
    name='SL C10',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C11_2_sl_car2',
    company='sl',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Local passenger',
        'Builder': 'ASEA, Hägglund',
    }),
).add_articulated_part(
    id='s_e_C11_2_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=144,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_C16_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(70),
    power=600,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=46,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=134,
    loading_speed=30,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C16_1_sl = Train(
    **COMMON_C16_PROPS,
    id='s_e_C16_1_sl',
    name='SL C16',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1'),
        paint=('2'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    introduction_date=date(1987, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Local passenger',
        'Builder': 'ASEA, Hägglund',
         'Trivia': '''Rebuilt from C6 units 2789-2790'''
    }),
)