import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_201_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    country='belgium',
    max_speed=Train.kmhish(120),
    power=1717,
    weight=87,
)

be_d_201_1_nmbs = Train(
    **COMMON_201_PROPS,
    id='be_d_201_1_nmbs',
    name='NMBS HLD 201', #hirondelles 3
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    company='na',
    introduction_date=date(1958, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 59',
    }),
)

be_d_201_2_nmbs = Train(
    **COMMON_201_PROPS,
    id='be_d_201_2_nmbs',
    name='NMBS HLD 201', #star 1
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    company='na',
    introduction_date=date(1954, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 59',
    }),
)

be_d_201_3_nmbs = Train(
    **COMMON_201_PROPS,
    id='be_d_201_3_nmbs',
    name='NMBS HLD 201', #green 4
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs3',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    company='na',
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 59',
    }),
)

be_d_201_4_nmbs = Train(
    **COMMON_201_PROPS,
    id='be_d_201_4_nmbs',
    name='NMBS HLD 59', #yellow 5
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs4',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    company='na',
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

be_d_201_5_nmbs = Train(
    **COMMON_201_PROPS,
    id='be_d_201_5_nmbs',
    name='NMBS HLD 201', #expo 58 2
    liveries=make_psd_cc_liveries(
        'pp/201.psd',
        shading=('201',),
        paint=('nmbs5',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    company='na',
    introduction_date=date(1958, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 59',
    }),
)
