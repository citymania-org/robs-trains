import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_49_PROPS = dict(
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
    power=2080,
    weight=152,
)

no_s_49_1 = Train(
    **COMMON_49_PROPS,
    id='no_s_49_1',
    purchase_sprite_towed_id='no_s_49_2',
    name='њNSB Type 49 "Dovregubben"',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='norway',
    company='na',
    max_speed=Train.kmhish(90),
    introduction_date=date(1935, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
).add_articulated_part(
    id='no_s_49_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)