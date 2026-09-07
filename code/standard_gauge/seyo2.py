import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_Yo2_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=220,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=26,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=55,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_d_Yo2_1_MSJ = Train(
    id='s_d_Yo2_1_MSJ',
    **COMMON_Yo2_PROPS,
    name='њMSJ 11-12/TRJ Yho',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["CREAM"]
    ),
    country='sweden',
    introduction_date=date(1938, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'MSJ',
        'Use': 'Local passengers',
    }),
)

s_d_Yo2_2_BJ = Train(
    id='s_d_Yo2_2_BJ',
    **COMMON_Yo2_PROPS,
    name='њBJ Yo6',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["CREAM"]
    ),
    country='sweden',
    introduction_date=date(1938, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'BJ',
        'Use': 'Local passengers',
    }),
)

s_d_Yo2_3_SJ = Train(
    id='s_d_Yo2_3_SJ',
    **COMMON_Yo2_PROPS,
    name='њSJ Yo2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["YELLOW"]
    ),
    country='sweden',
    introduction_date=date(1943, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'BJ',
        'Use': 'Local passengers',
    }),
)

# TrailerS

s_p_YCDFo_1_TRJ = Train(
    id='s_p_YCDFo_1_TRJ',
    name='њTRJ YCDFo',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["CREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(70),
    power=0,
    introduction_date=date(1938, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=55,
    cost_factor=18,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

s_p_UBFo9_1_SJ = Train(
    id='s_p_UBFo9_1_SJ',
    name='њSJ UBFo9',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(110),
    power=0,
    introduction_date=date(1959, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=55,
    cost_factor=18,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)