import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_dk30stock_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

# cr

d_p_cr_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_cr_1_dsb',
    name='DSB CR',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('cr',),
        paint=('cr1_ca1_cae1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_cr_1_dsb',
    max_speed=Train.kmhish(120),
    introduction_date=date(1932, 1, 1),
    weight=43,
    cargo_capacity=68,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '3rd class',
    }),
)

d_p_ca_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_ca_1_dsb',
    name='DSB CA',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('cr',),
        paint=('cr1_ca1_cae1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_ca_1_dsb',
    max_speed=Train.kmhish(120),
    introduction_date=date(1941, 1, 1),
    weight=42,
    cargo_capacity=68,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_car_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_car_1_dsb',
    name='DSB CAR',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('cr',),
        paint=('car1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_car_1_dsb',
    max_speed=Train.kmhish(120),
    introduction_date=date(1951, 1, 1),
    weight=44,
    cargo_capacity=24,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Dining car, 2nd class',
    }),
)

d_p_cae_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_cae_1_dsb',
    name='DSB CAE',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('cae',),
        paint=('cr1_ca1_cae1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_cae_1_dsb',
    max_speed=Train.kmhish(120),
    introduction_date=date(1956, 1, 1),
    weight=42,
    cargo_capacity=44,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage, 2nd class',
    }),
)

# aci

d_p_ac_i_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_ac_i_1_dsb',
    name='DSB AC I',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('acii',),
        paint=('cc1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_ac_i_1_dsb',
    max_speed=Train.kmhish(120),
    introduction_date=date(1937, 1, 1),
    weight=33,
    cargo_capacity=42,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

# acii

d_p_ac_ii_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_ac_ii_1_dsb',
    name='DSB AC II',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('acii',),
        paint=('acii1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_ac_ii_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1949, 1, 1),
    weight=37,
    cargo_capacity=42,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

d_p_ag_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_ag_1_dsb',
    name='DSB Ag',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('ag',),
        paint=('acii1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_ag_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1971, 1, 1),
    weight=37,
    cargo_capacity=42,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

d_p_ag_2_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_ag_2_dsb',
    name='DSB Ag',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('ag',),
        paint=('ag1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_ag_2_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=42,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

# au

d_p_au_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_au_1_dsb',
    name='DSB AU',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('au',),
        paint=('cc1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_au_1_dsb',
    max_speed=Train.kmhish(120),
    introduction_date=date(1932, 1, 1),
    weight=44,
    cargo_capacity=56,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st, 2nd & 3rd class',
    }),
)

d_p_aul_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_aul_1_dsb',
    name='DSB AUL',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('au',),
        paint=('cc1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_aul_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1939, 1, 1),
    weight=31,
    cargo_capacity=58,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

d_p_av_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_av_1_dsb',
    name='DSB AV',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('au',),
        paint=('av1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_av_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1961, 1, 1),
    weight=31,
    cargo_capacity=58,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

d_p_abv_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_abv_1_dsb',
    name='DSB ABv',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('abv',),
        paint=('av1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_abv_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1968, 1, 1),
    weight=37,
    cargo_capacity=58,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

d_p_abg_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_abg_1_dsb',
    name='DSB ABg',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('abv',),
        paint=('abg1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_abg_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=58,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

d_p_bv_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_bv_1_dsb',
    name='DSB Bv',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('abv',),
        paint=('bg1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_bv_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1979, 1, 1),
    weight=37,
    cargo_capacity=58,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# cc

d_p_cc_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_cc_1_dsb',
    name='DSB CC',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('cc',),
        paint=('cc1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_cc_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1950, 1, 1),
    weight=34,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_bg_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_bg_1_dsb',
    name='DSB Bg',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('bg',),
        paint=('cc1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_bg_1_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1970, 1, 1),
    weight=34,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_bg_2_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_bg_2_dsb',
    name='DSB Bg',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('bg',),
        paint=('bg1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    purchase_sprite_towed_id='d_p_bg_2_dsb',
    max_speed=Train.kmhish(140),
    introduction_date=date(1972, 1, 1),
    weight=34,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)
