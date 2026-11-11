import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, make_psd_cc_liveries_flippable, standard_gauge, VEHICLE_FLAG_TRAIN_HAS_CAB, g, badges

COMMON_ew_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(140),
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_p_ewi_1 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_1',
    name='SBB A', #og
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1956, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_2 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_2',
    name='SBB A', #refurb
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_3 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_3',
    name='SBB A', #comfort
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["TURQUOISE"]
    ),
    introduction_date=date(1985, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_4 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_4',
    name='SBB A', #parrot
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["TURQUOISE"]
    ),
    introduction_date=date(1996, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_5 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_5',
    name='SBB AB', #og
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1965, 1, 1),
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_6 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_6',
    name='SBB AB', #refurb
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_7 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_7',
    name='SBB AB', #refurb
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_8 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_8',
    name='SBB B', #og
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1956, 1, 1),
    cargo_capacity=80,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_9 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_9',
    name='SBB B', #refurb
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=80,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_10 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_10',
    name='SBB B', #comfort
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["TURQUOISE"]
    ),
    introduction_date=date(1985, 1, 1),
    cargo_capacity=80,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_p_ewi_11 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewi_11',
    name='SBB B', #parrot
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["TURQUOISE"]
    ),
    introduction_date=date(1996, 1, 1),
    cargo_capacity=80,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)
