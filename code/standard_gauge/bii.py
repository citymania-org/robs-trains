import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_b_ii_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_p_b_ii_1_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_b_ii_1_dsb',
    name='DSB B II',
    liveries=make_psd_cc_liveries(
        'pp/bii.psd',
        shading=('bii',),
        paint=('bii1',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2002, 1, 1),
    weight=50,
    cargo_capacity=110,
    loading_speed=10,
    power=0,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_b_ii_2_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_b_ii_2_dsb',
    name='DSB B II',
    liveries=make_psd_cc_liveries(
        'pp/bii.psd',
        shading=('bii',),
        paint=('bii2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2012, 1, 1),
    weight=50,
    cargo_capacity=110,
    loading_speed=10,
    power=0,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_b_ii_3_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_b_ii_3_dsb',
    name='DSB B II',
    liveries=make_psd_cc_liveries(
        'pp/bii.psd',
        shading=('bii',),
        paint=('bii3',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2023, 1, 1),
    weight=50,
    cargo_capacity=110,
    loading_speed=10,
    power=0,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
    }),
)

d_p_bk_iii_1_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_bk_iii_1_dsb',
    name='DSB Bk III',
    liveries=make_psd_cc_liveries(
        'pp/bii.psd',
        shading=('bk',),
        paint=('bk1',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2002, 1, 1),
    weight=50,
    cargo_capacity=102,
    loading_speed=10,
    power=0,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class with kiosk',
    }),
)

d_p_bk_iii_2_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_bk_iii_2_dsb',
    name='DSB Bk III',
    liveries=make_psd_cc_liveries(
        'pp/bii.psd',
        shading=('bk',),
        paint=('bk2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2012, 1, 1),
    weight=50,
    cargo_capacity=102,
    loading_speed=10,
    power=0,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class with kiosk',
    }),
)

d_p_bk_iii_3_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_bk_iii_3_dsb',
    name='DSB Bk III',
    liveries=make_psd_cc_liveries(
        'pp/bii.psd',
        shading=('bk',),
        paint=('bk3',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2023, 1, 1),
    weight=50,
    cargo_capacity=102,
    loading_speed=10,
    power=0,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class with kiosk',
    }),
)

d_p_abs_1_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_abs_1_dsb',
    name='њDSB ABs',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2002, 1, 1),
    weight=52,
    cargo_capacity=78,
    loading_speed=10,
    power=1,
    callbacks={'properties': {'power': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st & 2nd class DVT',
    }),
)

d_p_abs_2_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_abs_2_dsb',
    name='њDSB ABs',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2012, 1, 1),
    weight=52,
    cargo_capacity=78,
    loading_speed=10,
    power=1,
    callbacks={'properties': {'power': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st & 2nd class DVT',
    }),
)

d_p_abs_3_dsb = Train(
    **COMMON_b_ii_PROPS,
    id='d_p_abs_3_dsb',
    name='њDSB ABs',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["COLBALT"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2023, 1, 1),
    weight=52,
    cargo_capacity=78,
    loading_speed=10,
    power=1,
    callbacks={'properties': {'power': 0},},
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 1st & 2nd class DVT',
    }),
)
