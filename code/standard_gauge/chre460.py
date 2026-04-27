import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_44_PROPS = dict(
    length=9,
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
)

ch_e_re460_1 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re460_1',
    name='SBB Re 460',
    liveries=make_psd_cc_liveries(
        'pp/chre460.psd',
        shading=('460',),
        paint=('sbb1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    max_speed=Train.kmhish(200),
    power=8294,
    weight=84,
    introduction_date=date(1991, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re460_4 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re460_4',
    name='SBB Re 460',
    liveries=make_psd_cc_liveries(
        'pp/chre460.psd',
        shading=('460',),
        paint=('sbb2',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    max_speed=Train.kmhish(200),
    power=8294,
    weight=84,
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive given the "New Look" livery',
    }),
)

ch_e_re460_5 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re460_5',
    name='SBB Re 460',
    liveries=make_psd_cc_liveries(
        'pp/chre460.psd',
        shading=('460',),
        paint=('sbb3',),
        overlay=('light'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    max_speed=Train.kmhish(200),
    power=8294,
    weight=84,
    introduction_date=date(2014, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive given the "EasyJet" livery',
    }),
)

ch_e_re460_2 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re460_2',
    name='BLS Re 465',
    liveries=make_psd_cc_liveries(
        'pp/chre460.psd',
        shading=('460',),
        paint=('bls1',),
        overlay=('light'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["CREAM"]
    ),
    country='switzerland',
    company='na',
    max_speed=Train.kmhish(160),
    power=8702,
    weight=84,
    introduction_date=date(1994, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re460_3 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re460_3',
    name='BLS Re 465',
    liveries=make_psd_cc_liveries(
        'pp/chre460.psd',
        shading=('460',),
        paint=('bls2',),
        overlay=('light'),
        cc_replace=colours["LIME"],
        cc2_replace=colours["DBLUE"]
    ),
    country='switzerland',
    company='na',
    max_speed=Train.kmhish(160),
    power=8702,
    weight=84,
    introduction_date=date(2020, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

no_e_el18_1 = Train(
    **COMMON_44_PROPS,
    id='no_e_el18_1',
    name='NSB El 18',
    liveries=make_psd_cc_liveries(
        'pp/chre460.psd',
        shading=('460',),
        paint=('nsb1',),
        overlay=('light'),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY10"]
    ),
    country='norway',
    company='na',
    max_speed=Train.kmhish(200),
    power=7342,
    weight=82,
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

no_e_el18_2 = Train(
    **COMMON_44_PROPS,
    id='no_e_el18_2',
    name='GAN El 18',
    liveries=make_psd_cc_liveries(
        'pp/chre460.psd',
        shading=('460',),
        paint=('gan1',),
        overlay=('light'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    country='norway',
    company='na',
    max_speed=Train.kmhish(200),
    power=7342,
    weight=82,
    introduction_date=date(2019, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
