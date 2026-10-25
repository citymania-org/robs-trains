import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_E_PROPS = dict(
    length=5,
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
    power=940,

)

se_s_e_1 = Train(
    **COMMON_E_PROPS,
    id='se_s_e_1',
    purchase_sprite_towed_id='se_s_e_2',
    name='њSJ E',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    max_speed=Train.kmhish(65),
    introduction_date=date(1907, 1, 1),
    weight=84,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='se_s_e_2',
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='3a',
        paint='3b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

se_s_e2_1 = Train(
    **COMMON_E_PROPS,
    id='se_s_e2_1',
    purchase_sprite_towed_id='se_s_e2_2',
    name='њSJ E2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    max_speed=Train.kmhish(70),
    introduction_date=date(1935, 1, 1),
    weight=91,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'A leading axle was added to the E locomotives to improve the ride quality and raise the top speed',
    }),
).add_articulated_part(
    id='se_s_e2_2',
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='3a',
        paint='3b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)