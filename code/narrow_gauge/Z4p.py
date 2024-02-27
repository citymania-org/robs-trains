import grf, lib

from datetime import date

from common import Train, Livery, p_gauge, colours, make_psd_cc_liveries

COMMON_Z4p_PROPS = dict(
    length=3,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=p_gauge, 
    max_speed=Train.kmhish(40),
    power=160,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25, #balance later
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Info': 'The most common diesel locomotive on narrow gauge lines. The first ones were acquired by SRJ, with other private companies and SJ following suit',
    }),
)

s_d_Z4p_1_srj = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_1_srj',
    name='SRJ Z4p',
    liveries={
        'Default': Livery('1947_SE_Z4p_1_1947.png', cc_replace=colours["REDBROWN"]),
        '2CC': Livery('1947_SE_Z4p_1_1947.png', auto_cc=lib.CC_DEFAULT),
    #    'SL Grey and yellow': '1947_SE_Z4p_4_xxxx.png',
    #    'SL Red': '1947_SE_Z4p_5_xxxx.png',
    },
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1947, 1, 1),
)

s_d_Z4p_1_srj_2 = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_1_srj_2',
    name='SRJ Z4p',
    liveries=make_psd_cc_liveries(
        'pp/Z4p.psd', shading='base', paint='1_srj', overlay='light', cc_replace=colours["REDBROWN"], cc2_replace=colours["REDBROWN"],
    ),
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1947, 1, 1),
)

s_d_Z4p_2_nklj = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_2_NKLJ',
    name='NKlJ Z4p',
    liveries={
        'Default': Livery('1947_SE_Z4p_2_xxxx.png', cc_replace=colours["MAROON"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1947_SE_Z4p_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
    },
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1947, 1, 1),
)


s_d_Z4p_3_donj = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_3_DONJ',
    name='DONJ Z4p',
    liveries={
        'Default': Livery('1947_SE_Z4p_3_xxxx.png', cc_replace=colours["ORANGE"], cc2_replace=colours["DTURQUOISE"]),
        '2CC': Livery('1947_SE_Z4p_3_xxxx.png', auto_cc=lib.CC_DEFAULT),
    },
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1947, 1, 1),
)