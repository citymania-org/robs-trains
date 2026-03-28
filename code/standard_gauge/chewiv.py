import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_ew_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_p_ewiv_1 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_1',
    name='SBB A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1981, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=60,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

ch_p_ewiv_2 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_2',
    name='SBB A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2000, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=60,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

ch_p_ewiv_3 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_3',
    name='SBB A',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2021, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=60,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

ch_p_ewiv_4 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_4',
    name='SBB B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1983, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=86,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

ch_p_ewiv_5 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_5',
    name='SBB B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2000, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=86,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

ch_p_ewiv_6 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_6',
    name='SBB B',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2021, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=86,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

COMMON_ews_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=1,
    callbacks={'properties': {'power': 0},},
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

ch_p_ewiv_7 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewiv_7',
    name='SBB Bt',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1996, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=62,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

ch_p_ewiv_8 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewiv_8',
    name='SBB Bt',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2000, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=62,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

ch_p_ewiv_9 = Train(
    **COMMON_ews_PROPS,
    id='ch_p_ewiv_9',
    name='SBB Bt',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2021, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=62,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)
