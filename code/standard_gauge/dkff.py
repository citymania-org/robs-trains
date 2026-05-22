import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_ff_PROPS = dict(
    length=9,
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
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_ff_1 = Train(
    **COMMON_ff_PROPS,
    id='dk_p_ff_1',
    name='DSB FF', #open ends
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1928, 1, 1),
    max_speed=Train.kmhish(100),
    cargo_capacity=78,
    weight=34,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 3rd class',
    }),
)

dk_p_ff_2 = Train(
    **COMMON_ff_PROPS,
    id='dk_p_ff_2',
    name='DSB CR', #closed ends
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1945, 1, 1),
    max_speed=Train.kmhish(100),
    cargo_capacity=78,
    weight=34,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

dk_p_ff_3 = Train(
    **COMMON_ff_PROPS,
    id='dk_p_ff_3',
    name='DSB CR', #open ends
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1955, 1, 1),
    max_speed=Train.kmhish(100),
    cargo_capacity=78,
    weight=34,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

dk_p_ff_4 = Train(
    **COMMON_ff_PROPS,
    id='dk_p_ff_4',
    name='DSB CR', #closed ends
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1955, 1, 1),
    max_speed=Train.kmhish(100),
    cargo_capacity=78,
    weight=34,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

dk_p_ff_5 = Train(
    **COMMON_ff_PROPS,
    id='dk_p_ff_5',
    name='DSB CRS', #closed ends
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1950, 1, 1),
    max_speed=Train.kmhish(100),
    cargo_capacity=78,
    weight=33,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class DVT',
    }),
)

dk_p_ff_6 = Train(
    **COMMON_ff_PROPS,
    id='dk_p_ff_6',
    name='DSB CRS', #closed ends
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1955, 1, 1),
    max_speed=Train.kmhish(100),
    cargo_capacity=78,
    weight=33,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class DVT',
    }),
)
