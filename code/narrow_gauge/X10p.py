import grf, lib

from datetime import date

from common import Train, Livery, p_gauge, p_gauge_dc

s_p_UBp_ii_1 = Train(
    id='s_p_UBp_ii_1',
    name='SL UBp II',
    length=9,
    liveries={
        'SL': Livery('xxxx_SE_X10p_UBp_1_xxxx.png'),
    },
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=p_gauge,
    country='sweden',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='s_p_UBp_ii_1',
    max_speed=Train.kmhish(80),
    power=0,
    introduction_date=date(1988, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(16.6)),
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=80,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Passenger',
        'Trivia': 'The middle part of the new emus were ordered to arive first so that they could be used earlier replacing the oldest rolling stock',
        'Builder': 'ABB railcar',
    }),
)

COMMON_X10p_PROPS = dict(
    length=9,
    country='sweden',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=p_gauge_dc,
    max_speed=Train.kmhish(80),
    power=536,
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(27.7+15.8+16.6)),
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=72,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Passenger emu', 
        'Trivia': 'Technically modular but always used in sets of one railcar with an unpowered trailer and a driving trailer in tow.',
        'Builder': 'ABB railcar',
    }),
)

s_e_X10p_1_sl = Train(
    **COMMON_X10p_PROPS, 
    id='s_e_X10p_1_sl,',
    name='SL X10p',
    liveries={
        'Default': Livery('xxxx_SE_X10p_X10p_1_xxxx.png'),
    },
    purchase_sprite_towed_id='s_e_X10p_1_sl_car2',
    introduction_date=date(1990, 1, 1),
).add_articulated_part(
    id='s_e_X10p_1_sl_car2',
    length=9,
    liveries={
        'Default': Livery('xxxx_SE_X10p_UBp_1_xxxx.png'),
    },
    cargo_capacity=80,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='s_e_X10p_1_sl_car3',
    length=9,
    liveries={
        'Default': Livery('xxxx_SE_X10p_UBxp_1_xxxx.png'),
    },
    cargo_capacity=76,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_X10p_2_sl = Train(
    **COMMON_X10p_PROPS, 
    id='s_e_X10p_2_sl,',
    name='SL X10p mod 2011',
    liveries={
        'Default': Livery('xxxx_SE_X10p_X10p_2_xxxx.png'),
        '2CC': Livery('xxxx_SE_X10p_X10p_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
        'Upptåget (Fictional)': Livery('SE_X10p_X10p_3.png'),
        'Upptåget 2CC': Livery('SE_X10p_X10p_3.png', auto_cc=lib.CC_DEFAULT),
    },
    purchase_sprite_towed_id='s_e_X10p_2_sl_car2',
    introduction_date=date(2011, 1, 1),
).add_articulated_part(
    id='s_e_X10p_2_sl_car2',
    length=9,
    liveries={
        'Default': Livery('xxxx_SE_X10p_UBp_2_xxxx.png'),
        '2CC': Livery('xxxx_SE_X10p_UBp_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
        'Upptåget (Fictional)': Livery('SE_X10p_UBp_3.png'),
        'Upptåget 2CC': Livery('SE_X10p_UBp_3.png', auto_cc=lib.CC_DEFAULT),
    },
    cargo_capacity=80,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='s_e_X10p_2_sl_car3',
    length=9,
    liveries={
        'Default': Livery('xxxx_SE_X10p_UBxp_2_xxxx.png'),
        '2CC': Livery('xxxx_SE_X10p_UBxp_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
        'Upptåget (Fictional)': Livery('SE_X10p_UBxp_3.png'),
        'Upptåget 2CC': Livery('SE_X10p_UBxp_3.png', auto_cc=lib.CC_DEFAULT),
    },
    cargo_capacity=76,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)