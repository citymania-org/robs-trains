import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_guage_3kv

COMMON_444_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='dc3000',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_guage_3kv,
    max_speed=Train.kmhish(200),
    power=5808,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=83,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

it_e_444_1 = Train(
    **COMMON_444_PROPS,
    id='it_e_444_1',
    name='FS E.444',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
)

it_e_444_2 = Train(
    **COMMON_444_PROPS,
    id='it_e_444_2',
    name='FS E.444', #red buffers
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    introduction_date=date(1973, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
)

COMMON_444r_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='dc3000',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_guage_3kv,
    max_speed=Train.kmhish(200),
    power=5808,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=84,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

it_e_444r_1 = Train(
    **COMMON_444r_PROPS,
    id='it_e_444r_1',
    name='FS E.444R',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    introduction_date=date(1989, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
)

it_e_444r_2 = Train(
    **COMMON_444r_PROPS,
    id='it_e_444r_2',
    name='FS E.444R',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
)

it_e_444r_3 = Train(
    **COMMON_444r_PROPS,
    id='it_e_444r_3',
    name='FS E.444R',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["GREY4"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
)
