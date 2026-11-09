import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_ma_PROPS = dict(
    length=8,
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
    max_speed=Train.kmhish(105),
    power=5384,
    weight=105,
)

se_e_ma_1 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_1',
    name='SJ Ma',
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('ma',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["GREY10"]
    ),
    introduction_date=date(1953, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/sj'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_2 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_2',
    name='TGOJ Ma',
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('ma',),
        paint=('tgoj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["MECONIUM"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(1953, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/tgoj'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_3 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_3',
    name='TGOJ Ma',
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('ma',),
        paint=('tgoj2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/tgoj'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_4 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_4',
    name='SJ Ma',
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('mal',),
        paint=('sj2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/sj'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_3l = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_3l',
    name='TGOJ Ma',
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('mal',),
        paint=('tgoj2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/tgoj'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_5 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_5',
    name='TGOJ Ma', #øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('mal',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["APPLE"],
        cc2_replace=colours["BLUE"]
    ),
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/tgoj'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_6 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_6',
    name='BK Ma', #øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('mal',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["BLUE"]
    ),
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/Bk'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_7 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_7',
    name='TGOJ Ma', #øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('mal',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["APPLE"],
        cc2_replace=colours["BLUE"]
    ),
    introduction_date=date(2001, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/tgoj'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_8 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_8',
    name='NR Ma', #øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('mal',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(2011, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/NR'],
        'manufacturer': ['SE/asea'],
    }),
)

se_e_ma_9 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_9',
    name='BJ Ma', #øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('mal',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["ORANGE"]
    ),
    introduction_date=date(2019, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['SE/bjs'],
        'manufacturer': ['SE/asea'],
    }),
)

no_e_ma_1 = Train(
    **COMMON_ma_PROPS,
    id='no_e_ma_1',
    name='NTA Ma', #øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
    liveries=make_psd_cc_liveries(
        'pp/sema.psd',
        shading=('mal',),
        paint=('sj1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(2014, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['NO'],
        'role': ['express_passenger', 'regional_passenger', 'freight'],
        'power': ['electric/ac/15kv'],
        'operator': ['NO/nta'],
        'manufacturer': ['SE/asea'],
    }),
)
