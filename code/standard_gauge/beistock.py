import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, make_psd_cc_liveries_flippable, standard_gauge, VEHICLE_FLAG_TRAIN_HAS_CAB, g, badges

COMMON_i6_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(160),
    weight=42,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_i6_1 = Train(
    **COMMON_i6_PROPS,
    id='be_p_i6_1',
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1977, 1, 1),
    cargo_capacity=54,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i6_2 = Train(
    **COMMON_i6_PROPS,
    id='be_p_i6_2',
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1991, 1, 1),
    cargo_capacity=54,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i6_3 = Train(
    **COMMON_i6_PROPS,
    id='be_p_i6_3',
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1999, 1, 1),
    cargo_capacity=54,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i6_4 = Train(
    **COMMON_i6_PROPS,
    id='be_p_i6_4',
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2017, 1, 1),
    cargo_capacity=54,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i6_5 = Train(
    **COMMON_i6_PROPS,
    id='be_p_i6_5',
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1977, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i6_6 = Train(
    **COMMON_i6_PROPS,
    id='be_p_i6_6',
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1991, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i6_7 = Train(
    **COMMON_i6_PROPS,
    id='be_p_i6_7',
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1999, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i6_8 = Train(
    **COMMON_i6_PROPS,
    id='be_p_i6_8',
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2017, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

COMMON_i11_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(200),
    weight=45,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_i11_1 = Train(
    **COMMON_i11_PROPS,
    id='be_p_i11_1',
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1995, 1, 1),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i11_2 = Train(
    **COMMON_i11_PROPS,
    id='be_p_i11_2',
    name='NMBS A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2024, 1, 1),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs', 'FR/ouigo'],
        'manufacturer': []
    }),
)

be_p_i11_3 = Train(
    **COMMON_i11_PROPS,
    id='be_p_i11_3',
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1995, 1, 1),
    cargo_capacity=80,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': []
    }),
)

be_p_i11_4 = Train(
    **COMMON_i11_PROPS,
    id='be_p_i11_4',
    name='NMBS B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2024, 1, 1),
    cargo_capacity=80,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger'],
        'power': [],
        'operator': ['BE/nmbs', 'FR/ouigo'],
        'manufacturer': []
    }),
)

COMMON_i11s_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    max_speed=Train.kmhish(200),
    weight=46,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    extra_flags=VEHICLE_FLAG_TRAIN_HAS_CAB,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

be_p_i11_5 = Train(
    **COMMON_i11s_PROPS,
    id='be_p_i11_5',
    name='NMBS BDx',
    liveries=make_psd_cc_liveries_flippable(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"],
        intermediate_graphics_chain=Train.Flip.switch_graphics
    ),
    introduction_date=date(1995, 1, 1),
    cargo_capacity=58,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['express_passenger', 'driving_cab'],
        'power': [],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
        'attribute': ['push_pull'],
    }),
)
