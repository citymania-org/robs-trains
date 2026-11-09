import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, badges

COMMON_J_PROPS = dict(
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
    power=620,
    weight=62,
)

se_s_j_1 = Train(
    **COMMON_J_PROPS,
    id='se_s_j_1',
    name='њSJ J',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(75),
    introduction_date=date(1914, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Last steam locomotive to be regularly used in SJ passenger trains'
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['steam'],
        'operator': ['SE/sj'],
        'manufacturer': [],
    }),
)