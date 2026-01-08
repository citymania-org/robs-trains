import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_X1_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(120),
    power=1500,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=78,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_X1a_1_sj = Train(
    id='s_e_X1a_1_sj',
    **COMMON_X1_PROPS,
    name='SJ/SL X1',
    liveries=make_psd_cc_liveries(
        'pp/x1.psd',
        shading=('x1a',),
        paint=('x1asj1',),
        overlay=('x1alight'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["DBLUE"]
    ),
    purchase_sprite_towed_id='s_e_X1b_1_sj',
    country='sweden',
    company='sj_70s',
    introduction_date=date(1968, 1, 1),
    cargo_capacity=148,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'Built by ASEA and developed from the X6 this train was used on the Stockholm Commuter Rail with 5 allowed to couple together to make a 10 car train set. One unit was modified for tilting and high speed research',
    }),
).add_articulated_part(
    id='s_e_X1b_1_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/x1.psd',
        shading='x1b',
        paint='x1bsj1',
        overlay='x1blight',
        cc_replace=colours['DBLUE'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=148,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_X1a_2_sj = Train(
    id='s_e_X1a_2_sj',
    **COMMON_X1_PROPS,
    name='SL X1',
    liveries=make_psd_cc_liveries(
        'pp/x1.psd',
        shading=('x1ab',),
        paint=('x1asl1',),
        overlay=('x1alight'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_X1b_2_sj',
    country='sweden',
    company='sl',
    introduction_date=date(1988, 1, 1),
    cargo_capacity=148,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'This rebuild took place in 1988 to increase reliability in cold weather',
    }),
).add_articulated_part(
    id='s_e_X1b_2_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/x1.psd',
        shading='x1b',
        paint='x1bsl1',
        overlay='x1blight',
        cc_replace=colours['DBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=148,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_X1a_3_sj = Train(
    id='s_e_X1a_3_sj',
    **COMMON_X1_PROPS,
    name='SL X1',
    liveries=make_psd_cc_liveries(
        'pp/x1.psd',
        shading=('x1ab',),
        paint=('x1asl2',),
        overlay=('x1alight'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='s_e_X1b_3_sj',
    country='sweden',
    company='sl',
    introduction_date=date(1996, 1, 1),
    cargo_capacity=148,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'Two sets given the same livery as contemporary stock',
    }),
).add_articulated_part(
    id='s_e_X1b_3_sj',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/x1.psd',
        shading='x1b',
        paint='x1bsl2',
        overlay='x1blight',
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=148,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
