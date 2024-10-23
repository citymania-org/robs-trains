import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_dre93_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    country='germany',
    max_speed=Train.kmhish(70),
    power=3355,
    weight=118,
)

de_e_dre93_1_dr = Train(
    id='de_e_dre93_1_dr',
    **COMMON_dre93_PROPS,
    name='њDR E 93/DB 193',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["DGREEN"]
    ),
    company='na',
    introduction_date=date(1933, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)

COMMON_dre94_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    country='germany',
    max_speed=Train.kmhish(100),
    power=4020,
    weight=119,
)

de_e_dre94_1_dr = Train(
    id='de_e_dre94_1_dr',
    **COMMON_dre94_PROPS,
    name='њDR E 94/DB 194/DR 254',
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["DGREEN"]
    ),
    company='na',
    introduction_date=date(1940, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)
