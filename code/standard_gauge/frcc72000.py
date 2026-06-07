import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_72000_PROPS = dict(
    length=9,
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
    max_speed=Train.kmhish(160),
    power=3603,
    weight=114,
)

fr_d_72000_1 = Train(
    **COMMON_72000_PROPS,
    id='fr_d_72000_1',
    name='SNCF CC 72000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    introduction_date=date(1967, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_72000_2 = Train(
    **COMMON_72000_PROPS,
    id='fr_d_72000_2',
    name='SNCF CC 72000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_72000_3 = Train(
    **COMMON_72000_PROPS,
    id='fr_d_72000_3',
    name='SNCF CC 72000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
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

fr_d_72000_4 = Train(
    **COMMON_72000_PROPS,
    id='fr_d_72000_4',
    name='SNCF CC 72000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
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

fr_d_72000_5 = Train(
    **COMMON_72000_PROPS,
    id='fr_d_72000_5',
    name='SNCF CC 72000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
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

fr_d_72000_6 = Train(
    **COMMON_72000_PROPS,
    id='fr_d_72000_6',
    name='SNCF CC 72000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
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
