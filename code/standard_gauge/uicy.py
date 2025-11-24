import grf, lib

from datetime import date

from common import g, Train, LuggageTrain, colours, make_psd_cc_liveries, standard_gauge

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
        'pp/uicy.psd',
        shading=('b',),
        paint=('b1_bd1_bn1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
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
        'pp/uicy.psd',
        shading=('b',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2_an2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=80,
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
        'pp/uicy.psd',
        shading=('b',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2_an2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1973, 1, 1),
    weight=40,
    cargo_capacity=64,
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
        'pp/uicy.psd',
        shading=('b',),
        paint=('bk2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
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
        'pp/uicy.psd',
        shading=('ab',),
        paint=('ab1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
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
        'pp/uicy.psd',
        shading=('ab',),
        paint=('ab2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
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
        'pp/uicy.psd',
        shading=('ab',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2_an2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
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
        'pp/uicy.psd',
        shading=('a',),
        paint=('a1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
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
        'pp/uicy.psd',
        shading=('a',),
        paint=('a2_an1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
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
        'pp/uicy.psd',
        shading=('a',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2_an2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1991, 1, 1),
    weight=40,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_bd_1_dsb = LuggageTrain(
    **COMMON_b_PROPS,
    id='d_p_bd_1_dsb',
    name='DSB BD',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bd',),
        paint=('b1_bd1_bn1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1968, 1, 1),
    weight=37,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': 'Luggage carriage, 2nd class',
    }),
    luggage_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'properties': {'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(4)},
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

d_p_bd_2_dsb = LuggageTrain(
    **COMMON_b_PROPS,
    id='d_p_bd_2_dsb',
    name='DSB BD',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bd',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2_an2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=48,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': 'Luggage carriage, 2nd class',
    }),
    luggage_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(4),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

d_p_bd_3_dsb = LuggageTrain(
    **COMMON_b_PROPS,
    id='d_p_bd_3_dsb',
    name='DSB BDk',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bd',),
        paint=('bdk1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1986, 1, 1),
    weight=37,
    cargo_capacity=18,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': 'Luggage carriage with kiosk, 2nd class',
    }),
    luggage_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(4),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

d_p_bn_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_1_dsb',
    name='DSB Bn',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bn',),
        paint=('b1_bd1_bn1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1971, 1, 1),
    weight=40,
    cargo_capacity=80,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
        'Trivia': 'Bn & variants used on Sjælland until early 2010s by then many were scrapped or sold',
    }),
)

d_p_bn_2_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_2_dsb',
    name='DSB Bn',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bn',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2_an2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=40,
    cargo_capacity=80,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
        'Trivia': 'Used in Stockholm when SL lacked rolling stock - 1 or 2 of these can also be sandwiched between 2 MO railbusses',
    }),
)

d_p_bn_3_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_3_dsb',
    name='DSB Bn',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bn',),
        paint=('bn3',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2006, 1, 1),
    weight=40,
    cargo_capacity=80,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_bn_4_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_4_dsb',
    name='DSB BDn',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bn',),
        paint=('bn4',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1993, 1, 1),
    weight=36,
    cargo_capacity=48,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class, bike storage',
    }),
)

d_p_bn_5_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_5_dsb',
    name='DSB Bn-x',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bn',),
        paint=('bn5',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1990, 1, 1),
    weight=36,
    cargo_capacity=48,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': '''Local trains, 2nd class, children's carriage''',
        'Trivia': 'Features a ball pit, DSB staff act as child carers',
    }),
)

d_p_bn_6_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_bn_6_dsb',
    name='OHJ BDn',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('bn',),
        paint=('bn6',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1992, 1, 1),
    weight=40,
    cargo_capacity=80,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
        'Trivia': 'Four carriages bought from DSB in 1992 and 1993',
    }),
)

d_p_an_1_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_an_1_dsb',
    name='DSB An',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('an',),
        paint=('a2_an1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=40,
    cargo_capacity=64,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st class',
    }),
)

d_p_an_2_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_an_2_dsb',
    name='DSB Ban',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('an',),
        paint=('b2_ba1_bab1_bd2_bk1_bn2_an2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1991, 1, 1),
    weight=40,
    cargo_capacity=64,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_an_3_dsb = Train(
    **COMMON_b_PROPS,
    id='d_p_an_3_dsb',
    name='DSB BDan',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('an',),
        paint=('an3',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1991, 1, 1),
    weight=37,
    cargo_capacity=48,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class, bike storage',
    }),
)

fr_p_a_1_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_a_1_sncf',
    name='SNCF A9',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_a',),
        paint=('fr_a1',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["DGREEN"]
    ),
    country='france',
    company='na',
    introduction_date=date(1965, 1, 1),
    weight=42,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

fr_p_a_2_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_a_2_sncf',
    name='SNCF A9',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_a',),
        paint=('fr_a2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1971, 1, 1),
    weight=42,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

fr_p_a_3_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_a_3_sncf',
    name='SNCF A9',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_a',),
        paint=('fr_a3',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1979, 1, 1),
    weight=42,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

fr_p_ab_1_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_ab_1_sncf',
    name='SNCF A4B5',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_ab',),
        paint=('fr_ab1',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["DGREEN"]
    ),
    country='france',
    company='na',
    introduction_date=date(1969, 1, 1),
    weight=42,
    cargo_capacity=64,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

fr_p_ab_2_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_ab_2_sncf',
    name='SNCF A4B5',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_ab',),
        paint=('fr_ab2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1971, 1, 1),
    weight=42,
    cargo_capacity=64,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

fr_p_ab_3_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_ab_3_sncf',
    name='SNCF A4B5',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_ab',),
        paint=('fr_ab3',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1979, 1, 1),
    weight=42,
    cargo_capacity=64,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

fr_p_b_1_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_b_1_sncf',
    name='SNCF B10',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_b',),
        paint=('fr_b1',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["DGREEN"]
    ),
    country='france',
    company='na',
    introduction_date=date(1964, 1, 1),
    weight=42,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

fr_p_b_2_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_b_2_sncf',
    name='SNCF B10',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_b',),
        paint=('fr_b2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1971, 1, 1),
    weight=42,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

fr_p_b_3_sncf = Train(
    **COMMON_b_PROPS,
    id='fr_p_b_3_sncf',
    name='SNCF B10',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_b',),
        paint=('fr_b3',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1979, 1, 1),
    weight=42,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

fr_p_ad_1_sncf = LuggageTrain(
    **COMMON_b_PROPS,
    id='fr_p_ad_1_sncf',
    name='SNCF A7D',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_ad',),
        paint=('fr_ad1',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["DGREEN"]
    ),
    country='france',
    company='na',
    introduction_date=date(1968, 1, 1),
    weight=42,
    cargo_capacity=42,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage, 1st class',
    }),
    luggage_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(4),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

fr_p_ad_2_sncf = LuggageTrain(
    **COMMON_b_PROPS,
    id='fr_p_ad_2_sncf',
    name='SNCF A7D',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_ad',),
        paint=('fr_ad2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1971, 1, 1),
    weight=42,
    cargo_capacity=42,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage, 1st class',
    }),
    luggage_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(4),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

fr_p_ad_3_sncf = LuggageTrain(
    **COMMON_b_PROPS,
    id='fr_p_ad_3_sncf',
    name='SNCF B7D',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_ad',),
        paint=('fr_ad3',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1979, 1, 1),
    weight=42,
    cargo_capacity=56,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage, 2nd class',
    }),
    luggage_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(4),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

fr_p_bd_1_sncf = LuggageTrain(
    **COMMON_b_PROPS,
    id='fr_p_bd_1_sncf',
    name='SNCF B5D',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_bd',),
        paint=('fr_bd1',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=42,
    cargo_capacity=40,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage, 2nd class',
    }),
    luggage_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(4),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

fr_p_bd_2_sncf = LuggageTrain(
    **COMMON_b_PROPS,
    id='fr_p_bd_2_sncf',
    name='SNCF B5D',
    liveries=make_psd_cc_liveries(
        'pp/uicy.psd',
        shading=('fr_bd',),
        paint=('fr_bd2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='france',
    company='na',
    introduction_date=date(1979, 1, 1),
    weight=42,
    cargo_capacity=40,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Luggage carriage, 2nd class',
    }),
    luggage_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'callbacks': {
            'cargo_capacity': LuggageTrain.switch_cargo_capacity_by_load_limit(4),
            'cargo_subtype_text': LuggageTrain.switch_subtype(g),
        },
    },
)

COMMON_bns_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=1,
    callbacks={'properties': {'power': 0},},
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_p_bns_1_dsb = Train(
    **COMMON_bns_PROPS,
    id='d_p_bns_1_dsb',
    name='њDSB Bns (I)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=40,
    cargo_capacity=72,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class DVT',
    }),
)

d_p_bns_2_dsb = Train(
    **COMMON_bns_PROPS,
    id='d_p_bns_2_dsb',
    name='њDSB ABns (I)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1989, 1, 1),
    weight=38,
    cargo_capacity=40,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st & 2nd class DVT',
    }),
)

d_p_bns_3_dsb = Train(
    **COMMON_bns_PROPS,
    id='d_p_bns_3_dsb',
    name='њDSB ADns (I)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1990, 1, 1),
    weight=38,
    cargo_capacity=41,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st & 2nd class DVT',
    }),
)

d_p_bns_4_dsb = Train(
    **COMMON_bns_PROPS,
    id='d_p_bns_4_dsb',
    name='њDSB ABns (I)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2006, 1, 1),
    weight=38,
    cargo_capacity=40,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st & 2nd class DVT',
    }),
)

d_p_bns_5_dsb = Train(
    **COMMON_bns_PROPS,
    id='d_p_bns_5_dsb',
    name='њDSB ADns-e (I)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2006, 1, 1),
    weight=38,
    cargo_capacity=41,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st & 2nd class DVT',
    }),
)

d_p_bns_6_dsb = Train(
    **COMMON_bns_PROPS,
    id='d_p_bns_6_dsb',
    name='њOHJ Bns 270',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1994, 1, 1),
    weight=40,
    cargo_capacity=72,
    loading_speed=20,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class DVT',
    }),
)
