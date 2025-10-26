import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_y1_PROPS = dict( # this is based on the HHJ YM 31
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=26,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=36,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y1_1_dsb = Train(
    id='d_d_y1_1_dsb',
    **COMMON_y1_PROPS,
    name='YM Railbus',
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'HHGB, HHJ',
    }),
)

COMMON_y2_PROPS = dict( # this is based on the LNJ YM 17
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(60),
    power=360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=27,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=58, #43 seats, ca 15 standing = 58
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y2_1_dsb = Train(
    id='d_d_y2_1_dsb',
    **COMMON_y2_PROPS,
    name='YM Railbus',
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Owners': 'LNJ',
    }),
)

COMMON_y3_PROPS = dict( # this is based on the LNJ YS 25
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(60),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=18,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=67, #52 seats, ca 15 standing = 67
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y3_1_dsb = Train(
    id='d_d_y3_1_dsb',
    **COMMON_y3_PROPS,
    name='YS Railbus DVT',
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Owners': 'LNJ',
    }),
)

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

COMMON_y8_PROPS = dict( # this is based on the LJ YP 70
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=17,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y8_1_dsb = Train(
    id='d_d_y8_1_dsb',
    **COMMON_y8_PROPS,
    name='YP',
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
)
