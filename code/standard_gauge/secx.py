import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro, standard_gauge, standard_gauge_1500v, badges


COMMON_C2_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
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
)

s_e_C2_1_ss = Train(
    **COMMON_C2_PROPS,
    id='s_e_C2_1_ss',
    name='њSS C2',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C1roof'],
        paint=['C1ss'],
        overlay=('C1lights',),
        r_overlay=('C1lightsr'),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    introduction_date=date(1949, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''348 units were built, the largest series of any swedish metro train''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/ss'],
        'manufacturer': ['SE/asea', 'SE/asj'],
    }),
)

s_e_C2_2_sl = Train(
    **COMMON_C2_PROPS,
    id='s_e_C2_2_sl',
    name='њSL C2',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C1roof'],
        paint=['C1sl'],
        overlay=('C1lights',),
        r_overlay=('C1lightsr'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1985, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''348 units were built, the largest series of any swedish metro train''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/ss'],
        'manufacturer': ['SE/asea', 'SE/asj'],
    }),
)

COMMON_C3_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
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
)

s_e_C3_1_ss = Train(
    **COMMON_C3_PROPS,
    id='s_e_C3_1_ss',
    name='њSS C3',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C3', 'C1roof'],
        paint=['C1ss'],
        overlay=('C3lights',),
        r_overlay=('C3lightsr'),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    introduction_date=date(1957, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''The C3 lacked proper cabs and were therefore always sandwiched between other units though they had a small control panel it was only used for swtiching''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/ss'],
        'manufacturer': ['SE/asea', 'SE/asj'],
    }),
)

s_e_C3_2_sl = Train(
    **COMMON_C3_PROPS,
    id='s_e_C3_2_sl',
    name='њSL C3',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C3', 'C1roof'],
        paint=['C1sl'],
        overlay=('C3lights',),
        r_overlay=('C3lightsr'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1985, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''The C3 lacked proper cabs and were therefore always sandwiched between other units though they had a small control panel it was only used for swtiching''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/ss'],
        'manufacturer': ['SE/asea', 'SE/asj'],
    }),
)

COMMON_C4_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
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
)

s_e_C4_1_ss = Train(
    **COMMON_C4_PROPS,
    id='s_e_C4_1_ss',
    name='њSS C4',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C4A', 'C4Aroof'],
        paint='C4Ass',
        overlay=('C4Alights',),
        r_overlay=('C4Blights'),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    purchase_sprite_towed_id='s_e_C4_1_ss_car2',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''200 were built between 1960 and 1967. They were lighter than their predecessors and coupled in pairs''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/ss'],
        'manufacturer': ['SE/asea', 'SE/asj'],
    }),
).add_articulated_part(
    id='s_e_C4_1_ss_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C4B', 'C4Broof'],
        paint='C4Bss',
        overlay=['C4Blights'],
        r_overlay=('C4Alights'),
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
    name='њSL C4',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C4A', 'C4Aroof'],
        paint='C4Asl',
        overlay=('C4Alights',),
        r_overlay=('C4Blights'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C4_1_sl_car2',
    company='sl',
    introduction_date=date(1985, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''200 were built between 1960 and 1967. They were lighter than their predecessors''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/asj'],
    }),
).add_articulated_part(
    id='s_e_C4_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C4B', 'C4Broof'],
        paint='C4Bsl',
        overlay=['C4Blights'],
        r_overlay=('C4Alights'),
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
)

s_e_C5_1_ss = Train(
    **COMMON_C5_PROPS,
    id='s_e_C5_1_ss',
    name='њSS C5',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C4A', 'C4Aroof'],
        paint='C4Asl',
        overlay=('C4Alights',),
        r_overlay=('C4Blights'),
        cc_replace=colours["GREY5"],
        cc2_replace=colours["GREY5"]
    ),
    purchase_sprite_towed_id='s_e_C5_1_ss_car2',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''Its unusual appearance spawned multiple urban legends, often involving the abonded Kymlinge station''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/ss'],
        'manufacturer': ['SE/haegglund'],
    }),
).add_articulated_part(
    id='s_e_C5_1_ss_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C4B', 'C4Broof'],
        paint='C4Bsl',
        overlay=['C4Blights'],
        r_overlay=('C4Alights'),
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
)

s_e_9239_1_sl = Train(
    **COMMON_9239_PROPS,
    id='s_e_9239_1_sl',
    name='њSL A225 9239',
    liveries=make_psd_cc_liveries(
        'pp/Cx.psd',
        shading=['C1', 'C1roof', '9239'],
        paint=['9239sl'],
        overlay=('9239lights+props',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''In 1977 a C2 was damaged in a fire and rebuilt into a battery driven works unit''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['utility'],
        'power': ['battery'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/asj'],
    }),
)

#2nd generation of Cx - new front

COMMON_C6_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
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
)

#original destination board
s_e_C6_1_sl = Train(
    **COMMON_C6_PROPS,
    id='s_e_C6_1_sl',
    name='њSL C6',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A'),
        paint=('C6Ass'),
        overlay=('C6Adestination1'),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    purchase_sprite_towed_id='s_e_C6_1_sl_car2',
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''2789-2790 were rebuilt into C16 for use on Saltsjöbanan'''
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/haegglund'],
    }),
).add_articulated_part(
    id='s_e_C6_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6B'),
        paint=('C6Bss'),
        overlay=('C6Bdestination1'),
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
    name='њSL C6',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A'),
        paint=('C6Asl1'),
        overlay=('C6Adestination1'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C6_2_sl_car2',
    introduction_date=date(1972, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''2789-2790 were rebuilt into C16 for use on Saltsjöbanan'''
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/haegglund'],
    }),
).add_articulated_part(
    id='s_e_C6_2_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6B'),
        paint=('C6Bsl1'),
        overlay=('C6Bdestination1'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_C6_3_sl = Train(
    **COMMON_C6_PROPS,
    id='s_e_C6_3_sl',
    name='њSL C6',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A'),
        paint=('C6Asl2'),
        overlay=('C6Adestination1'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C6_3_sl_car2',
    introduction_date=date(1990, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': ''''''
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/haegglund'],
    }),
).add_articulated_part(
    id='s_e_C6_3_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6B'),
        paint=('C6Bsl2'),
        overlay=('C6Bdestination1'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

#new destination board
s_e_C6_4_sl = Train(
    **COMMON_C6_PROPS,
    id='s_e_C6_4_sl',
    name='SL C6',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A'),
        paint=('C6Asl3'),
        overlay=('C6Adestination2'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C6_4_sl_car2',
    company='sl',
    introduction_date=date(2009, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''Rebuilt in 2009 to try new seating arrangements with more standing spaces'''
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/haegglund'],
    }),
).add_articulated_part(
    id='s_e_C6_4_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6B'),
        paint=('C6Bsl2'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=156,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_C13_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=metro,
    max_speed=Train.kmhish(80),
    power=435,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=29,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=146,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_C13_1_sl = Train(
    **COMMON_C13_PROPS,
    id='s_e_C13_1_sl',
    name='њSL C13',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A'),
        paint=('C6Agevalia'),
        overlay=('C6Adestination3'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C13_1_sl_car2',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''Promotional train for the coffee company Gevalia. It had a counter staffed by two baristas'''
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['metro'],
        'power': ['third_rail', 'metro'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/haegglund'],
    }),
).add_articulated_part(
    id='s_e_C13_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6B'),
        paint=('C6Bsl2'),
        overlay=('C6Bdestination3'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=158,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

#Saltsjöbanan

COMMON_C10_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
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
)

s_e_C10_1_sl = Train(
    **COMMON_C10_PROPS,
    id='s_e_C10_1_sl',
    name='њSL C10',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A', 'C10'),
        paint=('C6Asl1', 'C10text'),
        overlay=('C10overlay'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C11_1_sl_car2',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['suburban_passenger',],
        'power': ['electric/dc/750v'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/haegglund'],
    }),
).add_articulated_part(
    id='s_e_C11_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6B', 'C11'),
        paint=('C6Bsl1', 'C11text'),
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
    name='њSL C10',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A', 'C10'),
        paint=('C6Asl2', 'C10text'),
        overlay=('C10overlay'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_C11_2_sl_car2',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['suburban_passenger',],
        'power': ['electric/dc/750v'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/haegglund'],
    }),
).add_articulated_part(
    id='s_e_C11_2_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A', 'C11'),
        paint=('C6Bsl2'),
        overlay=('C11overlay'),
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
)

s_e_C16_1_sl = Train(
    **COMMON_C16_PROPS,
    id='s_e_C16_1_sl',
    name='њSL C16',
    liveries=make_psd_cc_liveries(
        'pp/Cx2.psd',
        shading=('C6A', 'C16'),
        paint=('C16sl1', 'C10text'),
        overlay=('C16overlay'),
        r_overlay=('C16overlayr'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1987, 1, 1),
    additional_text=grf.fake_vehicle_info({
         'Trivia': '''Rebuilt from C6 units 2789-2790'''
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['suburban_passenger',],
        'power': ['electric/dc/750v'],
        'operator': ['SE/sl'],
        'manufacturer': ['SE/asea', 'SE/haegglund'],
    }),
)
