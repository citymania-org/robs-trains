import grf, lib

from datetime import date

from common import  g, Train, colours, make_psd_cc_liveries, make_psd_cc_liveries_flippable, standard_gauge

se_d_201to202_1 = Train(
    id='se_d_201to202_1',
    name='њUGJ 201-202', 
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(75),
    power=160,
    introduction_date=date(1925, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(32)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=88,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

se_d_Xo6_1 = Train(
    id='se_d_Xo6_1',
    name='њSJ Xo6', 
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(75),
    power=160,
    introduction_date=date(1933, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(32)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=88,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)
