import grf, lib

from datetime import date

from common import  g, Train, colours, make_psd_cc_liveries, make_psd_cc_liveries_flippable, standard_gauge, badges

se_p_BCo_1 = Train(
    id='se_p_BCo_1',
    name='њOKB BCo', 
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(130),
    power=0,
    introduction_date=date(1926, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(40)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=79,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['SE/okb'],
        'manufacturer': [''],
    }),
)

se_p_BCo6b_1 = Train(
    id='se_p_BCo6b_1',
    name='њSJ BCo6b', 
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(130),
    power=0,
    introduction_date=date(1933, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(40)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=79,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['SE/okb'],
        'manufacturer': [''],
    }),
)

se_p_BCort_1 = Train(
    id='se_p_BCort_1',
    name='њOKB BCort', 
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(130),
    power=0,
    introduction_date=date(1927, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(44)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=40,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'amenity': ['restaurant_car'],
        'power': [],
        'operator': ['SE/okb'],
        'manufacturer': [''],
    }),
)

se_p_Ro2b_1 = Train(
    id='se_p_Ro2b_1',
    name='њSJ Ro2b', 
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(130),
    power=0,
    introduction_date=date(1933, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(44)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=40,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'amenity': ['restaurant_car'],
        'power': [],
        'operator': ['SE/okb'],
        'manufacturer': [''],
    }),
)

se_w_121to122_1 = Train(
    id='se_w_121to122_1',
    name='њOKB 121-122',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC + Train.Flags.USE_CARGO_MULT,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(130),
    power=0,
    introduction_date=date(1927, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(40)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=6,  #Post: 6t, Resgods: 4t
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=(grf.CargoClass.MAIL),
    non_refittable_cargo_classes=(grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
    cargo_allow_refit=[g.get_cargo_id("MAIL")],
    callbacks={
        #'cargo_capacity': Train.Luggage.sw_capacity_calculaiton_lug(6, g),
    },
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            #'cargo_capacity': Train.Luggage.sw_capacity_calculaiton_lug(4, g),
        },
    },
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': ['luggage'],
        'power': [],
        'operator': ['SE/okb'],
        'manufacturer': [''],
    }),
)

se_w_F3_1 = Train(
    id='se_w_F3_1',
    name='њOKB F3',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC + Train.Flags.USE_CARGO_MULT,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1927, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(21)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=10,  #Resgods: 10t
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=(grf.CargoClass.MAIL),
    non_refittable_cargo_classes=(grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
    cargo_allow_refit=[g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
    callbacks={
        #'cargo_capacity': Train.Luggage.sw_capacity_calculaiton_lug(10, g),
    },
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'amenity': ['luggage'],
        'power': [],
        'operator': ['SE/okb'],
        'manufacturer': [''],
    }),
)
