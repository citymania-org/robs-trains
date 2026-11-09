import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, badges

COMMON_M3s_PROPS = dict(
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
    power=1455,
    weight=135,
)

se_s_m3s_1 = Train(
    **COMMON_M3s_PROPS,
    id='se_s_m3s_1',
    purchase_sprite_towed_id='se_s_m3s_2',
    name='њBJ M3s ',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(70),
    introduction_date=date(1930, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''Sweden's second most powerful steam locomtive after SJ's R-locomotives'''
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight'],
        'power': ['steam'],
        'operator': ['SE/bj'],
        'manufacturer': [],
    }),
).add_articulated_part(
    id='se_s_m3s_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)