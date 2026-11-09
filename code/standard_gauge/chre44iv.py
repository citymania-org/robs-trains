import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges

COMMON_44_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(160),
    power=6744,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=80,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

ch_e_re44iv_1 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44iv_1',
    name='SBB Re 4/4 IV',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    introduction_date=date(1982, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as Re 446',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': [],
    }),
)

ch_e_re44iv_2 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44iv_2',
    name='SBB Re 4/4 IV',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1982, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as Re 446',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': [],
    }),
)

ch_e_re44iv_3 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44iv_3',
    name='SBB Re 4/4 IV',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1982, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as Re 446',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': [],
    }),
)

ch_e_re44iv_4 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44iv_4',
    name='SBB Re 4/4 IV',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1982, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as Re 446',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': [],
    }),
)

ch_e_re44iv_5 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44iv_5',
    name='SBB Re 4/4 IV',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1986, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as Re 446',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': [],
    }),
)
