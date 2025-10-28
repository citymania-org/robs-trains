COMMON_y4_PROPS = dict( # this is based on the LJ YM 60 and LJ YS 80
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=43,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    dual_headed=1,
    cargo_capacity=95,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y4_1_dsb = Train(
    id='d_d_y4_1_dsb',
    **COMMON_y4_PROPS,
    name='YM-YS',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('y41',),
        paint=('y41lj1',),
        overlay=('y41light'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'LJ',
    }),
).add_articulated_part(
    id='d_d_y42_1_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_y5_PROPS = dict( # this is based on the LJ YM 60
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=720,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=50,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    dual_headed=1,
    cargo_capacity=79,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y5_1_dsb = Train(
    id='d_d_y5_1_dsb',
    **COMMON_y5_PROPS,
    name='YM-YM',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'LJ',
    }),
).add_articulated_part(
    id='d_d_y52_1_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_y6_PROPS = dict( # this is based on the OHJ YM 51 and LJ YS 80
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=44,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    dual_headed=1,
    cargo_capacity=105,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y6_1_dsb = Train(
    id='d_d_y6_1_dsb',
    **COMMON_y6_PROPS,
    name='OHJ YM-YS',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'X',
    }),
).add_articulated_part(
    id='d_d_y62_1_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y6_2_dsb = Train(
    id='d_d_y6_2_dsb',
    **COMMON_y6_PROPS,
    name='VLTJ YM-YS',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    introduction_date=date(1983, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'Three locomotives bought in 1983 #12, #13, #14, named Storåen, Vigen and Tangen',
    }),
).add_articulated_part(
    id='d_d_y62_2_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y6_3_dsb = Train(
    id='d_d_y6_3_dsb',
    **COMMON_y6_PROPS,
    name='VLTJ YM-YS',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'One more locomotive was bought from NJ in 2005 #16, named Heden',
    }),
).add_articulated_part(
    id='d_d_y62_3_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_y7_PROPS = dict( # this is based on the OHJ YM 51
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=720,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=52,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    dual_headed=1,
    cargo_capacity=99,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y7_1_dsb = Train(
    id='d_d_y7_1_dsb',
    **COMMON_y7_PROPS,
    name='OHJ YM-YM',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'X',
    }),
).add_articulated_part(
    id='d_d_y72_1_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y7_2_dsb = Train(
    id='d_d_y7_2_dsb',
    **COMMON_y7_PROPS,
    name='VLTJ YM-YM',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    introduction_date=date(1983, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'Three locomotives bought in 1983 #12, #13, #14, named Storåen, Vigen and Tangen',
    }),
).add_articulated_part(
    id='d_d_y72_2_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y7_3_dsb = Train(
    id='d_d_y7_3_dsb',
    **COMMON_y7_PROPS,
    name='VLTJ YM-YM',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'One more locomotive was bought from NJ in 2005 #16, named Heden',
    }),
).add_articulated_part(
    id='d_d_y72_3_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
