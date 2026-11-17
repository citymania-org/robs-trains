import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, make_psd_cc_liveries_flippable, standard_gauge, VEHICLE_FLAG_TRAIN_HAS_CAB, badges

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
