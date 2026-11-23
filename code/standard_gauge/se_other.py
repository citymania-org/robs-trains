import grf, lib

from datetime import date

from common import g, Train, Livery, colours, make_psd_cc_liveries, standard_gauge, badges


s_s_N_ii_1_sj = Train(
    id='s_s_N_ii_1_sj',
    name='њSJ N II',
    length=5,
    liveries={
        'Default': Livery('1900_SE_N_II_1.png', cc_replace=colours["GREY10"], cc2_replace=colours["GREY10"]),
        '2CC': Livery('1900_SE_N_II_1.png', auto_cc=lib.CC_DEFAULT),
    },
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.STEAM,
    track_type=standard_gauge,
    max_speed=Train.kmhish(45),
    power=560,
    introduction_date=date(1900, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=55,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['shunting'],
        'power': ['steam'],
        'operator': ['SE/sj'],
        'manufacturer': [],
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

s_s_Sa_sj = Train(
    id='s_s_Sa_sj',
    name='њSJ S',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/1908_SE_Sa.psd',
        shading='Sa',
        paint='SJ',
        overlay=('Lights'),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.STEAM,
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=785,
    introduction_date=date(1908, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=60,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['steam'],
        'operator': ['SE/sj'],
        'manufacturer': [],
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

s_w_Gblssy_2_gc = Train(
    id='s_w_Gblssy_2_gc',
    name='љњGC Gblss-y',
    length=7,
    liveries={
        'Default': Livery('2000_SE_Gblssy_2_2000.png'),
        '2CC': Livery('2000_SE_Gblssy_2_2000.png', mask='2000_SE_Gblssy_2_2000_MASK.png'),
    },
    misc_flags=Train.Flags.USE_2CC + Train.Flags.USE_CARGO_MULT,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(2000, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=17,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.MAIL,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['mail',],
        'power': [],
        'operator': ['SE/posten', 'SE/gc'],
        'manufacturer': [],
    }),
    callbacks={
        'cargo_capacity': Train.sw_capacity_calculaiton(22.4, g)
    }
)

s_w_Hbis_sj = Train(
    id='s_w_Hbis_sj',
    name='љњSJ Hbis',
    length=7,
    liveries={
        'Default': Livery('1972_SE_Hbis_1972.png', cc_replace=colours["REDBROWN"], cc2_replace=colours["REDBROWN"]),
        '2CC': Livery('1972_SE_Hbis_1972.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1972_SE_Hbis_1972.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC + Train.Flags.USE_CARGO_MULT,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=17,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=1, 
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PIECE_GOODS + grf.CargoClass.EXPRESS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE', 'europe'],
        'role': ['freight',],
        'power': [],
        'operator': [],
        'manufacturer': [],
    }),
    callbacks={
        'cargo_capacity': Train.sw_capacity_calculaiton(25, g)
    }
)