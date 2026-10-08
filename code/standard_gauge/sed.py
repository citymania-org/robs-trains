import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_d_PROPS = dict(
    length=6,
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
    country='sweden',
)

se_e_d_1 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_1',
    name='SJ Ds',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    max_speed=Train.kmhish(90),
    power=1659,
    weight=80,
    company='na',
    introduction_date=date(1925, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_2 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_2',
    name='SJ Dg',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    max_speed=Train.kmhish(70),
    power=1659,
    weight=80,
    company='na',
    introduction_date=date(1925, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_3 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_3',
    name='SJ Ds',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    max_speed=Train.kmhish(90),
    power=1659,
    weight=80,
    company='na',
    introduction_date=date(1933, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_4 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_4',
    name='SJ Dg',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    max_speed=Train.kmhish(70),
    power=1659,
    weight=80,
    company='na',
    introduction_date=date(1933, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_5 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_5',
    name='SJ Dk',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    max_speed=Train.kmhish(100),
    power=1999,
    weight=80,
    company='na',
    introduction_date=date(1936, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_6 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_6',
    name='SJ Dk',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    max_speed=Train.kmhish(100),
    power=1999,
    weight=80,
    company='na',
    introduction_date=date(1936, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_7 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_7',
    name='SJ Dg',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    max_speed=Train.kmhish(75),
    power=1659,
    weight=80,
    company='na',
    introduction_date=date(1936, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_8 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_8',
    name='SJ Dg',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    max_speed=Train.kmhish(75),
    power=1659,
    weight=80,
    company='na',
    introduction_date=date(1936, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_9 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_9',
    name='SJ Du',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    max_speed=Train.kmhish(100),
    power=2502,
    weight=80,
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_d_10 = Train(
    **COMMON_d_PROPS,
    id='se_e_d_10',
    name='SJ Du',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    max_speed=Train.kmhish(100),
    power=2502,
    weight=80,
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
