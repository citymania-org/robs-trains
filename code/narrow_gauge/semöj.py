import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, extra_narrow_gauge, extra_narrow_gauge_15kv, badges, g

#This .py-file is intended for MÖJ (Mellersta Östergötlands Järnvägar) vehicles and related

#Motor Locomotives

s_d_Dx1_1_möj = Train(
    id='s_d_Dx1_1_möj',
    name='њMÖJ Dx 1', 
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    max_speed=Train.kmhish(40),
    power=75,
    introduction_date=date(1922, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=18,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger'],
        'power': ['diesel'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

s_d_Dx2_1_möj = Train(
    id='s_d_Dx2_1_möj',
    name='њMÖJ Dx 2', 
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    max_speed=Train.kmhish(30),
    power=120,
    introduction_date=date(1922, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=28,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
        'Trivia': 'Two were built for MÖJ but for unknown reasons the second one was rebuilt for metre-gauge and sent to work in Tunisia'
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger'],
        'power': ['diesel'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

#Electric Locomotives

COMMON_MÖJ1_PROPS = dict(
    length=5,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(40),
    power=140,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=24,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

s_e_MÖJ_2to5_1_möj = Train( #Add reversing graphics
    **COMMON_MÖJ1_PROPS,
    id='s_e_MÖJ_2to5_1_möj',
    name='њMÖJ 2-5 (early)',
    liveries=make_psd_cc_liveries(
        'pp/MÖJ_2to5.psd',
        shading='MÖJ 2-5',
        paint=['möj', 'Wood'],
        overlay=('möjlights'),
        r_overlay=('möjlightsr'),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    introduction_date=date(1915, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

COMMON_MÖJ2_PROPS = dict(
    length=5,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(70),
    power=280,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=24,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

s_e_MÖJ_2to5_2_möj = Train(
    **COMMON_MÖJ2_PROPS,
    id='s_e_MÖJ_2to5_2_möj',
    name='њMÖJ 2-5',
    liveries=make_psd_cc_liveries(
        'pp/MÖJ_2to5.psd',
        shading=['MÖJ 2-5', 'Wood', 'möj1936'],
        paint='möj',
        overlay=('möjlights'),
        r_overlay=('möjlightsr'),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    introduction_date=date(1936, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

#DMU

s_d_X1_1_vb = Train(
    id='s_d_X1_1_vb',
    name='њVB X1', 
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    max_speed=Train.kmhish(60),
    power=75,
    introduction_date=date(1916, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=27,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=36,  #Resgodsutrymme
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
        'Trivia': 'In the early 1940s it was rebuilt into a regular carriage'
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'power': ['diesel'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

s_d_X2_1_vb = Train(
    id='s_d_X2_1_vb',
    name='њVB X2', 
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    max_speed=Train.kmhish(60),
    power=120,
    introduction_date=date(1916, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=27,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=5,  #Resgods: 5t (irl stats)
    refittable_cargo_classes=(grf.CargoClass.MAIL),
    non_refittable_cargo_classes=(grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
    cargo_allow_refit=[g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
    loading_speed=20,
    callbacks={'properties': {
            'cargo_capacity': Train.Luggage.sw_capacity_calculaiton_lug(5, g),
    },},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': ['luggage'],
        'power': ['diesel'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

s_d_X3_1_vb = Train(
    id='s_d_X3_1_vb',
    name='њVB X3', 
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    max_speed=Train.kmhish(60),
    power=120,
    introduction_date=date(1922, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=27,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    cargo_capacity=2,  #Resgods: 3t, mail: 2t (irl stats)
    refittable_cargo_classes=(grf.CargoClass.MAIL),
    non_refittable_cargo_classes=(grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
    cargo_allow_refit=[g.get_cargo_id("MAIL")],
    callbacks={'properties': {
            'cargo_capacity': Train.Luggage.sw_capacity_calculaiton_lug(2, g),
    },},
    #mid_stats={
    #    'cargo_capacity': 3,
    #    'refittable_cargo_classes': (grf.CargoClass.MAIL),
    #    'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
    #    'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
    #    'loading_speed': 20,
    #    'callbacks': {
    #        'cargo_capacity': Train.Luggage.sw_capacity_calculaiton_lug(3, g),
    #    },
    #},
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger', 'mail'],
        'amenity': ['luggage'],
        'power': ['diesel'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

s_d_X1_1_vsbj = Train(
    id='s_d_X1_1_vsbj',
    name='ЉњVSBJ X1', 
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    max_speed=Train.kmhish(40), #Top speed: 65 km/h
    power=188,  #Љ - Power needs to be researched/approximated
    introduction_date=date(1916, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=27,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=38,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
        'Trivia': 'In 1944 it was rebuilt into a regular carriage'
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': [],
        'power': ['diesel'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

s_d_MÖJ4_1_möj = Train(
    id='s_d_MÖJ4_1_möj',
    name='ЉњMÖJ 4', 
    length=6,  #Љ - Length needs to be researched
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SEBROWN"],    #Љ - Colour needs to be researched
        cc2_replace=colours["SEBROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    max_speed=Train.kmhish(60), #Top speed: 75 km/h
    power=188,
    introduction_date=date(1936, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=27,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=40,  #Љ - Estimate
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
        'Trivia': 'Notoriusly unreliable'
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': [],
        'power': ['diesel'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

#EMU

s_e_MÖJ1_1_möj = Train(
    id='s_e_MÖJ1_1_möj',
    name='њMÖJ 1 "Ankan"',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(35),
    power=34,
    introduction_date=date(1907, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=15,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=22,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
        'Trivia': 'It initially had two axles but a third unpowered axle was quickly added to reduce the axle load'
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger', 'freight'],
        'amenity': [],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

s_e_MÖJ6_1_möj = Train(
    id='s_e_MÖJ6_1_möj',
    name='њMÖJ 6',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(70),
    power=280,
    introduction_date=date(1936, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=50,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': [],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

se_e_Yo3a_1 = Train(
    id='se_e_Yo3a_1',
    name='њMÖJ Yo3a',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["BLUE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(80),
    power=150,
    introduction_date=date(1949, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=13,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=46,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': [],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

se_e_Yoa1p_1 = Train(
    id='se_e_Yoa1p_1',
    name='њSJ Yoa1p',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["DCREAM"],
        cc2_replace=colours["DGREEN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=extra_narrow_gauge_15kv,
    max_speed=Train.kmhish(80),
    power=150,
    introduction_date=date(1952, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=13,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=46,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Gauge': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': [],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)

#Carriages

se_p_BCo_2 = Train(
    id='se_p_BCo_2',
    name='ЉњMÖJ BCo',
    length=7,
    liveries=make_psd_cc_liveries(
            'pp/7TemplateNG.psd',
            shading=('1',),
            paint=('2',),
            cc_replace=colours["SEBROWN"],
            cc2_replace=colours["SEBROWN"]
        ),
    engine_class=Train.EngineClass.DIESEL,
    track_type=extra_narrow_gauge,
    max_speed=Train.kmhish(70),
    power=0,
    introduction_date=date(1897, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(17)),
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=36,
    loading_speed=10,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Guage': '891mm',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': [],
        'power': [],
        'operator': ['SE/moej'],
        'manufacturer': [],
    }),
)
