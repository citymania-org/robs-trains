import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, VEHICLE_FLAG_TRAIN_HAS_CAB, g

COMMON_se80stock_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    max_speed=Train.kmhish(160), # A7 and B7 had 130 to begin with
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

# Header

s_p_80s = Train(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    max_speed=Train.kmhish(160), # A7 and B7 had 130 to begin with
    vehicle_life=30,
    model_life=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    id='s_p_80s_AB',
    name='80s stock auto',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1978, 1, 1),
    weight=43,
    cargo_capacity=27+27,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Status': 'Not implemented',
    }),
    climates_available=grf.ALL_CLIMATES,
)

# Header

s_p_80s_A = Train(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    max_speed=Train.kmhish(160), # A7 and B7 had 130 to begin with
    vehicle_life=30,
    model_life=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    id='s_p_80s_A',
    name='80s stock 1st class',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1979, 1, 1),
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
    climates_available=grf.NO_CLIMATE,
)

# A7 (A8 too was not very different had phone instead of luggage)

s_p_A7_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A7_1_sj',
    name='SJ A7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1979, 1, 1),
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

# arrows

s_p_A7_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A7_2_sj',
    name='SJ A7/A8',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A2',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1985, 1, 1),
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

# not down whole way 

s_p_A7_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A7_3_sj',
    name='SJ A7/A8',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A3',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

# down whole way 

s_p_A7_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A7_4_sj',
    name='SJ A7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A4',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

s_p_A7_5_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A7_5_sj',
    name='SJ A7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A5',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
        'Trivia': ''
    }),
)

s_p_A7_6_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A7_6_sj',
    name='SJ A7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A6',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2006, 1, 1),
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

# same but line

s_p_A7_7_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A7_7_sj',
    name='SJ A7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A7',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2006, 1, 1),
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
        'Trivia': 'Only one'
    }),
)

s_p_A7_8_ssrt = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A7_8_ssrt',
    name='SSRT A7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A8',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY6"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2007, 1, 1), # date not known but likely 2007 due to the others being refurbised then
    weight=48,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class "night train?"',
    }),
)

# A11

s_p_A11_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_A11_1_sj',
    name='SJ A11',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2001, 1, 1),
    weight=50,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class express',
        'Trivia': 'Meant to be 180',
    }),
)

# AB9

s_p_AB9_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_AB9_1_sj',
    name='SJ AB9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('AB9-1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj90s',
    introduction_date=date(1994, 1, 1),
    weight=43,
    cargo_capacity=27+27,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

s_p_AB9_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_AB9_2_sj',
    name='SJ AB9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('AB9-2',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj90s',
    introduction_date=date(2006, 1, 1),
    weight=43,
    cargo_capacity=27+27,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

s_p_AB7_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_AB7_1_sj',
    name='SJ AB7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('AB9-2',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj90s',
    introduction_date=date(2009, 1, 1),
    weight=43,
    cargo_capacity=27+30,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

# Header

s_p_80s_B = Train(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    max_speed=Train.kmhish(160), # A7 and B7 had 130 to begin with
    vehicle_life=30,
    model_life=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    id='s_p_80s_B',
    name='80s stock 2nd class',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1979, 1, 1),
    weight=46,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
    climates_available=grf.NO_CLIMATE,
)

# B7

s_p_B7_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B7_1_sj',
    name='SJ B7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1979, 1, 1),
    weight=46,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

s_p_B7_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B7_2_sj',
    name='SJ B7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1985, 1, 1),
    weight=46,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# not down whole way 

s_p_B7_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B7_3_sj',
    name='SJ B7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=46,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# down whole way 

s_p_B7_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B7_4_sj',
    name='SJ B7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=46,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

s_p_B7_5_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B7_5_sj',
    name='SJ B7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=46,
    cargo_capacity=80,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

s_p_B7_6_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B7_6_sj',
    name='SJ B7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2006, 1, 1),
    weight=46,
    cargo_capacity=80, # other sources say 78
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

s_p_B7_7_tagab = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B7_7_tagab',
    name='TÅGAB B7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='taagab',
    introduction_date=date(2015, 1, 1),
    weight=46,
    cargo_capacity=76,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# B4 / BF4

s_p_B4_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B4_1_sj',
    name='SJ B4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1985, 1, 1),
    weight=48,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

# not down whole way 

s_p_BF4_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BF4_2_sj',
    name='SJ BF4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=48,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

# down whole way 

s_p_BF4_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BF4_3_sj',
    name='SJ BF4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=48,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

s_p_BF4_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BF4_4_sj',
    name='SJ BF4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=48,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

s_p_BF4_5_ssrt = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BF4_5_ssrt',
    name='SSRT BF4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY6"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2007, 1, 1),
    weight=48,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

s_p_BF7_6_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BF7_6_sj',
    name='SJ BF7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2010, 1, 1),
    weight=48,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

# B2

s_p_B2_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B2_1_sj',
    name='SJ B2',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1988, 1, 1),
    weight=48,
    cargo_capacity=69,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# not down whole way

s_p_B2_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B2_2_sj',
    name='SJ B2',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=48,
    cargo_capacity=69,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# down whole way

s_p_B2_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B2_3_sj',
    name='SJ B2',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=48,
    cargo_capacity=69,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

s_p_B2_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B2_3_sj',
    name='SJ B2',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=48,
    cargo_capacity=69,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

s_p_B2_5_ssrt = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B2_4_ssrt',
    name='SSRT B2',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY6"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2007, 1, 1),
    weight=48,
    cargo_capacity=70,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# B7B / B8

# not down whole way centered text

s_p_B7B_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B7B_1_sj',
    name='SJ B7B',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1990, 1, 1),
    weight=46,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, family',
    }),
)

# not down whole way 

s_p_B8_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B8_2_sj',
    name='SJ B8',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1990, 1, 1),
    weight=46,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, family',
    }),
)

# down whole way 

s_p_B8_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B8_3_sj',
    name='SJ B8',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1990, 1, 1),
    weight=46,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, family',
    }),
)

s_p_B8_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B8_4_sj',
    name='SJ B8',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2006, 1, 1),
    weight=46,
    cargo_capacity=46,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, family',
    }),
)

# B9

s_p_B9_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B9_1_sj',
    name='SJ B9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=48,
    cargo_capacity=68,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
        'Trivai': 'Initally meant for InterRegio traffic',
    }),
)

s_p_B9_2_tkab = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B9_2_tkab',
    name='TKAB B9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2000, 1, 1),
    weight=48,
    cargo_capacity=68,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

s_p_B9_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B9_3_sj',
    name='SJ B9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2006, 1, 1),
    weight=48,
    cargo_capacity=68,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

s_p_B9_3_ssrt = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B9_3_ssrt',
    name='SSRT B9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY6"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2007, 1, 1),
    weight=48,
    cargo_capacity=68,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# B10

s_p_B10_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B10_1_sj',
    name='SJ B10',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2001, 1, 1),
    weight=48,
    cargo_capacity=81+4,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, high capacity',
        'Trivai': 'Has loose chairs inside, TiM',
    }),
)

s_p_B10_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B10_2_sj',
    name='SJ B10',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2001, 1, 1),
    weight=48,
    cargo_capacity=81+4,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, high capacity',
        'Trivai': 'Has loose chairs inside, TiM, Ex S4',
    }),
)

s_p_B10_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B10_3_sj',
    name='SJ B10',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2006, 1, 1),
    weight=48,
    cargo_capacity=81+4,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, high capacity',
        'Trivai': 'Has loose chairs inside, TiM',
    }),
)

s_p_B10_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B10_4_sj',
    name='SJ B10',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2006, 1, 1),
    weight=48,
    cargo_capacity=81+4,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, high capacity',
        'Trivai': 'Has loose chairs inside, TiM, Ex S4',
    }),
)

# B11

s_p_B11_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_B11_1_sj',
    name='SJ B11',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2001, 1, 1),
    weight=49,
    cargo_capacity=78,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class express',
        'Trivia': 'Meant to be 180',
    }),
)

# BF8

s_p_BF8_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BF8_1_sj',
    name='SJ BF8',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('cr1_ca1_cae1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2017, 1, 1),
    weight=49,
    cargo_capacity=72,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
        'Trivia': 'Despite the F in the class it doesn\'t have space for goods only a staff compartment',
    }),
)

s_p_80s_R = Train(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    max_speed=Train.kmhish(160), 
    vehicle_life=30,
    model_life=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    id='s_p_80s_R',
    name='80s stock Resturant / kiosk',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        paint=('A1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1981, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Resturant / kiosk',
    }),
    climates_available=grf.NO_CLIMATE,
)

s_p_R4_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_R4_1_sj',
    name='SJ R4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1987, 1, 1),
    weight=51,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Resturant',
    }),
)

s_p_R4_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_R4_2_sj',
    name='SJ R4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1987, 1, 1),
    weight=51,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Resturant',
    }),
)

s_p_R4_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_R4_3_sj',
    name='SJ R4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1987, 1, 1),
    weight=51,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Resturant',
    }),
)

s_p_R4_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_R4_4_sj',
    name='SJ R4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2002, 1, 1),
    weight=51,
    cargo_capacity=52,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Resturant',
    }),
)

# S12

s_p_S12_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S12_1_sj',
    name='SJ S12',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=55,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Kiosk, Cinema',
    }),
)

s_p_S12_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S12_2_sj',
    name='SJ S12',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=55,
    cargo_capacity=44,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Kiosk, Cinema',
    }),
)

s_p_S12_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S12_3_sj',
    name='SJ S12',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=55,
    cargo_capacity=44,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Kiosk, Cinema',
    }),
)

# BFS9

s_p_BFS9_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BFS9_1_sj',
    name='SJ BFS9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1994, 1, 1),
    weight=49,
    cargo_capacity=41,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, kiosk, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

s_p_BFS9_2_tkab = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BFS9_2_tkab',
    name='TKAB BFS9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2005, 1, 1),
    weight=49,
    cargo_capacity=41,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, kiosk, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

s_p_BFS9_3_ssrt = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BFS9_3_ssrt',
    name='SSRT BFS9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY6"],
        cc2_replace=colours["GREY4"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2007, 1, 1),
    weight=49,
    cargo_capacity=34,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, kiosk, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

s_p_BFS9_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BFS9_4_sj',
    name='SJ BFS9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2007, 1, 1),
    weight=49,
    cargo_capacity=34,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, kiosk, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

s_p_BFS9_5_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BFS9_5_sj',
    name='SJ BFS9',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2024, 1, 1),
    weight=49,
    cargo_capacity=26,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, kiosk, luggage',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

# RB11

s_p_RB11_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_RB11_1_sj',
    name='SJ RB11',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2001, 1, 1),
    weight=53,
    cargo_capacity=36,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, Resturant',
    }),
)

s_p_RB11_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_RB11_2_sj',
    name='SJ RB11',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('half',),
        #paint=('A1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2018, 1, 1),
    weight=53,
    cargo_capacity=36,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, Resturant',
    }),
)

# RB7

s_p_RB7_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_RB7_1_sj',
    name='SJ RB7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2013, 1, 1),
    weight=49,
    cargo_capacity=41,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, Resturant',
    }),
)

# BC4

s_p_BC4_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BC4_1_sj',
    name='SJ BC4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1985, 1, 1),
    weight=49,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Coachette',
    }),
)

s_p_BC4_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BC4_2_sj',
    name='SJ BC4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=49,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Coachette',
    }),
)

s_p_BC4_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BC4_3_sj',
    name='SJ BC4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=49,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Coachette',
    }),
)

s_p_BC4_4_ssrt = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BC4_4_ssrt',
    name='SSRT BC4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY6"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2005, 1, 1),
    weight=49,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Coachette',
    }),
)

s_p_BC4_5_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_BC4_5_sj',
    name='SJ BC4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2006, 1, 1),
    weight=49,
    cargo_capacity=54,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Coachette',
    }),
)

# WL4

s_p_WL4_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_WL4_1_sj',
    name='SJ WL4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1990, 1, 1),
    weight=56,
    cargo_capacity=22,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Sleeper, 1st class',
    }),
)

s_p_WL4_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_WL4_2_sj',
    name='SJ WL4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1990, 1, 1),
    weight=56,
    cargo_capacity=22,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Sleeper, 1st class',
    }),
)

s_p_WL4_3_ssrt = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_WL4_3_ssrt',
    name='SSRT WL4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY6"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2005, 1, 1),
    weight=56,
    cargo_capacity=22,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Sleeper, 1st class',
    }),
)

s_p_WL4_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_WL4_4_sj',
    name='SJ WL4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2006, 1, 1),
    weight=56,
    cargo_capacity=22,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Sleeper, 1st class',
    }),
)

# WL6

s_p_WL6_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_WL6_1_sj',
    name='SJ WL6',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1993, 1, 1),
    weight=55,
    cargo_capacity=39,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Sleeper',
    }),
)

s_p_WL6_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_WL6_2_sj',
    name='SJ WL6',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1993, 1, 1),
    weight=55,
    cargo_capacity=39,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Sleeper',
    }),
)

s_p_WL6_3_ssrt = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_WL6_3_ssrt',
    name='SSRT WL6',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY6"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2007, 1, 1),
    weight=55,
    cargo_capacity=39,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Sleeper',
    }),
)

s_p_WL6_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_WL6_4_sj',
    name='SJ WL6',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        #paint=('A1',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2006, 1, 1),
    weight=55,
    cargo_capacity=39,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Sleeper',
    }),
)

# UA7 / AFM7

s_p_AFM7_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_AFM7_1_sj',
    name='SJ UA7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='sweden',
    company='sj_70s',
    introduction_date=date(1988, 1, 1),
    weight=49,
    cargo_capacity=41,
    loading_speed=10,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class DVT',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

# not down whole way 

s_p_AFM7_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_AFM7_2_sj',
    name='SJ AF7X',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A3',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=49,
    cargo_capacity=41,
    loading_speed=10,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class DVT',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

# down whole way 

s_p_AFM7_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_AFM7_3_sj',
    name='SJ AFM7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A4',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(1988, 1, 1),
    weight=49,
    cargo_capacity=41,
    loading_speed=10,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class DVT',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

s_p_AFM7_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_AFM7_4_sj',
    name='SJ AFM7',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A6',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj_90s',
    introduction_date=date(2006, 1, 1),
    weight=49,
    cargo_capacity=41,
    loading_speed=10,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class DVT',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

# Header

s_p_80s_S = Train(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    max_speed=Train.kmhish(160), 
    vehicle_life=30,
    model_life=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    id='s_p_80s_S',
    name='80s stock Special',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('A1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["GREY3"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1981, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Special',
    }),
    climates_available=grf.NO_CLIMATE,
)

# S1

s_p_S1_1_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S1_1_sj',
    name='SJ S1',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('S1-1',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["GREY3"]
    ),
    country='sweden',
    company='sj70s',
    introduction_date=date(1981, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Conference',
    }),
)

s_p_S1_2_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S1_2_sj',
    name='SJ S1T',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('S1-2',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["BLUE"]
    ),
    country='sweden',
    company='sj90s',
    introduction_date=date(1988, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Conference',
    }),
)

s_p_S1_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S1_3_sj',
    name='SJ S1T',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('S1-3',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj90s',
    introduction_date=date(1990, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Conference',
    }),
)

s_p_S1_4_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S1_4_sj',
    name='SJ S1T',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('S1-3',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj90s',
    introduction_date=date(2004, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Conference, SJ svarar',
    }),
)

s_p_S1_5_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S1_5_sj',
    name='SJ S1',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='sj90s',
    introduction_date=date(2006, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Conference',
    }),
)

s_p_S4_1_asea = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S4_1_asea',
    name='ASEA S4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('S4-1',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1986, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Office',
    }),
)

s_p_S4_2_abb = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S4_2_abb',
    name='ABB S4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('S4-2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1988, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Office',
    }),
)

s_p_S4_3_sj = Train(
    **COMMON_se80stock_PROPS,
    id='s_p_S4_3_sj',
    name='SJ S4',
    liveries=make_psd_cc_liveries(
        'pp/sj80stock.psd',
        shading=('full',),
        paint=('S4-3',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["BLUE"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1989, 1, 1),
    weight=48,
    cargo_capacity=0,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Office',
    }),
)