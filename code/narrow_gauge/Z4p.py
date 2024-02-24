import grf, lib

from datetime import date

from common import Train, Livery, p_gauge, modern_diesel_sound, colours

s_d_Z4p_1_srj = Train(
    id='s_d_Z4p_1_srj',
    name='SRJ Z4p',
    length=3,
    liveries={
        'Default': Livery('1947_SE_Z4p_1_1947.png', cc_replace=colours["REDBROWN"]),
        '2CC': Livery('1947_SE_Z4p_1_1947.png', auto_cc=lib.CC_DEFAULT),
    #    'SL Grey and yellow': '1947_SE_Z4p_4_xxxx.png',
    #    'SL Red': '1947_SE_Z4p_5_xxxx.png',
    },
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='s_p_Co_1',
    engine_class=Train.EngineClass.DIESEL, 
    sound_effects=modern_diesel_sound,
    track_type=p_gauge,
    max_speed=Train.kmhish(40),
    power=160,
    introduction_date=date(1947, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=1,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS, # can't be NONE
    additional_text=grf.fake_vehicle_info({
        'Info': 'The most common diesel locomotive on narrow gauge lines. The first ones were acquired by SRJ, with other private companies and SJ following suit',
    }),
    callbacks={'properties': {'cargo_capacity': 0},}
)

s_d_Z4p_2_nklj = Train(
    id='s_d_Z4p_2_NKLJ',
    name='NKlJ Z4p',
    length=3,
    liveries={
        'Default': Livery('1947_SE_Z4p_2_xxxx.png', cc_replace=colours["MAROON"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1947_SE_Z4p_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='s_p_Co_1',
    engine_class=Train.EngineClass.DIESEL, 
    sound_effects=modern_diesel_sound,
    track_type=p_gauge,
    max_speed=Train.kmhish(40),
    power=160,
    introduction_date=date(1947, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=1,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS, # can't be NONE
    additional_text=grf.fake_vehicle_info({
        'Info': 'The most common diesel locomotive on narrow gauge lines. The first ones were acquired by SRJ, with other private companies and SJ following suit',
    }),
    callbacks={'properties': {'cargo_capacity': 0},}
)


s_d_Z4p_3_donj = Train(
    id='s_d_Z4p_3_DONJ',
    name='DONJ Z4p',
    length=3,
    liveries={
        'Default': Livery('1947_SE_Z4p_3_xxxx.png', cc_replace=colours["ORANGE"], cc2_replace=colours["DTURQUOISE"]),
        '2CC': Livery('1947_SE_Z4p_3_xxxx.png', auto_cc=lib.CC_DEFAULT),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='s_p_Co_1',
    engine_class=Train.EngineClass.DIESEL, 
    sound_effects=modern_diesel_sound,
    track_type=p_gauge,
    max_speed=Train.kmhish(40),
    power=160,
    introduction_date=date(1947, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=1,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS, # can't be NONE
    additional_text=grf.fake_vehicle_info({
        'Info': 'The most common diesel locomotive on narrow gauge lines. The first ones were acquired by SRJ, with other private companies and SJ following suit',
    }),
    callbacks={'properties': {'cargo_capacity': 0},}
)