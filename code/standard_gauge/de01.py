import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_01_PROPS = dict(
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

de_s_01_1 = Train(
    **COMMON_01_PROPS,
    id='de_s_01_1',
    purchase_sprite_towed_id='de_s_012_1',
    name='DR 01', #big smoke things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(130),
    power=2241,
    weight=184,
    country='germany',
    company='na',
    introduction_date=date(1925, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 01',
    }),
).add_articulated_part(
    id='de_s_012_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

de_s_01_2 = Train(
    **COMMON_01_PROPS,
    id='de_s_01_2',
    purchase_sprite_towed_id='de_s_012_2',
    name='DR 01.10', #small smoke things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(150),
    power=2120,
    weight=197,
    country='germany',
    company='na',
    introduction_date=date(1939, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 011',
    }),
).add_articulated_part(
    id='de_s_012_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

de_s_01_3 = Train(
    **COMMON_01_PROPS,
    id='de_s_01_3',
    purchase_sprite_towed_id='de_s_012_3',
    name='DR 01.10', #small smoke things (new boiler)
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(150),
    power=2349,
    weight=192,
    country='germany',
    company='na',
    introduction_date=date(1953, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 011',
    }),
).add_articulated_part(
    id='de_s_012_3',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

de_s_01_4 = Train(
    **COMMON_01_PROPS,
    id='de_s_01_4',
    purchase_sprite_towed_id='de_s_012_4',
    name='DR 01.10', #small smoke things (oil)
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(150),
    power=2470,
    weight=197,
    country='germany',
    company='na',
    introduction_date=date(1956, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 012',
    }),
).add_articulated_part(
    id='de_s_012_4',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)
