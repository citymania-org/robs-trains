import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_ma_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    max_speed=Train.kmhish(105),
    power=5384,
    weight=105,
)

se_e_ma_1 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_1',
    name='SJ Ma', #https://www.svenska-lok.se/Fotos/MotorSJ/SJ_Ma_962_2019.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    company='na',
    introduction_date=date(1953, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_2 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_2',
    name='TGOJ Ma', #https://www.svenska-lok.se/Fotos/PbaneSJ/TGOJ/TGOJ_Ma_409_1966.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MECONIUM"],
        cc2_replace=colours["YELLOW"]
    ),
    company='na',
    introduction_date=date(1953, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_3 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_3',
    name='TGOJ Ma', #https://www.svenska-lok.se/Fotos/PbaneSJ/TGOJ/TGOJ_Ma_409_1987.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(1968, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_4 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_4',
    name='SJ Ma', #https://www.svenska-lok.se/Fotos/MotorSJ/SJ_Ma_880_1987.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    company='na',
    introduction_date=date(1970, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_5 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_5',
    name='TGOJ Ma', #https://www.svenska-lok.se/Fotos/PbaneSJ/TGOJ/TGOJ_Ma_401_1998.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["APPLE"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    introduction_date=date(1996, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_6 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_6',
    name='BK Ma', #https://www.svenska-lok.se/Fotos/PbaneSJ/BK/BK_Ma_825_1999.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    introduction_date=date(1999, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_7 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_7',
    name='TGOJ Ma', #https://www.svenska-lok.se/Fotos/PbaneSJ/TGOJ/TGOJ_Ma2_966_2001.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["APPLE"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    introduction_date=date(2001, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_8 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_8',
    name='NR Ma', #https://www.svenska-lok.se/Fotos/PbaneSJ/NR/NR_Ma_827_2011.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(2011, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_9 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_9',
    name='BJ Ma', #https://www.svenska-lok.se/Fotos/PbaneSJ/TGOJ/TGOJ_Ma_403_2019.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["ORANGE"]
    ),
    company='na',
    introduction_date=date(2019, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

no_e_ma_1 = Train(
    **COMMON_ma_PROPS,
    id='no_e_ma_1',
    name='GR Ma', #https://www.jarnvag.net/images/bild/lokguide/Ma_404_Oslo2014BGK.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(2005, 1, 1),
    country='norway',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
