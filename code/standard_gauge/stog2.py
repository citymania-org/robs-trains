import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_1500v

d_e_stog2_1_dsb = Train(
    id='d_e_stog2_1_dsb',
    name='њDSB S-Tog 2 "De Røde S-Tog"',
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
    power=800,
    introduction_date=date(1967, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=70,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=229, #130 seats, 0 collapsible seats, ca 100 standing = 230
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Class': 'MM-FS',
    }),
).add_articulated_part(
    id='d_e_stog22_1_dsb',
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

d_e_stog2_2_dsb = Train(
    id='d_e_stog2_2_dsb',
    name='њDSB S-Tog 2 "De Røde S-Tog"',
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
    power=800,
    introduction_date=date(1968, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=69,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=220, #121 seats, 0 collapsible seats, ca 100 standing = 221
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers with 1st class carriage',
        'Trivia': '7 of these sets existed for use on the Holte – Hillerød line because the local mayors could not imagine their poor citizens having to use a 2nd class carriage on their short distance commute',
        'Class': 'MM-AS',
    }),
).add_articulated_part(
    id='d_e_stog22_2_dsb',
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

#DSB 70s rebranding happens here

d_e_stog2_9_dsb = Train(
    id='d_e_stog2_9_dsb',
    name='њDSB S-Tog 2 "De Røde S-Tog"',
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
    power=800,
    introduction_date=date(1972, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=70,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=229, #130 seats, 0 collapsible seats, ca 100 standing = 230
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Class': 'MM-FS',
    }),
).add_articulated_part(
    id='d_e_stog22_9_dsb',
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

d_e_stog2_3_dsb = Train(
    id='d_e_stog2_3_dsb',
    name='њDSB S-Tog 2 "De Røde S-Tog"',
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
    power=800,
    introduction_date=date(1972, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=69,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=220, #121 seats, 0 collapsible seats, ca 100 standing = 221
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers with ex 1st class carriage',
        'Class': 'MM-FS',
    }),
).add_articulated_part(
    id='d_e_stog22_3_dsb',
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

d_e_stog2_4_dsb = Train(
    id='d_e_stog2_4_dsb',
    name='њDSB S-Tog 2 "De Røde S-Tog"',
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
    power=1600,
    introduction_date=date(1975, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=142,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=200, #260 seats, 0 collapsible seats, ca 200 standing = 460
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Class': 'MM-FU-MU-FS',
    }),
).add_articulated_part(
    id='d_e_stog22_4_dsb',
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
    id='d_e_stog23_4_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=59,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog24_4_dsb',
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

#DSB 1993 bike symbols

d_e_stog2_5_dsb = Train(
    id='d_e_stog2_5_dsb',
    name='њDSB S-Tog 2 "De Røde S-Tog"',
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
    power=800,
    introduction_date=date(1993, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=70,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=229, #130 seats, 0 collapsible seats, ca 100 standing = 230
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers with bike space',
        'Class': 'MM-FS',
    }),
).add_articulated_part(
    id='d_e_stog22_5_dsb',
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

d_e_stog2_6_dsb = Train(
    id='d_e_stog2_6_dsb',
    name='њDSB S-Tog 2 "De Røde S-Tog"',
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
    power=1600,
    introduction_date=date(1993, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=142,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=200, #260 seats, 0 collapsible seats, ca 200 standing = 460
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers with bike space',
        'Class': 'MM-FU-MU-FS',
    }),
).add_articulated_part(
    id='d_e_stog22_6_dsb',
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
    id='d_e_stog23_6_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=59,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog24_6_dsb',
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

#DSB 1993 white and red

d_e_stog2_7_dsb = Train(
    id='d_e_stog2_7_dsb',
    name='њDSB S-Tog 2',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(100),
    power=800,
    introduction_date=date(1993, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=70,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=229, #130 seats, 0 collapsible seats, ca 100 standing = 230
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Trivia': 'One painted in this livery',
        'Class': 'MM-FS',
    }),
).add_articulated_part(
    id='d_e_stog22_7_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY1'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_stog2_8_dsb = Train(
    id='d_e_stog2_8_dsb',
    name='њDSB S-Tog 2',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(100),
    power=1600,
    introduction_date=date(1993, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=142,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=200, #260 seats, 0 collapsible seats, ca 200 standing = 460
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Trivia': 'One painted in this livery',
        'Class': 'MM-FU-MU-FS',
    }),
).add_articulated_part(
    id='d_e_stog22_8_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY1'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog23_8_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY1'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=59,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog24_8_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY1'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
