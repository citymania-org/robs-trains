import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_mp_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(200),
    power=1502,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=102,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mp2_1_dsb = Train(
    id='d_d_mp2_1_dsb',
    **COMMON_mp_PROPS,
    name='њDSB MP (IC2)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    introduction_date=date(2011, 1, 1),
    cargo_capacity=57,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, up to 4 IC2 or IC4 can be coupled together into a train set',
        'Trivia': 'Meant to be delivered from 2004, all retired by 2016',
    }),
).add_articulated_part(
    id='d_d_mp22_1_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mp2_2_dsb = Train(
    id='d_d_mp2_2_dsb',
    **COMMON_mp_PROPS,
    name='њDSB MP (IC2)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    introduction_date=date(2012, 1, 1),
    cargo_capacity=57,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, up to 4 IC2 or IC4 can be coupled together into a train set',
        'Trivia': 'Meant to be delivered from 2004, all retired by 2016',
    }),
).add_articulated_part(
    id='d_d_mp22_2_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_mg_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(200),
    power=3004,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=163,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mg_1_dsb = Train(
    id='d_d_mg_1_dsb',
    **COMMON_mg_PROPS,
    name='њDSB MG (IC4)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    introduction_date=date(2007, 1, 1),
    cargo_capacity=51,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, up to 4 IC2 or IC4 can be coupled together into a train set',
        'Trivia': 'Meant to be delivered from 2003',
    }),
).add_articulated_part(
    id='d_d_mg2_1_dsb',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=51,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_d_mg3_1_dsb',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=51,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_d_mg4_1_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=51,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mg_2_dsb = Train(
    id='d_d_mg_2_dsb',
    **COMMON_mg_PROPS,
    name='њDSB MG (IC4)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    introduction_date=date(2012, 1, 1),
    cargo_capacity=51,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, up to 4 IC2 or IC4 can be coupled together into a train set',
        'Trivia': 'Meant to be delivered from 2003',
    }),
).add_articulated_part(
    id='d_d_mg2_2_dsb',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=51,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_d_mg3_2_dsb',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=51,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_d_mg4_2_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=51,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
