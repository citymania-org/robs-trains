import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_e18_PROPS = dict(
    length=8,
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
    country='germany',
    max_speed=Train.kmhish(150),
    power=4133,
    weight=109,
)

de_e_e18_1 = Train(
    **COMMON_e18_PROPS,
    id='de_e_e18_1',
    name='DR E 18',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    company='na',
    introduction_date=date(1935, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 118 & DR 218',
    }),
)

de_e_e18_2 = Train(
    **COMMON_e18_PROPS,
    id='de_e_e18_2',
    name='DR E 18', #red wheels
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    company='na',
    introduction_date=date(1935, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 118 & DR 218',
    }),
)

de_e_e18_3 = Train(
    **COMMON_e18_PROPS,
    id='de_e_e18_3',
    name='DR E 18',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["NAVY"]
    ),
    company='na',
    introduction_date=date(1935, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 118 & DR 218',
    }),
)

de_e_e18_4 = Train(
    **COMMON_e18_PROPS,
    id='de_e_e18_4',
    name='DR E 18', #red wheels
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["NAVY"]
    ),
    company='na',
    introduction_date=date(1935, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 118 & DR 218',
    }),
)

de_e_e18_5 = Train(
    **COMMON_e18_PROPS,
    id='de_e_e18_5',
    name='DB 118',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["DTURQUOISE"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1974, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
)

COMMON_e19_PROPS = dict(
    length=8,
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
    country='germany',
    max_speed=Train.kmhish(180),
    power=5547,
    weight=111,
)

de_e_e19_1 = Train(
    **COMMON_e19_PROPS,
    id='de_e_e19_1',
    name='DR E 19', #bumpers
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["DBRED"],
        cc2_replace=colours["DBRED"]
    ),
    company='na',
    introduction_date=date(1938, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 119',
    }),
)

de_e_e19_2 = Train(
    **COMMON_e19_PROPS,
    id='de_e_e19_2',
    name='DR E 19',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    company='na',
    introduction_date=date(1945, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 119',
    }),
)

de_e_e19_3 = Train(
    **COMMON_e19_PROPS,
    id='de_e_e19_3',
    name='DR E 19',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["NAVY"]
    ),
    company='na',
    introduction_date=date(1945, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 119',
    }),
)
