import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

#Contains the DMUs of SNJ and their previous iterations. Some vehicles do not have a separate entry for SNJ, since their SJ livery was pretty much identical. SNJ is the common denonimator for these units and are therefore bunched together in this .py file.

#SNJ DMU 1-2
se_d_SNJ1to2_1 = Train(
    id='se_d_SNJ1to2_1',
    name='њSNJ 1-2', 
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=120,
    introduction_date=date(1928, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=23,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=80,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': '3rd class',
    }),
)

#SNJ DMU 3
se_d_SNJ3_1 = Train(
    id='se_d_SNJ3_1',
    name='њSNJ 3', 
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=200,
    introduction_date=date(1931, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=23,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=80,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 2,    #Increase to 3?
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)





#SNJ 4 (LyJ 10)

se_d_LyJ10_1 = Train(
    id='se_d_LyJ10_1',
    name='њLyJ 10', 
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=200,
    introduction_date=date(1932, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 1,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

#SNJ 5 (VBHJ 4)

se_d_MCo_2 = Train(
    id='se_d_MCo_2',
    name='њVBHJ MCo 4', 
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["DCREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=120,
    introduction_date=date(1928, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=23,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=65,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

#SNJ 6 (SJ Xod4 5)

se_d_Xod4_1 = Train(
    id='se_d_Xod4_1',
    name='њSJ Xod4', 
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DCREAM"],
        cc2_replace=colours["DGREEN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=450,
    introduction_date=date(1937, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=23,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=65,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': '3rd class',
    }),
)

#SNJ 8-9 (VBHJ 5-6, SJ Xod4 SEBROWN)

se_d_MCo_3 = Train(
    id='se_d_MCo_3',
    name='њVBHJ MCo 5-6', 
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["DCREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(110),
    power=410,
    introduction_date=date(1938, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=75,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class, Luggage',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

#SNJ 30 (MYJ XCo 300, SJ Xod6/Xo5/XBo5/tjv 626289)

se_d_XCo_1 = Train(
    id='se_d_XCo_1',
    name='њMYJ XCo', 
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["DCREAM"]   #Antingen gräddvit eller ljusgul
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=480,
    introduction_date=date(1935, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 1,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

se_d_Xod6_1 = Train(
    id='se_d_Xod6_1',
    name='њSJ Xod6', 
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=480,
    introduction_date=date(1941, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 1,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)