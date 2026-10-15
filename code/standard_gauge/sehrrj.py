import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, standard_gauge_1500v

COMMON_HRRJ1_PROPS = dict(
    length=5,
    misc_flags=Train.Flags.USE_2CC,
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(30),
    power=110,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=19,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

se_e_hrrj1to2_1 = Train(
    **COMMON_HRRJ1_PROPS,
    id='se_e_hrrj1to2_1',
    name='њHRRJ 1-2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["YORANGE"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1907, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
        'Trivia': '''Denmark's first electric locomotive''',
    }),
)

COMMON_HRRJ2_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(70),
    power=68,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=19,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

se_e_hrrj1to5_1 = Train(
    **COMMON_HRRJ2_PROPS,
    id='se_e_hrrj1to5_1',
    name='њHRRJ 1-5',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='7a',
        paint='7b',
        cc_replace=colours["SKY"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1906, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

#Trailers

COMMON_HRRJ3_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    max_speed=Train.kmhish(70),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

se_w_hrrj21to22_1 = Train(
    **COMMON_HRRJ3_PROPS,
    id='se_w_hrrj21to22_1',
    name='њHRRJ 21-22',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SKY"],
        cc2_replace=colours["CREAM"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1906, 1, 1),
    cargo_capacity=80,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

COMMON_HRRJ3_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=11,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    max_speed=Train.kmhish(70),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

se_w_hrrj23to24_1 = Train(
    **COMMON_HRRJ3_PROPS,
    id='se_w_hrrj23to23_1',
    name='њHRRJ 23-24',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SKY"],
        cc2_replace=colours["CREAM"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1906, 1, 1),
    cargo_capacity=70,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)