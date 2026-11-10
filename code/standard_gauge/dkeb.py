import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv_15kv, standard_gauge_all_voltages, badges

COMMON_vectron_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    max_speed=Train.kmhish(200),
    power=8702,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_e_eb_1_dsb = Train(
    **COMMON_vectron_PROPS,
    id='d_e_eb_1_dsb',
    name='DSB EB',
    liveries=make_psd_cc_liveries(
        'pp/eb.psd',
        shading=('eb',),
        paint=('dsb1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    track_type=standard_gauge_25kv_15kv,
    weight=87,
    introduction_date=date(2020, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv', 'electric/ac/25kv'],
        'operator': ['DK/dsb'],
        'manufacturer': ['siemens'],
    }),
)

d_e_eb_2_dsb = Train(
    **COMMON_vectron_PROPS,
    id='d_e_eb_2_dsb',
    name='DSB EB',
    liveries=make_psd_cc_liveries(
        'pp/eb.psd',
        shading=('eb',),
        paint=('dsb2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    track_type=standard_gauge_25kv_15kv,
    weight=87,
    introduction_date=date(2021, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'The 1000th Vectron',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/ac/15kv', 'electric/ac/25kv'],
        'operator': ['DK/dsb'],
        'manufacturer': ['siemens'],
    }),
)

at_e_vectron_1 = Train(
    **COMMON_vectron_PROPS,
    id='at_e_vectron_1',
    name='ÖBB 1293',
    liveries=make_psd_cc_liveries(
        'pp/eb.psd',
        shading=('eb',),
        paint=('öbb1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    track_type=standard_gauge_all_voltages,
    weight=90,
    introduction_date=date(2018, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['AT'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['electric/dc/1500v', 'electric/dc/3kv', 'electric/ac/15kv', 'electric/ac/25kv'],
        'operator': ['AT/obb'],
        'manufacturer': ['siemens'],
    }),
)
