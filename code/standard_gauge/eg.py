import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv_15kv

COMMON_eg_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv/25kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_25kv_15kv,
    max_speed=Train.kmhish(140),
    power=8717,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=132,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_e_eg_1_dsb = Train(
    **COMMON_eg_PROPS,
    id='d_e_eg_1_dsb',
    name='њDSB EG',
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)

d_e_eg_2_dsb = Train(
    **COMMON_eg_PROPS,
    id='d_e_eg_2_dsb',
    name='њRSC EG',
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2010, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
        'Trivia': 'All thirteen locomotives bought from RDK in 2009',
    }),
)

d_e_eg_3_dsb = Train(
    **COMMON_eg_PROPS,
    id='d_e_eg_3_dsb',
    name='њDBCSC EG',
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2019, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
        'Trivia': 'All thirteen locomotives bought from RSC in 2016',
    }),
)
