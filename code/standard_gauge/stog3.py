import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_1500v

d_e_stog3_1_dsb = Train(
    id='d_e_stog3_1_dsb',
    name='њDSB S-Tog 3 Prototype', #with diamond pantos
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(120),
    power=2339,
    introduction_date=date(1979, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=166,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=200, #212 seats, 28 collapsible seats, ca 200 standing = 440
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Class': 'FC-MC-MC-FC',
    }),
).add_articulated_part(
    id='d_e_stog32_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog33_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=39,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog34_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_stog3_2_dsb = Train(
    id='d_e_stog3_2_dsb',
    name='њDSB S-Tog 3 Prototype', #with z pantos
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(120),
    power=2253,
    introduction_date=date(1979, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=166,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=200, #212 seats, 28 collapsible seats, ca 200 standing = 440
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Class': 'FC-MC-MC-FC',
    }),
).add_articulated_part(
    id='d_e_stog32_2_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog33_2_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=39,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog34_2_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_stog3_3_dsb = Train(
    id='d_e_stog3_3_dsb',
    name='њDSB S-Tog 3',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(100),
    power=2253,
    introduction_date=date(1986, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=166,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=200, #212 seats, 28 collapsible seats, ca 200 standing = 440
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Class': 'FC-MC-MC-FC',
    }),
).add_articulated_part(
    id='d_e_stog32_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog33_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=39,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog34_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_stog3_4_dsb = Train(
    id='d_e_stog3_4_dsb',
    name='њDSB S-Tog 3',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(100),
    power=2253,
    introduction_date=date(1993, 1, 1), #bike symbols introduced
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=166,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=200, #212 seats, 28 collapsible seats, ca 200 standing = 440
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Class': 'FC-MC-MC-FC',
    }),
).add_articulated_part(
    id='d_e_stog32_4_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog33_4_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=39,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog34_4_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
