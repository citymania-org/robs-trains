import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_db103_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    power=9980,
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
)

de_e_db103_1_db = Train(
    id='de_e_db103_1_db',
    **COMMON_db103_PROPS,
    name='њDB 103',
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["DCREAM"]
    ),
    company='na',
    max_speed=Train.kmhish(200),
    weight=114,
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

de_e_db103_2_db = Train(
    id='de_e_db103_2_db',
    **COMMON_db103_PROPS,
    name='њDB 103 Orient Red',
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    max_speed=Train.kmhish(200),
    weight=114,
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

de_e_db103_3_db = Train(
    id='de_e_db103_3_db',
    **COMMON_db103_PROPS,
    name='њDB 103 Traffic Red',
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    max_speed=Train.kmhish(200),
    weight=114,
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

de_e_db103_4_radve = Train(
    id='de_e_db103_4_radve',
    **COMMON_db103_PROPS,
    name='њRADVE 103',
    liveries=make_psd_cc_liveries(
        'pp/9Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    max_speed=Train.kmhish(200),
    weight=114,
    introduction_date=date(2015, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
