import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv_15kv, standard_gauge_all_voltages

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
    power_type='15kv/25kv',
    weight=87,
    country='denmark',
    company='na',
    introduction_date=date(2020, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
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
    power_type='15kv/25kv',
    weight=87,
    country='denmark',
    company='na',
    introduction_date=date(2021, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'The 1000th Vectron',
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
    power_type='dc/dc3000/15kv/25kv',
    weight=90,
    country='austria',
    company='na',
    introduction_date=date(2018, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
