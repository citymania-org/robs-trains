import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, extra_narrow_gauge, extra_narrow_gauge_15kv

#This .py-file is intended for the vehicles of Thamshavnsbanen

#Electric Locomotives

no_e_st1to3_1 = Train(
    id='no_e_st1to3_1',
    name='њS&T 1-3', 
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["BLUE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='norway',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(40),
    power=160,
    introduction_date=date(1908, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=20,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1000mm',
        'Use': 'Universal',
    }),
)

no_e_st7to8_1 = Train(
    id='no_e_st7to8_1',
    name='њS&T 7-8', 
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["BLUE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='norway',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(50),
    power=400,
    introduction_date=date(1918, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=44,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1000mm',
        'Use': 'Freight',
    }),
)

no_e_st5to6_1= Train(
    id='no_e_st5to6_1',
    name='њS&T 5-6', 
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('3a',),
        paint=('3b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["BLUE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='norway',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(60),
    power=240,
    introduction_date=date(1950, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=22,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1000mm',
        'Use': 'Freight',
    }),
)

no_e_st1_1 = Train(
    id='no_e_st1_1',
    name='њS&T 1 "Sommerloket"', 
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["BLUE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='norway',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(60),
    power=480,
    introduction_date=date(1950, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1000mm',
        'Use': 'Freight',
        'Trivia': 'Was nicknamed "sommerloket" (the summer loco) due to its terrible performance during winters',
    }),
)

no_e_st1_2 = Train(
    id='no_e_st1_2',
    name='њS&T 1 "Sommerloket"', 
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["MBC"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='norway',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(60),
    power=480,
    introduction_date=date(1960, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1000mm',
        'Use': 'Freight',
        'Trivia': 'Was nicknamed "sommerloket" (the summer loco) due to its terrible performance during winters',
    }),
)

#EMU

no_e_st4_1 = Train(
    id='no_e_st4_1',
    name='њS&T 4 "Kongevognen"',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["REDBROWN"],
        cc2_replace=colours["CREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='norway',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(50),
    power=40,
    introduction_date=date(1908, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=23,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=19,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1000mm',
        'Use': 'Local passengers',
    }),
) 

no_e_st5to6_2 = Train(
    id='no_e_st5to6_2',
    name='њS&T 5-6',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='norway',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(50),
    power=300,
    introduction_date=date(1910, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=54,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1000mm',
        'Use': 'Local passengers',
        'Trivia': 'Both units were destroyed by sabotage during WWII'
    }),
) 

#Carriages

no_p_ACo_1 = Train(
    id='no_p_ACo_1',
    name='њS&T ACo',
    length=8,
    liveries=make_psd_cc_liveries(
            'pp/Template.psd',
            shading=('8a',),
            paint=('8b',),
            cc_replace=colours["BROWN"],
            cc2_replace=colours["BROWN"]
        ),
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    country='norway',
    company='na',
    power_type='na',
    max_speed=Train.kmhish(60),
    power=0,
    introduction_date=date(1908, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(16)),
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=52,
    loading_speed=10,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Guage': '1000mm',
        'Use': 'Local passengers',
    }),
)
