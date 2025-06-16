import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

s_d_ÖCJ25_1 = Train(
    id='s_d_ÖCJ25_1',
    name='ÖCJ 25 (early)',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/ÖCJ_25.psd',
        shading=('ÖCJ 25',),
        paint=('ÖCJ',),
        overlay=('öcjlights'),
        cc_replace=colours["CREAM"],
        cc2_replace=colours["DGREEN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(40),
    power=55,
    introduction_date=date(1924, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=38,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Operator': 'ÖCJ',
        'Use': 'Local passengers',
        'Builder': 'WUMAG',
    }),
)

s_d_ÖCJ25_2 = Train(
    id='s_d_ÖCJ25_2',
    name='ÖCJ 25',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/ÖCJ_25.psd',
        shading=('ÖCJ 25',),
        paint=('ÖCJ',),
        overlay=('öcjlights'),
        cc_replace=colours["REDBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(60),
    power=55,
    introduction_date=date(1924, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=45,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Operator': 'ÖCJ',
        'Use': 'Local passengers',
        'Builder': 'WUMAG',
    }),
)