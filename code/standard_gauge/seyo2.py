import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, badges

COMMON_Yo2_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=220,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=26,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=55,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_d_Yo2_1_MSJ = Train(
    id='s_d_Yo2_1_MSJ',
    **COMMON_Yo2_PROPS,
    name='њMSJ 11-12/TRJ Yho',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["CREAM"]
    ),
    introduction_date=date(1938, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'power': ['diesel'],
        'operator': ['SE/msj'],
        'manufacturer': [],
    }),
)

s_d_Yo2_2_BJ = Train(
    id='s_d_Yo2_2_BJ',
    **COMMON_Yo2_PROPS,
    name='њBJ Yo6',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["CREAM"]
    ),
    introduction_date=date(1938, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'power': ['diesel'],
        'operator': ['SE/bj'],
        'manufacturer': [],
    }),
)

s_d_Yo2_3_SJ = Train(
    id='s_d_Yo2_3_SJ',
    **COMMON_Yo2_PROPS,
    name='њSJ Yo2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(1943, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'power': ['diesel'],
        'operator': ['SE/bj'],
        'manufacturer': [],
    }),
)

# TrailerS

s_p_YCDFo_1_TRJ = Train(
    id='s_p_YCDFo_1_TRJ',
    name='ЉњTRJ YCDFo',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["CREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(70),
    power=0,
    introduction_date=date(1938, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=55,  #Љ - Post: 1t, Resgods: 2t
    cost_factor=18,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger', 'luggage'],
        'power': [],
        'operator': ['SE/trj'],
        'manufacturer': [],
    }),
)

s_p_UBFo9_1_SJ = Train(
    id='s_p_UBFo9_1_SJ',
    name='ЉњSJ UBFo9',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(110),
    power=0,
    introduction_date=date(1959, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=55,  #Љ - Resgods: 2t
    cost_factor=18,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['SE/sj'],
        'manufacturer': [],
    }),
)