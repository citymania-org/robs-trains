import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_e04_PROPS = dict(
    length=7,
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
    max_speed=Train.kmhish(130),
    power=2978,
    weight=92,
)

de_e_e04_1 = Train(
    **COMMON_e04_PROPS,
    id='de_e_e04_1',
    name='DR E 04',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    company='na',
    introduction_date=date(1932, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 104 & DR 204',
    }),
)

de_e_e04_2 = Train(
    **COMMON_e04_PROPS,
    id='de_e_e04_2',
    name='DR E 04', #red wheels
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    company='na',
    introduction_date=date(1932, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
        'Trivia': 'Later classed as DB 104 & DR 204',
    }),
)
