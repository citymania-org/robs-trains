import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_y1_PROPS = dict( # this is based on the HHJ YM 31
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=26,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=36,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y1_1_dsb = Train(
    id='d_d_y1_1_dsb',
    **COMMON_y1_PROPS,
    name='YM Railbus',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('rb',),
        paint=('rbhhj1',),
        overlay=('rblight'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'HHGB, HHJ',
    }),
)

COMMON_y1dvt_PROPS = dict( # this is based on the HHJ YS 41
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=18,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=58,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y1dvt_1_dsb = Train(
    id='d_d_y1dvt_1_dsb',
    **COMMON_y1dvt_PROPS,
    name='HHJ YS Railbus DVT',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('rbdvt',),
        paint=('rbhhj1',),
        overlay=('rblight'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

COMMON_y2_PROPS = dict( # this is based on the LNJ YM 17
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=27,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=58, #43 seats, ca 15 standing = 58
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y2_1_dsb = Train(
    id='d_d_y2_1_dsb',
    **COMMON_y2_PROPS,
    name='YM Railbus',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('rbl',),
        paint=('rbhhj1',),
        overlay=('rblight'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY3"]
    ),
    country='denmark',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Owners': 'LNJ',
    }),
)

d_d_y2_2_dsb = Train(
    id='d_d_y2_2_dsb',
    **COMMON_y2_PROPS,
    name='VLTJ YM Railbus "Fjorden"',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('rbl',),
        paint=('rblvltj1',),
        overlay=('rblight'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    introduction_date=date(2000, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Trivia': 'One locomotive bought from LNJ in 1999 #15, named Fjorden',
    }),
)

COMMON_y3_PROPS = dict( # this is based on the LNJ YS 25
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=18,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=67, #52 seats, ca 15 standing = 67
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y3_1_dsb = Train(
    id='d_d_y3_1_dsb',
    **COMMON_y3_PROPS,
    name='YS Railbus DVT',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('rbldvt',),
        paint=('rbhhj1',),
        overlay=('rblight'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY3"]
    ),
    country='denmark',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Owners': 'LNJ',
    }),
)

COMMON_y4_PROPS = dict( # this is based on the LJ YM 60
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=25,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=40,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y4_1_dsb = Train(
    id='d_d_y4_1_dsb',
    **COMMON_y4_PROPS,
    name='YM (early)',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('ym',),
        paint=('ymlj1',),
        overlay=('ymlight'),
        r_overlay=('ymlightr'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'HHGB, HHJ, LJ',
    }),
)

COMMON_y6_PROPS = dict( # this is based on the OHJ YM 51
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=26,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=50,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y6_1_dsb = Train(
    id='d_d_y6_1_dsb',
    **COMMON_y6_PROPS,
    name='OHJ YM',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('yml',),
        paint=('ymlj1',),
        overlay=('ymlight'),
        r_overlay=('ymlightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

d_d_y6_4_dsb = Train(
    id='d_d_y6_4_dsb',
    **COMMON_y6_PROPS,
    name='YM',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('yml',),
        paint=('ymlj1',),
        overlay=('ymlight'),
        r_overlay=('ymlightr'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1983, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'HHGB, HHJ',
    }),
)

d_d_y6_2_dsb = Train(
    id='d_d_y6_2_dsb',
    **COMMON_y6_PROPS,
    name='VLTJ YM',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('yml',),
        paint=('ymlvltj1',),
        overlay=('ymlight'),
        r_overlay=('ymlightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    introduction_date=date(1983, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'Three locomotives bought in 1983 #12, #13, #14, named Storåen, Vigen and Tangen',
    }),
)

d_d_y6_3_dsb = Train(
    id='d_d_y6_3_dsb',
    **COMMON_y6_PROPS,
    name='VLTJ YM',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('yml',),
        paint=('ymlvltj2',),
        overlay=('ymlight'),
        r_overlay=('ymlightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'One more locomotive was bought from NJ in 2005 #16, named Heden',
    }),
)

COMMON_y8_PROPS = dict( # this is based on the LJ YS 80
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=18,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y8_1_dsb = Train(
    id='d_d_y8_1_dsb',
    **COMMON_y8_PROPS,
    name='YS',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('ys',),
        paint=('yslj1',),
        overlay=('yslight'),
        r_overlay=('yslightr'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'HHGB, HHJ, LJ',
    }),
)

d_d_y8_2_dsb = Train(
    id='d_d_y8_2_dsb',
    **COMMON_y8_PROPS,
    name='OHJ YS',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('ys',),
        paint=('yslj1',),
        overlay=('yslight'),
        r_overlay=('yslightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

d_d_y8_3_dsb = Train(
    id='d_d_y8_3_dsb',
    **COMMON_y8_PROPS,
    name='VLTJ YS',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('ys',),
        paint=('ysvltj1',),
        overlay=('yslight'),
        r_overlay=('yslightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    introduction_date=date(1983, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

d_d_y8_4_dsb = Train(
    id='d_d_y8_4_dsb',
    **COMMON_y8_PROPS,
    name='VLTJ YS',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('ys',),
        paint=('ysvltj2',),
        overlay=('yslight'),
        r_overlay=('yslightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

COMMON_y9_PROPS = dict( # this is based on the LJ YP 70
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=17,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y9_1_dsb = Train(
    id='d_d_y9_1_dsb',
    **COMMON_y9_PROPS,
    name='YP',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('yp',),
        paint=('yplj1',),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'HHJ, LJ',
    }),
)

d_d_y9_2_dsb = Train(
    id='d_d_y9_2_dsb',
    **COMMON_y9_PROPS,
    name='OHJ YP',
    liveries=make_psd_cc_liveries(
        'pp/ytog.psd',
        shading=('yp',),
        paint=('yplj1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)
