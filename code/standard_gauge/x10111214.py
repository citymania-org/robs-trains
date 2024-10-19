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
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x10_1_sl = Train(
    id='s_e_x10_1_sl',
    **COMMON_x10_PROPS,
    name='љњSL X10',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1982, 1, 1),
    cargo_capacity=183,
    additional_text=grf.fake_vehicle_info({
        'Use': 'meatball transport',
    }),
).add_articulated_part(
    id='s_e_x102_1_sl',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
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
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x11_1_sj = Train(
    id='s_e_x11_1_sj',
    **COMMON_x11_PROPS,
    name='љњSJ X11',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1994, 1, 1),
    cargo_capacity=175,
    additional_text=grf.fake_vehicle_info({
        'Use': 'meatball transport',
    }),
).add_articulated_part(
    id='s_e_x112_1_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
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
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x12_1_sj = Train(
    id='s_e_x12_1_sj',
    **COMMON_x12_PROPS,
    name='љњSJ X12',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1991, 1, 1),
    cargo_capacity=121,
    additional_text=grf.fake_vehicle_info({
        'Use': 'meatball transport',
    }),
).add_articulated_part(
    id='s_e_x122_1_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
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
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_x14_1_sj = Train(
    id='s_e_x14_1_sj',
    **COMMON_x14_PROPS,
    name='љњSJ X14',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1994, 1, 1),
    cargo_capacity=195,
    additional_text=grf.fake_vehicle_info({
        'Use': 'meatball transport',
    }),
).add_articulated_part(
    id='s_e_x142_1_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
