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
)

s_d_Z4p_1_srj = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_1_srj',
    name='SRJ Z4p',
    liveries=make_psd_cc_liveries(
        'pp/Z4p.psd', shading='base', paint='1_srj', overlay='light', cc_replace=colours["REDBROWN"], cc2_replace=colours["REDBROWN"],
    ),
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1947, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SRJ, GJ, SJ, SL, and others (probably)',
        'Use': 'Universal',
        'Builder': 'Kalmar Verkstad'
    }),
)

s_d_Z4p_2 = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_2_',
    name='Munkfors Bruk Ms 3',
    liveries=make_psd_cc_liveries(
        'pp/Z4p.psd', shading='base', paint='2', overlay='light', cc_replace=colours["DGREEN"], cc2_replace=colours["DGREEN"],
    ),
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1948, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'Munkfors Bruk',
        'Use': 'Shunting',
        'Builder': 'Kalmar Verkstad'
    }),
)

s_d_Z4p_3_nklj = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_3_NKLJ',
    name='NKlJ Z4p',
    liveries=make_psd_cc_liveries(
        'pp/Z4p.psd', shading='base', paint='3_nklj', overlay='light',  cc_replace=colours["MAROON"], cc2_replace=colours["CREAM"],
    ),
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'NKlJ',
        'Use': 'Universal',
        'Builder': 'Kalmar Verkstad'
    }),
)

s_d_Z4p_4 = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_4',
    name='Böksholms Bruk Z4p',
    liveries=make_psd_cc_liveries(
        'pp/Z4p.psd', shading='base', paint='4', overlay='light', cc_replace=colours["ORANGE"], cc2_replace=colours["DGREEN"],
    ),
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'Böksholms Bruk',
        'Use': 'Shunting',
        'Builder': 'Kalmar Verkstad'
    }),
)

s_d_Z4p_5_donj = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_5_DONJ',
    name='DONJ Z4p',
    liveries=make_psd_cc_liveries(
        'pp/Z4p.psd', shading='base', paint='5_donj', overlay='light', cc_replace=colours["ORANGE"], cc2_replace=colours["DTURQUOISE"],
    ),
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1966, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'DONJ',
        'Use': 'Universal',
        'Builder': 'Kalmar Verkstad'
    }),
)

s_d_Z4p_6_sl = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_6_sl',
    name='SL Z4p',
    liveries=make_psd_cc_liveries(
        'pp/Z4p.psd', shading='base', paint='6_sl', overlay='light', cc_replace=colours["YELLOW"], cc2_replace=colours["GREY3"],
    ),
    #    'SL Grey and yellow': '1947_SE_Z4p_4_xxxx.png',
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(1991, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Universal',
        'Builder': 'Kalmar Verkstad'
    }),
)

s_d_Z4p_7_sl = Train(
    **COMMON_Z4p_PROPS,
    id='s_d_Z4p_7_sl',
    name='SL Z4p',
    liveries=make_psd_cc_liveries(
        'pp/Z4p.psd', shading='base', paint='7_sl', overlay='light', cc_replace=colours["RED"], cc2_replace=colours["RED"],
    ),
    #    'SL Red': '1947_SE_Z4p_5_xxxx.png',
    country='sweden',
    company='na',
    purchase_sprite_towed_id='s_p_Co_1',
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Universal',
        'Builder': 'Kalmar Verkstad'
    }),
)
