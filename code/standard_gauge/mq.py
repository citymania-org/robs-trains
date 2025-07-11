import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

d_d_ml_1_dsb = Train(
    id='d_d_ml_1_dsb',
    name='DSB ML',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/ml.psd',
        shading=('ml',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(75),
    power=240,
    introduction_date=date(1929, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=44,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

d_d_ml_2_dsb = Train(
    id='d_d_ml_2_dsb',
    name='DSB ML (Büssing)',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/ml.psd',
        shading=('ml',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(75),
    power=300,
    introduction_date=date(1943, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=44,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

d_d_mq_1_dsb = Train(
    id='d_d_mq_1_dsb',
    name='DSB MQ',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mq.psd',
        shading=('mq',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(100),
    power=250,
    introduction_date=date(1932, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=56,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

d_d_mp_1_dsb = Train(
    id='d_d_mp_1_dsb',
    name='DSB MP',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mp.psd',
        shading=('mp',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=440,
    introduction_date=date(1934, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=61,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=64,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers & light freight',
    }),
)

d_d_mo_ii_1_dsb = Train(
    id='d_d_mo_ii_1_dsb',
    name='DSB MO I/II',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mo.psd',
        shading=('mo2',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=500,
    introduction_date=date(1935, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=65,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=52,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers & light freight',
    }),
)

d_d_mo_iv_1_dsb = Train(
    id='d_d_mo_iv_1_dsb',
    name='DSB MO III/IV',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mo.psd',
        shading=('mo4',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=500,
    introduction_date=date(1936, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=65,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=52,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers & light freight',
    }),
)

d_d_mo_v_1_dsb = Train(
    id='d_d_mo_v_1_dsb',
    name='DSB MO V',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mo.psd',
        shading=('mo5',),
        paint=('dsb2',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=500,
    introduction_date=date(1951, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=65,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=37,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers & light freight',
    }),
)
