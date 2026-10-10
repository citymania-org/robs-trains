import grf, lib

from datetime import date

from common import  g, Train, colours, make_psd_cc_liveries, make_psd_cc_liveries_flippable, standard_gauge

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
    country='sweden',
    company='na',
    power_type='diesel',
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
        'Use': 'Express passengers',
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
    country='sweden',
    company='na',
    power_type='diesel',
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
        'Use': 'Express passengers',
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
    country='sweden',
    company='na',
    power_type='diesel',
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
        'Use': 'Restaurant carriage',
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
    country='sweden',
    company='na',
    power_type='diesel',
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
        'Use': 'Restaurant carriage',
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
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
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
    cargo_capacity=10,  #Post: 6t, Resgods: 4t
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.MAIL,
    callbacks={
                'cargo_capacity': Train.Luggage.switch_cargo_capacity(10, g),
            },
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage',
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
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
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
    refittable_cargo_classes=grf.CargoClass.MAIL,
    callbacks={
                    'cargo_capacity': Train.Luggage.switch_cargo_capacity(10, g),
                },
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage',
    }),
)
