import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_x10_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(140),
    power=1717,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=100,
    loading_speed=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x10_1_sj = Train(
    id='s_e_x10_1_sj',
    **COMMON_x10_PROPS,
    name='њSL X10',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1982, 1, 1),
    cargo_capacity=175,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x102_1_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['DBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x10_2_sj = Train(
    id='s_e_x10_2_sj',
    **COMMON_x10_PROPS,
    name='њLM X10',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["LAVENDER"]
    ),
    introduction_date=date(1983, 1, 1),
    cargo_capacity=175,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x102_2_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['COLBALT'],
        cc2_replace=colours['LAVENDER'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x10_3_sj = Train(
    id='s_e_x10_3_sj',
    **COMMON_x10_PROPS,
    name='њGL X10',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1985, 1, 1),
    cargo_capacity=175,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x102_3_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x10_4_sj = Train(
    id='s_e_x10_4_sj',
    **COMMON_x10_PROPS,
    name='њSL X10',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1996, 1, 1),
    cargo_capacity=175,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x102_4_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x10_5_sj = Train(
    id='s_e_x10_5_sj',
    **COMMON_x10_PROPS,
    name='њSL X10',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY4"]
    ),
    introduction_date=date(1999, 1, 1),
    cargo_capacity=175,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x102_5_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY4'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x10_6_sj = Train(
    id='s_e_x10_6_sj',
    **COMMON_x10_PROPS,
    name='њTÅGAB X10',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY4"]
    ),
    introduction_date=date(2017, 1, 1),
    cargo_capacity=175,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x102_6_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY4'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x10_7_sj = Train(
    id='s_e_x10_7_sj',
    **COMMON_x10_PROPS,
    name='њSaga Rail X10',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["PINK"],
        cc2_replace=colours["GREY10"]
    ),
    introduction_date=date(2017, 1, 1),
    cargo_capacity=175,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x102_7_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['PINK'],
        cc2_replace=colours['GREY10'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_x11_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(140),
    power=1717,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=107,
    loading_speed=20,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x11_1_sj = Train(
    id='s_e_x11_1_sj',
    **COMMON_x11_PROPS,
    name='њLM X11',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["LAVENDER"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1994, 1, 1),
    cargo_capacity=167,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x112_1_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['LAVENDER'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x11_2_sj = Train(
    id='s_e_x11_2_sj',
    **COMMON_x11_PROPS,
    name='њGL X11',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1994, 1, 1),
    cargo_capacity=167,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x112_2_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x11_3_sj = Train(
    id='s_e_x11_3_sj',
    **COMMON_x11_PROPS,
    name='њVästtrafik X11',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY4"]
    ),
    introduction_date=date(2004, 1, 1),
    cargo_capacity=167,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x112_3_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY4'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x11_4_sj = Train(
    id='s_e_x11_4_sj',
    **COMMON_x11_PROPS,
    name='њKrösatågen X11',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(2011, 1, 1),
    cargo_capacity=167,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x112_4_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x11_5_sj = Train(
    id='s_e_x11_5_sj',
    **COMMON_x11_PROPS,
    name='њNorrtåg X11',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["SKY"]
    ),
    introduction_date=date(2011, 1, 1),
    cargo_capacity=167,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x112_5_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['SKY'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_x12_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(160),
    power=1717,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=103,
    loading_speed=10,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x12_1_sj = Train(
    id='s_e_x12_1_sj',
    **COMMON_x12_PROPS,
    name='њSJ X12',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1991, 1, 1),
    cargo_capacity=114,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x122_1_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x12_2_sj = Train(
    id='s_e_x12_2_sj',
    **COMMON_x12_PROPS,
    name='њVästtrafik X12',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY4"]
    ),
    introduction_date=date(2008, 1, 1),
    cargo_capacity=114,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x122_2_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY4'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x12_3_sj = Train(
    id='s_e_x12_3_sj',
    **COMMON_x12_PROPS,
    name='њSJ X12',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY7"]
    ),
    introduction_date=date(2012, 1, 1),
    cargo_capacity=114,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x122_3_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY4'],
        cc2_replace=colours['GREY7'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_x14_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(160),
    power=1717,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=103,
    loading_speed=20,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x14_1_sj = Train(
    id='s_e_x14_1_sj',
    **COMMON_x14_PROPS,
    name='њSJ X14',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1994, 1, 1),
    cargo_capacity=142,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x142_1_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x14_2_sj = Train(
    id='s_e_x14_2_sj',
    **COMMON_x14_PROPS,
    name='њGL X14',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1994, 1, 1),
    cargo_capacity=142,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x142_2_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x14_3_sj = Train(
    id='s_e_x14_3_sj',
    **COMMON_x14_PROPS,
    name='њÖstgötatrafiken X14',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1994, 1, 1),
    cargo_capacity=142,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x142_3_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY1'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x14_4_sj = Train(
    id='s_e_x14_4_sj',
    **COMMON_x14_PROPS,
    name='њÖstgötatrafiken X14',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["ORANGE"]
    ),
    introduction_date=date(2003, 1, 1),
    cargo_capacity=142,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x142_4_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['ORANGE'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x14_5_sj = Train(
    id='s_e_x14_5_sj',
    **COMMON_x14_PROPS,
    name='њVästtrafik X14',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY4"]
    ),
    introduction_date=date(2010, 1, 1),
    cargo_capacity=142,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x142_5_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY4'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x14_6_sj = Train(
    id='s_e_x14_6_sj',
    **COMMON_x14_PROPS,
    name='њKrösatågen X14',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(2015, 1, 1),
    cargo_capacity=142,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Meatball transport',
    }),
).add_articulated_part(
    id='s_e_x142_6_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
