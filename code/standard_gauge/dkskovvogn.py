import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_skovvogn_PROPS = dict(
    length=5,
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
    max_speed=Train.kmhish(60),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_skovvogn_1 = Train(
    **COMMON_skovvogn_PROPS,
    id='dk_p_skovvogn_1',
    name='SJS Cc',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1880, 1, 1),
    cargo_capacity=40,
    weight=10,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)

dk_p_skovvogn_2 = Train(
    **COMMON_skovvogn_PROPS,
    id='dk_p_skovvogn_2',
    name='DSB CE I',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1893, 1, 1),
    cargo_capacity=40,
    weight=10,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)

dk_p_skovvogn_3 = Train(
    **COMMON_skovvogn_PROPS,
    id='dk_p_skovvogn_3',
    name='KSB Cc 1/2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["APPLE"],
        cc2_replace=colours["APPLE"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1905, 1, 1),
    cargo_capacity=50,
    weight=9,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)

dk_p_skovvogn_4 = Train(
    **COMMON_skovvogn_PROPS,
    id='dk_p_skovvogn_4',
    name='AB C 1/2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1907, 1, 1),
    cargo_capacity=50,
    weight=10,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)
