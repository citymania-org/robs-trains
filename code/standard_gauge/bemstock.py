import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, make_psd_cc_liveries_flippable, standard_gauge, VEHICLE_FLAG_TRAIN_HAS_CAB, badges

COMMON_m4_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(160),
    weight=37,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_m4_1 = Train(
    id='be_p_m4_1',
    **COMMON_m4_PROPS,
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1979, 1, 1),
    cargo_capacity=72,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m4_2 = Train(
    id='be_p_m4_2',
    **COMMON_m4_PROPS,
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1996, 1, 1),
    cargo_capacity=72,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m4_3 = Train(
    id='be_p_m4_3',
    **COMMON_m4_PROPS,
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1979, 1, 1),
    cargo_capacity=104,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m4_4 = Train(
    id='be_p_m4_4',
    **COMMON_m4_PROPS,
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1996, 1, 1),
    cargo_capacity=104,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m4_5 = Train(
    id='be_p_m4_5',
    **COMMON_m4_PROPS,
    name='NMBS AD',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1979, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
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
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m4_6 = Train(
    id='be_p_m4_6',
    **COMMON_m4_PROPS,
    name='NMBS AD',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1996, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
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
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m4_7 = Train(
    id='be_p_m4_7',
    **COMMON_m4_PROPS,
    name='NMBS BD',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1979, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
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
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m4_8 = Train(
    id='be_p_m4_8',
    **COMMON_m4_PROPS,
    name='NMBS BD',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1996, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
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
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

COMMON_m4s_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(160),
    weight=39,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_m4_9 = Train(
    id='be_p_m4_9',
    **COMMON_m4s_PROPS,
    name='NMBS ADx',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"],
    ),
    introduction_date=date(1979, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
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
        'flag': ['BE'],
        'role': ['regional_passenger', 'driving_cab'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

be_p_m4_10 = Train(
    id='be_p_m4_10',
    **COMMON_m4s_PROPS,
    name='NMBS ADx',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('11a',),
        paint=('11b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"],
    ),
    introduction_date=date(1996, 1, 1),
    cargo_capacity=48,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
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
        'flag': ['BE'],
        'role': ['regional_passenger', 'driving_cab'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

COMMON_m5_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(140),
    weight=44,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_m5_1 = Train(
    id='be_p_m5_1',
    **COMMON_m5_PROPS,
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=142,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m5_2 = Train(
    id='be_p_m5_2',
    **COMMON_m5_PROPS,
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2007, 1, 1),
    cargo_capacity=142,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m5_3 = Train(
    id='be_p_m5_3',
    **COMMON_m5_PROPS,
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=146,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m5_4 = Train(
    id='be_p_m5_4',
    **COMMON_m5_PROPS,
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2007, 1, 1),
    cargo_capacity=146,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

COMMON_m5s_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(140),
    weight=49,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_m5_5 = Train(
    id='be_p_m5_5',
    **COMMON_m5s_PROPS,
    name='NMBS BDx',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"],
    ),
    introduction_date=date(1984, 1, 1),
    cargo_capacity=118,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger', 'driving_cab'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

be_p_m5_6 = Train(
    id='be_p_m5_6',
    **COMMON_m5s_PROPS,
    name='NMBS BDx',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"],
    ),
    introduction_date=date(2007, 1, 1),
    cargo_capacity=118,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger', 'driving_cab'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

COMMON_m6_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(160),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_m6_1 = Train(
    id='be_p_m6_1',
    **COMMON_m6_PROPS,
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    weight=50,
    introduction_date=date(1999, 1, 1),
    cargo_capacity=124,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m6_2 = Train(
    id='be_p_m6_2',
    **COMMON_m6_PROPS,
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    weight=50,
    introduction_date=date(1999, 1, 1),
    cargo_capacity=140,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m6_3 = Train(
    id='be_p_m6_3',
    **COMMON_m6_PROPS,
    name='NMBS ABD',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    weight=50,
    introduction_date=date(1999, 1, 1),
    cargo_capacity=103,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m6_4 = Train(
    id='be_p_m6_4',
    **COMMON_m6_PROPS,
    name='NMBS BD',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    weight=50,
    introduction_date=date(2005, 1, 1),
    cargo_capacity=103,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

COMMON_m6s_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(160),
    weight=50,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_m6_5 = Train(
    id='be_p_m6_5',
    **COMMON_m6s_PROPS,
    name='NMBS Bx',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"],
    ),
    introduction_date=date(1999, 1, 1),
    cargo_capacity=136,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger', 'driving_cab'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)

COMMON_m7_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(200),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_m7_1 = Train(
    id='be_p_m7_1',
    **COMMON_m7_PROPS,
    name='NMBS AB',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    weight=53,
    introduction_date=date(2018, 1, 1),
    cargo_capacity=133,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m7_2 = Train(
    id='be_p_m7_2',
    **COMMON_m7_PROPS,
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    weight=53,
    introduction_date=date(2018, 1, 1),
    cargo_capacity=140,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_m7_3 = Train(
    id='be_p_m7_3',
    **COMMON_m7_PROPS,
    name='NMBS BD',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    weight=55,
    introduction_date=date(2018, 1, 1),
    cargo_capacity=103,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

COMMON_m7s_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(200),
    weight=56,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_m7_4 = Train(
    id='be_p_m7_4',
    **COMMON_m7s_PROPS,
    name='NMBS BDx',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"],
    ),
    introduction_date=date(2018, 1, 1),
    cargo_capacity=100,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '20',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger', 'driving_cab'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)
