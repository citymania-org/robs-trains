import grf, lib

from datetime import date

from common import Train, LuggageTrain, colours, make_psd_cc_liveries, standard_gauge, g

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
    max_speed=Train.kmhish(120),
    introduction_date=date(1951, 1, 1),
    weight=44,
    cargo_capacity=24,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Dining car, 2nd class',
    }),
)

d_p_cae_1_dsb = LuggageTrain(
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
    max_speed=Train.kmhish(120),
    introduction_date=date(1956, 1, 1),
    weight=42,
    cargo_capacity=44,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage, 2nd class',
    }),
    luggage_stats={
        'cargo_capacity': 3,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(3),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
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
    max_speed=Train.kmhish(120),
    introduction_date=date(1937, 1, 1),
    weight=33,
    cargo_capacity=42,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

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

d_p_crl_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_crl_1_dsb',
    name='DSB CRL',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('cc',),
        paint=('cc1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1939, 1, 1),
    weight=35,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '3rd class',
    }),
)

d_p_cb_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_cb_1_dsb',
    name='DSB CB',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('cc',),
        paint=('cc1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1941, 1, 1),
    weight=35,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

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
    name='DSB Cc',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('bg',),
        paint=('cc1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(140),
    introduction_date=date(1968, 1, 1),
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
    max_speed=Train.kmhish(140),
    introduction_date=date(1972, 1, 1),
    weight=34,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_b_1_lj = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_b_1_lj',
    name='LJ B 79',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('cc',),
        paint=('ljb79',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(140),
    introduction_date=date(1983, 1, 1),
    weight=34,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_b_2_lj = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_b_2_lj',
    name='LJ B 75',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('bg',),
        paint=('ljb75',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(140),
    introduction_date=date(1989, 1, 1),
    weight=34,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# luggage

d_p_bdg_1_dsb = LuggageTrain(
    **COMMON_dk30stock_PROPS,
    id='d_p_bdg_1_dsb',
    name='DSB BDg',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('bdg',),
        paint=('bg1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(140),
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=40,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage, 2nd class',
    }),
    luggage_stats={
        'cargo_capacity': 3,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(3),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

# dance

d_p_bu_1_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_bu_1_dsb',
    name='DSB BU',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('au',),
        paint=('bu1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1964, 1, 1),
    weight=43,
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Excursion & dance carriage',
    }),
)

d_p_bu_2_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_bu_2_dsb',
    name='DSB BU',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('au',),
        paint=('bu2',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1964, 1, 1),
    weight=43,
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Excursion & dance carriage',
    }),
)

d_p_bu_3_dsb = Train(
    **COMMON_dk30stock_PROPS,
    id='d_p_bu_3_dsb',
    name='DSB Buh',
    liveries=make_psd_cc_liveries(
        'pp/dk30stock.psd',
        shading=('au',),
        paint=('bu3',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1973, 1, 1),
    weight=43,
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Excursion & dance carriage',
        'Trivia': '#704 appeared in the film "Olsenbanden på Sporet" in 1975',
    }),
)

# local

COMMON_CL_PROPS = dict(
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_p_cl_1_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_1_dsb',
    name='њDSB CL',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(110),
    power=0,
    introduction_date=date(1943, 1, 1),
    weight=29,
    cargo_capacity=87,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_cl_9_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_9_dsb',
    name='њHFHJ C 61',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1949, 1, 1),
    weight=29,
    cargo_capacity=71,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_cl_10_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_10_dsb',
    name='њHFHJ C 61',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1958, 1, 1),
    weight=29,
    cargo_capacity=71,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_cl_11_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_11_dsb',
    name='њHFHJ C 61',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1975, 1, 1),
    weight=29,
    cargo_capacity=71,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_cl_8_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_8_dsb',
    name='њLJ P 76',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1975, 1, 1),
    weight=29,
    cargo_capacity=87,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_cl_7_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_7_dsb',
    name='њHTJ CLE 71',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1981, 1, 1),
    weight=29,
    cargo_capacity=87,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class luggage carriage',
    }),
)

d_p_cl_2_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_2_dsb',
    name='њDSB CLE',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1945, 1, 1),
    weight=28,
    cargo_capacity=61,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class luggage carriage',
    }),
)

d_p_cl_3_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_3_dsb',
    name='њDSB CLS',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(120),
    power=1,
    callbacks={'properties': {'power': 0},},
    introduction_date=date(1960, 1, 1),
    weight=37,
    cargo_capacity=87,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class DVT',
    }),
)

d_p_cl_5_dsb = Train(
    **COMMON_CL_PROPS,
    id='d_p_cl_5_dsb',
    name='њDSB Bhs',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(100),
    power=1,
    callbacks={'properties': {'power': 0},},
    introduction_date=date(1968, 1, 1),
    weight=37,
    cargo_capacity=73,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT for use with MO railcars',
    }),
)
