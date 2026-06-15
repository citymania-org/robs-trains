import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_compl_PROPS = dict(
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    max_speed=Train.kmhish(100),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_compl_1 = Train(
    **COMMON_compl_PROPS,
    id='dk_p_compl_1',
    name='SJS Ac II',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=7,
    cargo_capacity=38,
    weight=27,
    country='denmark',
    company='na',
    introduction_date=date(1892, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Use': '1st & 2nd class',
        'Trivia': 'Later classed as DSB AA I',
    }),
)

dk_p_compl_2 = Train(
    **COMMON_compl_PROPS,
    id='dk_p_compl_2',
    name='DSB AA II',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=7,
    cargo_capacity=38,
    weight=25,
    country='denmark',
    company='na',
    introduction_date=date(1894, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Use': '1st & 2nd class',
    }),
)

dk_p_compl_3 = Train(
    **COMMON_compl_PROPS,
    id='dk_p_compl_3',
    name='JFJ MD',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=8,
    cargo_capacity=80,
    weight=21,
    country='denmark',
    company='na',
    introduction_date=date(1891, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Use': '1st, 2nd & 3rd class',
        'Trivia': 'Later classed as DSB BA',
    }),
)

dk_p_compl_4 = Train(
    **COMMON_compl_PROPS,
    id='dk_p_compl_4',
    name='DSB BN',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=7,
    cargo_capacity=56,
    weight=25,
    country='denmark',
    company='na',
    introduction_date=date(1897, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Use': '2nd & 3rd class',
    }),
)

dk_p_compl_5 = Train(
    **COMMON_compl_PROPS,
    id='dk_p_compl_5',
    name='DSB CK I',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=8,
    cargo_capacity=86,
    weight=25,
    country='denmark',
    company='na',
    introduction_date=date(1894, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Use': '3rd class',
    }),
)
