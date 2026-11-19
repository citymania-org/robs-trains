import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv, badges, g

COMMON_44e_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(110),
    power=1599,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=57,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=40,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_cfe44_1 = Train(
    **COMMON_44e_PROPS,
    id='ch_e_cfe44_1',
    name='SBB CFe 4/4',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as BFe 4/4, BDe 4/4 & BDe 570',
    }),
    mid_stats={
        'cargo_capacity': 4,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

COMMON_44_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(125),
    power=2703,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=68,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=64,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rbe44_1 = Train(
    **COMMON_44_PROPS,
    id='ch_e_rbe44_1',
    name='SBB RBe 4/4',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1959, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as RBe 540',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_e_rbe44_2 = Train(
    **COMMON_44_PROPS,
    id='ch_e_rbe44_2',
    name='SBB RBe 4/4',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["SBB"]
    ),
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as RBe 540',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

ch_e_rbe44_3 = Train(
    **COMMON_44_PROPS,
    id='ch_e_rbe44_3',
    name='SBB RBe 4/4',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Trivia': 'Later classed as RBe 540',
    }),
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
)

COMMON_1212_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(125),
    power=3323,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=170,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=120, #200 seats, 0 collapsible seats, ca 160 standing = 360
    loading_speed=20,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabde1212_1 = Train(
    **COMMON_1212_PROPS,
    id='ch_e_rabde1212_1',
    purchase_sprite_towed_id='ch_e_rabde12122_1',
    name='SBB RABDe 12/12',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["NSBRED"]
    ),
    introduction_date=date(1965, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Info': 'Up to 4 RABDe 12/12 or RABDe 8/16 can be coupled together into a train set',
        'Trivia': 'Later classed as RABDe 510',
    }),
    mid_stats={
        'cargo_capacity': 3,
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
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabde12122_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['NSBRED'],
        cc2_replace=colours['NSBRED'],
    ),
    cargo_capacity=120,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabde12123_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['NSBRED'],
        cc2_replace=colours['NSBRED'],
    ),
    cargo_capacity=120,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabde1212_2 = Train(
    **COMMON_1212_PROPS,
    id='ch_e_rabde1212_2',
    purchase_sprite_towed_id='ch_e_rabde12122_2',
    name='SBB RABDe 12/12',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Info': 'Up to 4 RABDe 12/12 or RABDe 8/16 can be coupled together into a train set',
        'Trivia': 'Later classed as RABDe 510',
    }),
    mid_stats={
        'cargo_capacity': 3,
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
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabde12122_2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=120,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabde12123_2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=120,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_816_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(125),
    power=3059,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=149,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=107, #278 seats, 0 collapsible seats, ca 150 standing = 428
    loading_speed=20,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabde816_1 = Train(
    **COMMON_816_PROPS,
    id='ch_e_rabde816_1',
    purchase_sprite_towed_id='ch_e_rabde8162_1',
    name='SBB RABDe 8/16',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["LAVENDER"]
    ),
    introduction_date=date(1976, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Info': 'Up to 4 RABDe 12/12 or RABDe 8/16 can be coupled together into a train set',
        'Trivia': 'Later classed as RABDe 511',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(2, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabde8162_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['LAVENDER'],
    ),
    cargo_capacity=107,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabde8163_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['LAVENDER'],
    ),
    cargo_capacity=107,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabde8164_1',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['LAVENDER'],
    ),
    cargo_capacity=107,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_e_rabde816_2 = Train(
    **COMMON_816_PROPS,
    id='ch_e_rabde816_2',
    purchase_sprite_towed_id='ch_e_rabde8162_2',
    name='SBB RABDe 8/16',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
        'Info': 'Up to 4 RABDe 12/12 or RABDe 8/16 can be coupled together into a train set',
        'Trivia': 'Later classed as RABDe 511',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 20,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(2, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    badges=badges.set_train_badges({
        'flag': ['CH'],
        'role': ['suburban_passenger', 'regional_passenger'],
        'power': ['electric/ac/15kv'],
        'operator': ['CH/sbb'],
        'manufacturer': []
    }),
).add_articulated_part(
    id='ch_e_rabde8162_2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=107,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabde8163_2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=107,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='ch_e_rabde8164_2',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='11a',
        paint='11b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=107,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
