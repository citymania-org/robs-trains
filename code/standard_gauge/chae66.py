import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_66_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(125),
    power=5846,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=120,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

ch_e_ae66_1 = Train(
    **COMMON_66_PROPS,
    id='ch_e_ae66_1',
    name='SBB Ae 6/6', #strip
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Ae 610',
    }),
)

ch_e_ae66_3 = Train(
    **COMMON_66_PROPS,
    id='ch_e_ae66_3',
    name='SBB Ae 6/6', #strip
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Ae 610',
    }),
)

ch_e_ae66_2 = Train(
    **COMMON_66_PROPS,
    id='ch_e_ae66_2',
    name='SBB Ae 6/6',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1958, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Ae 610',
    }),
)

ch_e_ae66_4 = Train(
    **COMMON_66_PROPS,
    id='ch_e_ae66_4',
    name='SBB Ae 6/6',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as Ae 610',
    }),
)

ch_e_ae66_5 = Train(
    **COMMON_66_PROPS,
    id='ch_e_ae66_5',
    name='SBB Cargo Ae 610',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
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
