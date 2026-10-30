import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_ma_PROPS = dict(
    length=8,
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
    max_speed=Train.kmhish(105),
    power=5384,
    weight=105,
)

se_e_ma_1 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_1',
    name='SJ Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('ma',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["GREY10"]
    ),
    company='na',
    introduction_date=date(1953, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_2 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_2',
    name='TGOJ Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('ma',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["MECONIUM"],
        cc2_replace=colours["YELLOW"]
    ),
    company='na',
    introduction_date=date(1953, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_3 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_3',
    name='TGOJ Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('ma',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(1968, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_4 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_4',
    name='SJ Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('mal',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["DBLUE"]
    ),
    company='na',
    introduction_date=date(1970, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_3l = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_3l',
    name='TGOJ Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('mal',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(1977, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_5 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_5',
    name='TGOJ Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('mal',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["APPLE"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    introduction_date=date(1996, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_6 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_6',
    name='BK Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('mal',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    introduction_date=date(1999, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_7 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_7',
    name='TGOJ Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('mal',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["APPLE"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    introduction_date=date(2001, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_8 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_8',
    name='NR Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('mal',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(2011, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_ma_9 = Train(
    **COMMON_ma_PROPS,
    id='se_e_ma_9',
    name='BJ Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('mal',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["ORANGE"]
    ),
    company='na',
    introduction_date=date(2019, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

no_e_ma_1 = Train(
    **COMMON_ma_PROPS,
    id='no_e_ma_1',
    name='NTA Ma',
    liveries=make_psd_cc_liveries(
        paint=('8b',),
        'pp/sema.psd',
        shading=('mal',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(2014, 1, 1),
    country='norway',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
