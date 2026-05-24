import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_701_PROPS = dict(
    length=4,
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
    loading_speed=7,
    max_speed=Train.kmhish(60),
    cargo_capacity=100,
    weight=12,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_701_1 = Train(
    **COMMON_701_PROPS,
    id='dk_p_701_1',
    name='SJS 701',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1868, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '7',
        'Use': 'Local trains, 3rd class',
        'Trivia': 'Later classed as Db, 1 built, nicknamed "Bismarck"',
    }),
)

dk_p_701_2 = Train(
    **COMMON_701_PROPS,
    id='dk_p_701_2',
    name='DSB CF I',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1893, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '7',
        'Use': 'Local trains, 3rd class',
        'Trivia': 'Lost in the crash at Gentofte in 1897',
    }),
)

COMMON_da_PROPS = dict(
    length=5,
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
    loading_speed=7,
    max_speed=Train.kmhish(60),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_701_3 = Train(
    **COMMON_da_PROPS,
    id='dk_p_701_3',
    name='SJS Da',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["REDBROWN"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1870, 1, 1),
    weight=13,
    cargo_capacity=86,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '7',
        'Use': 'Local trains, 2nd & 3rd class',
        'Trivia': 'Later classed as Da I',
    }),
)

dk_p_701_4 = Train(
    **COMMON_da_PROPS,
    id='dk_p_701_4',
    name='DSB BL I',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1893, 1, 1),
    weight=13,
    cargo_capacity=86,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '7',
        'Use': 'Local trains, 2nd & 3rd class',
        'Trivia': 'Later classed as CO I',
    }),
)

dk_p_701_5 = Train(
    **COMMON_da_PROPS,
    id='dk_p_701_5',
    name='SJS Da II',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["REDBROWN"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1877, 1, 1),
    weight=11,
    cargo_capacity=94,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '7',
        'Use': 'Local trains, 2nd & 3rd class',
    }),
)

dk_p_701_6 = Train(
    **COMMON_da_PROPS,
    id='dk_p_701_6',
    name='DSB BL II',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1893, 1, 1),
    weight=12,
    cargo_capacity=94,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '7',
        'Use': 'Local trains, 2nd & 3rd class',
        'Trivia': 'Later classed as CO II',
    }),
)
