import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_ra_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    power=3540,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    max_speed=Train.kmhish(150),
    weight=61,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

# early

s_e_ra_1_sj = Train(
    id='s_e_ra_1_sj',
    **COMMON_ra_PROPS,
    name='SJ Ra',
    liveries=make_psd_cc_liveries(
        'pp/ra.psd',
        shading=('ra',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY7"]
    ),
    introduction_date=date(1955, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/sj'],
        'manufacturer': ['SE/asea'],
    }),
)

s_e_ra_2_sj = Train(
    id='s_e_ra_2_sj',
    **COMMON_ra_PROPS,
    name='SJ Ra',
    liveries=make_psd_cc_liveries(
        'pp/ra.psd',
        shading=('ra',),
        paint=('sj2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["TURQUOISE"]
    ),
    introduction_date=date(1961, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/sj'],
        'manufacturer': ['SE/asea'],
    }),
)

# late

s_e_ra_3_sj = Train(
    id='s_e_ra_3_sj',
    **COMMON_ra_PROPS,
    name='SJ Ra',
    liveries=make_psd_cc_liveries(
        'pp/ra.psd',
        shading=('ral',),
        paint=('sj3',),
        overlay=('llight'),
        r_overlay=('llightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["TURQUOISE"]
    ),
    introduction_date=date(1983, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/sj'],
        'manufacturer': ['SE/asea'],
    }),
)

s_e_ra_4_sj = Train(
    id='s_e_ra_4_sj',
    **COMMON_ra_PROPS,
    name='SJ Ra',
    liveries=make_psd_cc_liveries(
        'pp/ra.psd',
        shading=('ral',),
        paint=('sj4',),
        overlay=('llight'),
        r_overlay=('llightr'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["TURQUOISE"]
    ),
    introduction_date=date(1994, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/sj'],
        'manufacturer': ['SE/asea'],
    }),
)

s_e_ra_5_sj = Train(
    id='s_e_ra_5_sj',
    **COMMON_ra_PROPS,
    name='SJ Ra',
    liveries=make_psd_cc_liveries(
        'pp/ra.psd',
        shading=('ral',),
        paint=('sj5',),
        overlay=('llight'),
        r_overlay=('llightr'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/sj'],
        'manufacturer': ['SE/asea'],
    }),
)
