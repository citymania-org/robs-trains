import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_H3s_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.USE_2CC,
    power_type='steam',
    engine_class=Train.EngineClass.STEAM, 
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    power=1400,
    weight=131,
)

se_s_h3s_1 = Train(
    **COMMON_H3s_PROPS,
    id='se_s_h3s_1',
    purchase_sprite_towed_id='se_s_h3s_2',
    name='њBJ H3s ',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    max_speed=Train.kmhish(100),
    introduction_date=date(1927, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Highest top speed of any steam locomotive in Sweden',
    }),
).add_articulated_part(
    id='se_s_h3s_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

se_s_a8_1 = Train(
    **COMMON_H3s_PROPS,
    id='se_s_a8_1',
    purchase_sprite_towed_id='se_s_a8_2',
    name='њSJ A8 ',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    max_speed=Train.kmhish(100),
    introduction_date=date(1948, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''After BJ's nationalisation in 1948 these ex-H3s locomotives were quickly proven redundant since the former BJ mainline was electrified and their high axle-load made them incompatible with many other parts of the network''',
    }),
).add_articulated_part(
    id='se_s_a8_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)