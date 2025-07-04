import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

be_d_201_1_nmbs = Train(
    id='be_d_201_1_nmbs',
    name='NMBS HLD 201/HLD 59',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs1',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='belgium',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=1717,
    introduction_date=date(1954, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=87,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

be_d_201_2_nmbs = Train(
    id='be_d_201_2_nmbs',
    name='NMBS HLD 201/HLD 59',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs2',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='belgium',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=1717,
    introduction_date=date(1954, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=87,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

be_d_201_3_nmbs = Train(
    id='be_d_201_3_nmbs',
    name='NMBS HLD 201/HLD 59',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs3',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='belgium',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=1717,
    introduction_date=date(1954, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=87,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

be_d_201_4_nmbs = Train(
    id='be_d_201_4_nmbs',
    name='NMBS HLD 201/HLD 59',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs4',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='belgium',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=1717,
    introduction_date=date(1954, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=87,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

be_d_201_5_nmbs = Train(
    id='be_d_201_5_nmbs',
    name='NMBS HLD 201/HLD 59',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs5',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='belgium',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=1717,
    introduction_date=date(1954, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=87,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)
