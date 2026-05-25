import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv_1500v

COMMON_26000_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='dc/25kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_25kv_1500v,
    max_speed=Train.kmhish(200),
    power=7614,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=89,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

fr_e_bb26000_1 = Train(
    **COMMON_26000_PROPS,
    id='fr_e_bb26000_1',
    name='SNCF BB 26000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(1988, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_e_bb26000_2 = Train(
    **COMMON_26000_PROPS,
    id='fr_e_bb26000_2',
    name='SNCF BB 26000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(1993, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_e_bb26000_3 = Train(
    **COMMON_26000_PROPS,
    id='fr_e_bb26000_3',
    name='SNCF BB 26000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_e_bb26000_4 = Train(
    **COMMON_26000_PROPS,
    id='fr_e_bb26000_4',
    name='SNCF BB 26000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_e_bb26000_5 = Train(
    **COMMON_26000_PROPS,
    id='fr_e_bb26000_5',
    name='SNCF BB 26000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(2002, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_e_bb26000_6 = Train(
    **COMMON_26000_PROPS,
    id='fr_e_bb26000_6',
    name='SNCF BB 26000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(2010, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_e_bb26000_7 = Train(
    **COMMON_26000_PROPS,
    id='fr_e_bb26000_7',
    name='SNCF BB 26000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["DBRED"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(2011, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
