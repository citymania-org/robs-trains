import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_bc_PROPS = dict(
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
    cargo_capacity=38,
    weight=17,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_bc_1 = Train(
    **COMMON_bc_PROPS,
    id='dk_p_bc_1',
    name='DSB BC II', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1915, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
        'Trivia': 'Later classed as CQ I then CY',
    }),
)

dk_p_bc_2 = Train(
    **COMMON_bc_PROPS,
    id='dk_p_bc_2',
    name='DSB BC III', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1923, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
        'Trivia': 'Later classed as CQ II then CY',
    }),
)

dk_p_bc_3 = Train(
    **COMMON_bc_PROPS,
    id='dk_p_bc_3',
    name='DSB CY', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
        'Trivia': 'Vehicles in this class could also appear like the previous 2 in this list',
    }),
)
