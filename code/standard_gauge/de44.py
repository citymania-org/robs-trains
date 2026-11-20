import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, badges

COMMON_44_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.USE_2CC,
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
    weight=184,
)

de_s_44_1 = Train(
    **COMMON_44_PROPS,
    id='de_s_44_1',
    purchase_sprite_towed_id='de_s_442_1',
    name='DR 44', #small smoke things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    power=1910,
    introduction_date=date(1926, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as DB 44',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['steam'],
        'operator': ['DE/dr'],
        'manufacturer': [],
    }),
).add_articulated_part(
    id='de_s_442_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

de_s_44_2 = Train(
    **COMMON_44_PROPS,
    id='de_s_44_2',
    purchase_sprite_towed_id='de_s_442_2',
    name='DR 44', #big smoke things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    power=1910,
    introduction_date=date(1926, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as DB 44',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['steam'],
        'operator': ['DE/dr'],
        'manufacturer': [],
    }),
).add_articulated_part(
    id='de_s_442_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

de_s_44_3 = Train(
    **COMMON_44_PROPS,
    id='de_s_44_3',
    purchase_sprite_towed_id='de_s_442_3',
    name='DB 44', #small smoke things (oil)
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    power=2101,
    introduction_date=date(1958, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['steam'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
).add_articulated_part(
    id='de_s_442_3',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

de_s_44_4 = Train(
    **COMMON_44_PROPS,
    id='de_s_44_4',
    purchase_sprite_towed_id='de_s_442_4',
    name='DB 44', #big smoke things (oil)
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    power=2101,
    introduction_date=date(1958, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight'],
        'power': ['steam'],
        'operator': ['DE/db'],
        'manufacturer': [],
    }),
).add_articulated_part(
    id='de_s_442_4',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)
