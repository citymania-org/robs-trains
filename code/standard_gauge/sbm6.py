import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

d_d_sbm6_1_dsb = Train(
    id='d_d_sbm6_1_dsb',
    name='SB M 6',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/5Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(75),
    power=480,
    introduction_date=date(1952, 1, 1),
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=45,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Operated around Skagen, only 1 made, it is preserved at Aalborg as of 2021',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_d_sbm6_2_dsb = Train(
    id='d_d_sbm6_2_dsb',
    name='SB M 6',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/5Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(75),
    power=480,
    introduction_date=date(1989, 1, 1),
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=45,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Operated around Skagen, only 1 made, it is preserved at Aalborg as of 2021',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)
