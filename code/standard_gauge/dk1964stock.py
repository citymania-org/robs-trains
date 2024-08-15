import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_b_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_p_b_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_b_1_dsb',
    name='DSB B',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('b',),
        paint=('b1_bd1_bn1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_b_1_dsb',
    introduction_date=date(1964, 1, 1),
    weight=37,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_b_i_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_b_i_1_dsb',
    name='DSB B I',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('b',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_b_i_1_dsb',
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=60,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': '2nd class',
    }),
)

d_p_bk_i_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bk_i_1_dsb',
    name='DSB Bk I',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('b',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_b_i_1_dsb',
    introduction_date=date(1973, 1, 1),
    weight=40,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Kiosk car, 2nd class',
    }),
)

d_p_bk_i_2_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bk_i_2_dsb',
    name='DSB Bk I',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('b',),
        paint=('bk2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_b_i_1_dsb',
    introduction_date=date(1983, 1, 1),
    weight=40,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Kiosk car, 2nd class',
    }),
)

d_p_ab_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_ab_1_dsb',
    name='DSB AB',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('ab',),
        paint=('ab1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_ab_1_dsb',
    introduction_date=date(1969, 1, 1),
    weight=37,
    cargo_capacity=64,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

d_p_ab_2_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_ab_2_dsb',
    name='DSB AB',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('ab',),
        paint=('ab2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_ab_2_dsb',
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=64,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

d_p_ab_3_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_ab_3_dsb',
    name='DSB Bab',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('ab',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_ab_3_dsb',
    introduction_date=date(1991, 1, 1),
    weight=37,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_a_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_a_1_dsb',
    name='DSB A',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('a',),
        paint=('a1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_b_1_dsb',
    introduction_date=date(1966, 1, 1),
    weight=37,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': '1st class',
    }),
)

d_p_a_2_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_a_2_dsb',
    name='DSB A',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('a',),
        paint=('a2_an1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_b_i_1_dsb',
    introduction_date=date(1972, 1, 1),
    weight=40,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

d_p_a_3_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_a_3_dsb',
    name='DSB Ba',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('a',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_a_3_dsb',
    introduction_date=date(1991, 1, 1),
    weight=40,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_bd_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bd_1_dsb',
    name='DSB BD',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('bd',),
        paint=('b1_bd1_bn1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_bd_1_dsb',
    introduction_date=date(1968, 1, 1),
    weight=37,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': 'Luggage carriage, 2nd class',
    }),
)

d_p_bd_2_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bd_2_dsb',
    name='DSB BD',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('bd',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_bd_2_dsb',
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=36,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': 'Luggage carriage, 2nd class',
    }),
)

d_p_bn_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_1_dsb',
    name='DSB Bn',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('bn',),
        paint=('b1_bd1_bn1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_bn_1_dsb',
    introduction_date=date(1971, 1, 1),
    weight=40,
    cargo_capacity=80,
    loading_speed=15,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
        'Trivia': 'Bn & variants used on Sjælland until early 2010s by then many were scrapped or sold - Used in Stockholm when SL lacked rolling stock',
    }),
)

d_p_bn_2_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_2_dsb',
    name='DSB Bn',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('bn',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_bn_2_dsb',
    introduction_date=date(1972, 1, 1),
    weight=40,
    cargo_capacity=80,
    loading_speed=15,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
        'Trivia': 'Bn & variants used on Sjælland until early 2010s by then many were scrapped or sold - Used in Stockholm when SL lacked rolling stock',
    }),
)

d_p_bn_3_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_3_dsb',
    name='DSB Bn',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('bn',),
        paint=('bn3',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_bn_3_dsb',
    introduction_date=date(2006, 1, 1),
    weight=40,
    cargo_capacity=80,
    loading_speed=15,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
        'Trivia': 'Bn & variants used on Sjælland until early 2010s by then many were scrapped or sold - Used in Stockholm when SL lacked rolling stock',
    }),
)

d_p_an_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_an_1_dsb',
    name='DSB An',
    liveries=make_psd_cc_liveries(
        'pp/dk1964stock.psd',
        shading=('an',),
        paint=('a2_an1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_an_1_dsb',
    introduction_date=date(1972, 1, 1),
    weight=40,
    cargo_capacity=64,
    loading_speed=15,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st class',
    }),
)
