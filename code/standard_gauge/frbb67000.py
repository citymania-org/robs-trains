import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_67000_PROPS = dict(
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
    max_speed=Train.kmhish(140),
)

fr_d_67000_1 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67000_1',
    name='SNCF BB 67000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    power=1686,
    weight=80,
    introduction_date=date(1963, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67000_2 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67000_2',
    name='SNCF BB 67000', #new cabs with different windows from 67041
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    power=1686,
    weight=80,
    introduction_date=date(1964, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67300_1 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67300_1',
    name='SNCF BB 67300',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    power=2073,
    weight=80,
    introduction_date=date(1967, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67300_2 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67300_2',
    name='SNCF BB 67300 "Isabelle"',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    power=2073,
    weight=80,
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67300_3 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67300_3',
    name='SNCF BB 67300',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    power=2073,
    weight=80,
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67300_4 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67300_4',
    name='SNCF BB 67300',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    power=2073,
    weight=80,
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67400_1 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67400_1',
    name='SNCF BB 67400',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    power=2400,
    weight=83,
    introduction_date=date(1969, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67400_2 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67400_2',
    name='SNCF BB 67400',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    power=2400,
    weight=83,
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67400_3 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67400_3',
    name='SNCF BB 67400',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    power=2400,
    weight=83,
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67400_4 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67400_4',
    name='SNCF BB 67400',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    power=2400,
    weight=83,
    introduction_date=date(2002, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67400_5 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67400_5',
    name='SNCF BB 67400',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    power=2400,
    weight=83,
    introduction_date=date(2002, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)


fr_d_67400_6 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67400_6',
    name='SNCF BB 67400 "Capitole"',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["DBRED"],
        cc2_replace=colours["GREY5"]
    ),
    country='france',
    company='na',
    power=2400,
    weight=83,
    introduction_date=date(2019, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_67400_7 = Train(
    **COMMON_67000_PROPS,
    id='fr_d_67400_7',
    name='SNCF BB 67400 "Isabelle"',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    power=2400,
    weight=83,
    introduction_date=date(2021, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
