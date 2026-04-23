import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_ec_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=43,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_p_ec_1 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_1',
    name='SBB Apm 10-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec',),
        paint=('apm1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY9"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1989, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

ch_p_ec_2 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_2',
    name='SBB Apm 10-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec08',),
        paint=('apm3',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2008, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

ch_p_ec_3 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_3',
    name='CIS Apm 10-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec',),
        paint=('apm2',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY9"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2004, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class, for the Cisalpino service',
    }),
)

ch_p_ec_11 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_11',
    name='SBB Apm 10-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec',),
        paint=('apm4',),
        cc_replace=colours["GREY5"],
        cc2_replace=colours["GREY9"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2009, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
        'Trivia': 'Former Cisalpino stock',
    }),
)

ch_p_ec_4 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_4',
    name='SBB Apm 10-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec08',),
        paint=('apm5',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2021, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

ch_p_ec_5 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_5',
    name='SBB Bpm 20-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec',),
        paint=('bpm1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY9"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1990, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=77,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

ch_p_ec_6 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_6',
    name='SBB Bpm 20-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec08',),
        paint=('bpm3',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2008, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=77,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

ch_p_ec_7 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_7',
    name='CIS Bpm 20-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec',),
        paint=('bpm2',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY9"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2004, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=77,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, for the Cisalpino service',
    }),
)

ch_p_ec_12 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_12',
    name='SBB Bpm 20-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec',),
        paint=('bpm4',),
        cc_replace=colours["GREY5"],
        cc2_replace=colours["GREY9"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2009, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=77,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
        'Trivia': 'Former Cisalpino stock',
    }),
)

ch_p_ec_8 = Train(
    **COMMON_ec_PROPS,
    id='ch_p_ec_8',
    name='SBB Bpm 20-90',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec08',),
        paint=('bpm5',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2021, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=77,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

COMMON_pw_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=48,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_p_ec_9 = Train(
    **COMMON_pw_PROPS,
    id='ch_p_ec_9',
    name='SBB Apm 19-90 "Panoramawagen"',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec',),
        paint=('12b',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["GREY9"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1991, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=54,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Panoramic car, 1st class',
    }),
)

ch_p_ec_10 = Train(
    **COMMON_pw_PROPS,
    id='ch_p_ec_10',
    name='SBB Apm 19-90 "Panoramawagen"',
    liveries=make_psd_cc_liveries(
        'pp/chec.psd',
        shading=('ec',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2000, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=54,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Panoramic car, 1st class',
    }),
)
