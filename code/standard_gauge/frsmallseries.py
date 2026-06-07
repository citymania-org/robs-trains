import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_65000_PROPS = dict(
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
    visual_effect=(Train.VisualEffect.DIESEL, 6),
    max_speed=Train.kmhish(130),
    power=1849,
    weight=112,
)

fr_d_65000_1 = Train(
    **COMMON_65000_PROPS,
    id='fr_d_65000_1',
    name='SNCF 060 DB',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["BLUE"]
    ),
    country='france',
    company='na',
    introduction_date=date(1956, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as CC 65000',
    }),
)

fr_d_65000_2 = Train(
    **COMMON_65000_PROPS,
    id='fr_d_65000_2',
    name='SNCF CC 65000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    introduction_date=date(1962, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

COMMON_69000_PROPS = dict(
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
    visual_effect=(Train.VisualEffect.DIESEL, 6),
    max_speed=Train.kmhish(140),
    power=4133,
    weight=84,
)

fr_d_69000_1 = Train(
    **COMMON_69000_PROPS,
    id='fr_d_69000_1',
    name='SNCF BB 69000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    introduction_date=date(1964, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two of this class built',
    }),
)

fr_d_69000_2 = Train(
    **COMMON_69000_PROPS,
    id='fr_d_69000_2',
    name='SNCF BB 69000', #new cabs with different windows
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    introduction_date=date(1964, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two of this class built',
    }),
)

COMMON_70000_PROPS = dict(
    length=10,
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
    visual_effect=(Train.VisualEffect.DIESEL, 6),
    max_speed=Train.kmhish(140),
    power=4802,
    weight=117,
)

fr_d_70000_1 = Train(
    **COMMON_70000_PROPS,
    id='fr_d_70000_1',
    name='SNCF CC 70000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two of this class built',
    }),
)
