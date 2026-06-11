import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_42_PROPS = dict(
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
    max_speed=Train.kmhish(80),
    power=1801,
    weight=155,
)

de_s_42_1 = Train(
    **COMMON_42_PROPS,
    id='de_s_42_1',
    purchase_sprite_towed_id='de_s_422_1',
    name='DR 42', #small smoke things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1943, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
        'Trivia': 'Later classed as DB 42',
    }),
).add_articulated_part(
    id='de_s_422_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)
