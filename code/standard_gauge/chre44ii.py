import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_44_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(140),
    power=6499,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=80,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

ch_e_re44ii_1 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_1',
    name='SBB Re 4/4 II series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1964, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Re 420',
    }),
)

ch_e_re44ii_8 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_8',
    name='SBB Re 4/4 II series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers',
        'Trivia': 'Used on the Swiss Express',
    }),
)

ch_e_re44ii_3 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_3',
    name='SBB Re 4/4 II series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Re 420',
    }),
)

ch_e_re44ii_17 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_17',
    name='BLS Re 420.5',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["LIME"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2004, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44ii_2 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_2',
    name='SBB Re 4/4 II series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1969, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Re 420',
    }),
)

ch_e_re44ii_6 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_6',
    name='SBB Re 4/4 II series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["DCREAM"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1969, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers',
        'Trivia': 'Used on the TEE',
    }),
)

ch_e_re44ii_10 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_10',
    name='MThB Re 4/4 II series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1969, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Re 420',
    }),
)

ch_e_re44ii_4 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_4',
    name='SBB Re 4/4 II series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Re 420',
    }),
)

ch_e_re44ii_11 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_11',
    name='MThB Re 4/4 II series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["CREAM"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1991, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Re 420',
    }),
)

ch_e_re44ii_12 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_12',
    name='RM Re 436', #colani
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44ii_5 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_5',
    name='SBBC Re 420 series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["BLUE"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)

ch_e_re44ii_9 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_9',
    name='SBB Re 420 series 2 "Lion"',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2011, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Used on the Zürich S-Bahn',
    }),
)

ch_e_re44ii_15 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_15',
    name='MBC Re 420 series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2013, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44ii_13 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_13',
    name='WRS Re 430',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["YELLOW"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2017, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44ii_14 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_14',
    name='WRS Re 430',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2019, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44ii_7 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_7',
    name='TR Re 420 series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["DCREAM"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2020, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Charter services',
        'Trivia': 'One given a Rheingold style livery',
    }),
)

ch_e_re44ii_16 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44ii_16',
    name='UTL Re 421',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["GREY3"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2022, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
