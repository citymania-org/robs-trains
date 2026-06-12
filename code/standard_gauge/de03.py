import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_03_PROPS = dict(
    length=7,
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
)

de_s_03_1 = Train(
    **COMMON_03_PROPS,
    id='de_s_03_1',
    purchase_sprite_towed_id='de_s_032_1',
    name='DR 03', #big smoke things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(130),
    power=1980,
    weight=174,
    country='germany',
    company='na',
    introduction_date=date(1930, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 03',
    }),
).add_articulated_part(
    id='de_s_032_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

de_s_03_2 = Train(
    **COMMON_03_PROPS,
    id='de_s_03_2',
    purchase_sprite_towed_id='de_s_032_2',
    name='DR 03.10', #small smoke things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(140),
    power=1791,
    weight=182,
    country='germany',
    company='na',
    introduction_date=date(1939, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 03.10',
    }),
).add_articulated_part(
    id='de_s_032_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)
