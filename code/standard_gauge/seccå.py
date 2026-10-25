import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_Cc_PROPS = dict(
    length=4,
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
    power=577,
    weight=72,
)

se_s_cc_1 = Train(
    **COMMON_Cc_PROPS,
    id='se_s_cc_1',
    purchase_sprite_towed_id='se_s_cc_2',
    name='њSJ Cc',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    max_speed=Train.kmhish(90),
    introduction_date=date(1886, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
).add_articulated_part(
    id='se_s_cc_2',
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='3a',
        paint='3b',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['RED'],
    ),
)