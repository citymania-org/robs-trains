import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_47_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(100),
    power=3127,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=118,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

ch_e_ae47_1 = Train(
    **COMMON_47_PROPS,
    id='ch_e_ae47_1',
    name='SBB Ae 4/7 series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1927, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_ae47_2 = Train(
    **COMMON_47_PROPS,
    id='ch_e_ae47_2',
    name='SBB Ae 4/7 series 3',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1930, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
