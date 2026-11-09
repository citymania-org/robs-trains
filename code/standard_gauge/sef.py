import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_f_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
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

se_e_f_1 = Train(
    **COMMON_f_PROPS,
    id='se_e_f_1',
    name='SJ F',
    liveries=make_psd_cc_liveries(
        'pp/sef.psd',
        shading=('f',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    max_speed=Train.kmhish(135),
    power=3481,
    weight=102,
    introduction_date=date(1942, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/sj'],
        'manufacturer': ['SE/asea'],
    }),
)
