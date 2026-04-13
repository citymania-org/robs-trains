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
    loading_speed=10,
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
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

ch_p_ewiv_20 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_20',
    name='BLS A', #these didnt have DVT so cc2 can be elsewhere
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1985, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
        'Trivia': 'Later obtained by SBB in 2004',
    }),
)

ch_p_ewiv_21 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_21',
    name='A', #these didnt have DVT so cc2 can be elsewhere
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["CREAM"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1990, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
        'Owners': 'BT, SOB',
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
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

ch_p_ewiv_22 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_22',
    name='BLS B', #these didnt have DVT so cc2 can be elsewhere
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1985, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=86,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
        'Trivia': 'Later obtained by SBB in 2004',
    }),
)

ch_p_ewiv_23 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_23',
    name='B', #these didnt have DVT so cc2 can be elsewhere
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["CREAM"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1990, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=86,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
        'Owners': 'BT, SOB',
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
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

ch_p_ewiv_10 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_10',
    name='SBB WR', #88-73 000-003
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1983, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_11 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_11',
    name='SBB WR', #88-73 100-116
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1988, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_12 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_12',
    name='SBB WRm', #88-94 000-003
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["DPURPLE"],
        cc2_replace=colours["MAGENTA"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1991, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_13 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_13',
    name='SBB WR', #mcdo
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1992, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_14 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_14',
    name='SBB WRm', #88-94 000-003
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["DPURPLE"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1996, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_15 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_15',
    name='SBB S', #coop
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2000, 1, 1),
    max_speed=Train.kmhish(160),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_16 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_16',
    name='SBB WRm', #88-94.1
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2000, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_17 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_17',
    name='SBB WRm', #88-94 000-003
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["DPURPLE"],
        cc2_replace=colours["GREY1"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2002, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_18 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_18',
    name='SBB WRm', #88-94.1
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2011, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
    }),
)

ch_p_ewiv_19 = Train(
    **COMMON_ew_PROPS,
    id='ch_p_ewiv_19',
    name='SRCM WRm', #srcm
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["LAVENDER"],
        cc2_replace=colours["LAVENDER"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(2014, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=1,
    callbacks={'properties': {'cargo_capacity': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Restaurant carriage',
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
    loading_speed=10,
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
        cc_replace=colours["RED"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    introduction_date=date(1996, 1, 1),
    max_speed=Train.kmhish(200),
    cargo_capacity=62,
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
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)
