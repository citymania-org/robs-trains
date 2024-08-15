import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

hu_d_m61_1_mav = Train(
    id='hu_d_m61_1_mav',
    name='MÁV M61',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('mav1',),
        overlay=('light'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["ORANGE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='hungary',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=1650,
    introduction_date=date(1963, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=106,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

hu_d_m61_2_mav = Train(
    id='hu_d_m61_2_mav',
    name='MÁV M61',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('mav2',),
        overlay=('light'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["ORANGE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='hungary',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=1650,
    introduction_date=date(1963, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=106,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)


hu_d_m61_3_mav = Train(
    id='hu_d_m61_3_mav',
    name='MÁV M61',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('mav3',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["WHITE1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='hungary',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=1650,
    introduction_date=date(1963, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=106,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)
