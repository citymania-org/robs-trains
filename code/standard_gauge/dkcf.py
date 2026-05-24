import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_cf_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    max_speed=Train.kmhish(80),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_cf_1 = Train(
    **COMMON_cf_PROPS,
    id='dk_p_cf_1',
    name='DSB CF III', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    cargo_capacity=66,
    weight=14,
    introduction_date=date(1912, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
        'Trivia': 'Later classed as CX',
    }),
)

dk_p_cf_2 = Train(
    **COMMON_cf_PROPS,
    id='dk_p_cf_2',
    name='DSB CF II', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    country='denmark',
    company='na',
    cargo_capacity=64,
    weight=17,
    introduction_date=date(1923, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
        'Trivia': 'Later classed as CFM then CXM',
    }),
)

dk_p_cf_3 = Train(
    **COMMON_cf_PROPS,
    id='dk_p_cf_3',
    name='DSB CXM', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    cargo_capacity=60,
    weight=16,
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
        'Trivia': 'Vehicles in this class could also appear like the CF II',
    }),
)
