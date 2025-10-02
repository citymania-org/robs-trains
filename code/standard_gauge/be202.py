import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_202_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=1750,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=108,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 7),
)

be_d_202_1_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_1_nmbs',
    name='NMBS HLD 202/203', # 1 stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('52/53',),
        paint=('nmbs1',),
        overlay=('bllight'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1955, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 52/53',
    }),
)

be_d_202_2_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_2_nmbs',
    name='NMBS HLD 202/203', # 2 stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('52/53',),
        paint=('cfl1',),
        overlay=('bllight'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1955, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 52/53',
    }),
)

be_d_202_3_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_3_nmbs',
    name='NMBS HLD 52/53', # thick stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('52/53',),
        paint=('nmbs2',),
        overlay=('bllight'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1971, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

be_d_202_4_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_4_nmbs',
    name='њNMBS HLD 52/53', # modern
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1979, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'New cab to improve drivability',
    }),
)

be_d_202_5_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_5_nmbs',
    name='NMBS HLD 204', # 1 stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('nmbs1',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    max_speed=Train.kmhish(140),
    introduction_date=date(1957, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 54',
    }),
)

be_d_202_6_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_6_nmbs',
    name='NMBS HLD 204', # 2 stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('cfl1',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    max_speed=Train.kmhish(140),
    introduction_date=date(1957, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 54',
    }),
)

be_d_202_7_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_7_nmbs',
    name='NMBS HLD 54', # thick stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('nmbs2',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    max_speed=Train.kmhish(140),
    introduction_date=date(1971, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

be_d_202_8_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_8_nmbs',
    name='њNMBS HLD 54', # modern
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1992, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'New cab to improve drivability',
    }),
)
