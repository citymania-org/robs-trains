import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv_3kv_1500v, standard_gauge_all_voltages, badges

COMMON_13_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_25kv_3kv_1500v,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    max_speed=Train.kmhish(200),
    power=7070,
    weight=90,
)

be_e_13_1 = Train(
    id='be_e_13_1',
    **COMMON_13_PROPS,
    name='NMBS HLE 13',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/acdc/1500v_3kv_25kv', 'electric/dc/1500v', 'electric/dc/3kv', 'electric/ac/25kv'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

COMMON_17_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_all_voltages,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    max_speed=Train.kmhish(200),
    power=8702,
    weight=87,
)

be_e_17_1 = Train(
    id='be_e_17_1',
    **COMMON_17_PROPS,
    name='NMBS HLE 17',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["COBALT"]
    ),
    introduction_date=date(2025, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': ['electric/acdc/1500v_3kv_15kv_25kv', 'electric/dc/1500v', 'electric/dc/3kv', 'electric/ac/15kv', 'electric/ac/25kv'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

COMMON_18_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_25kv_3kv_1500v,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    max_speed=Train.kmhish(200),
    power=8158,
    weight=88,
)

be_e_18_1 = Train(
    id='be_e_18_1',
    **COMMON_18_PROPS,
    name='NMBS HLE 18/19',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2009, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['regional_passenger', 'express_passenger'],
        'power': ['electric/acdc/1500v_3kv_25kv', 'electric/dc/1500v', 'electric/dc/3kv', 'electric/ac/25kv'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)
