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

COMMON_ews_PROPS = dict(
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
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    mid_stats={
        'cargo_capacity': 1,
        'refittable_cargo_classes': grf.CargoClass.MAIL,
        'callbacks': {
            'cargo_subtype_text': Train.Flip.switch_subtype(g),
            'cargo_capacity': 0,
        },
    },
)

ch_p_ewi_12 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_12',
    name='SBB ABt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1956, 1, 1),
    cargo_capacity=54,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_13 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_13',
    name='SBB ABt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["SBB"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=54,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_14 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_14',
    name='SBB DZt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1956, 1, 1),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    mid_stats={
        'cargo_capacity': 8,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(3, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_15 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_15',
    name='SBB DZt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["SBB"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    mid_stats={
        'cargo_capacity': 8,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(3, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_16 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_16',
    name='SBB BDt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1965, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(3, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_17 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_17',
    name='SBB BDt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["SBB"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(3, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_18 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_18',
    name='SBB DZt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1965, 1, 1),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    mid_stats={
        'cargo_capacity': 8,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(3, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_19 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_19',
    name='SBB Dt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["SBB"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    mid_stats={
        'cargo_capacity': 8,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(3, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_20 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_20',
    name='SBB BDt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(3, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

ch_p_ewi_21 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewi_21',
    name='SBB BDt',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(3, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger', 'express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['CH/sbb'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)
