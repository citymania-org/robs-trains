import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_rc_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    power=4828,
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

s_e_rc1245_1_sj = Train(
    id='s_e_rc1245_1_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc1/2/4/5',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    max_speed=Train.kmhish(135),
    weight=76,
    introduction_date=date(1967, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc1245_2_sj = Train(
    id='s_e_rc1245_2_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc1/2/4/5',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(135),
    weight=76,
    introduction_date=date(1990, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc1245_3_sj = Train(
    id='s_e_rc1245_3_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc1/2', #this is the rc one
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(135),
    weight=76,
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc1245_4_sj = Train(
    id='s_e_rc1245_4_sj',
    **COMMON_rc_PROPS,
    name='њGC Rc2/4',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREY7"]
    ),
    company='na',
    max_speed=Train.kmhish(135),
    weight=76,
    introduction_date=date(2001, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc1245_5_sj = Train(
    id='s_e_rc1245_5_sj',
    **COMMON_rc_PROPS,
    name='њTÅGAB Rc2',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(135),
    weight=76,
    introduction_date=date(2001, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc1245_6_sj = Train(
    id='s_e_rc1245_6_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc5',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    max_speed=Train.kmhish(135),
    weight=76,
    introduction_date=date(1986, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc36_1_sj = Train(
    id='s_e_rc36_1_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc3/6',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    max_speed=Train.kmhish(160),
    weight=76,
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc36_2_sj = Train(
    id='s_e_rc36_2_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc3/6',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(160),
    weight=76,
    introduction_date=date(1990, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc36_3_sj = Train(
    id='s_e_rc36_3_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc6',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(160),
    weight=76,
    introduction_date=date(2003, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc36_4_sj = Train(
    id='s_e_rc36_4_sj',
    **COMMON_rc_PROPS,
    name='њSSRT Rc3/6',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["GREY9"]
    ),
    company='na',
    max_speed=Train.kmhish(160),
    weight=76,
    introduction_date=date(2005, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc36_5_sj = Train(
    id='s_e_rc36_5_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc3/6',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    company='na',
    max_speed=Train.kmhish(160),
    weight=76,
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc36_6_sj = Train(
    id='s_e_rc36_6_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc6',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["GREY10"]
    ),
    company='na',
    max_speed=Train.kmhish(160),
    weight=76,
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc36_7_sj = Train(
    id='s_e_rc36_7_sj',
    **COMMON_rc_PROPS,
    name='њHCTOR Rc3',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["ORANGE"]
    ),
    company='na',
    max_speed=Train.kmhish(160),
    weight=76,
    introduction_date=date(2014, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

s_e_rc7_1_sj = Train(
    id='s_e_rc7_1_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rc7',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(180),
    weight=76,
    introduction_date=date(2001, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
)

s_e_rm_1_sj = Train(
    id='s_e_rm_1_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rm',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    max_speed=Train.kmhish(100),
    weight=90,
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)

s_e_rm_2_sj = Train(
    id='s_e_rm_2_sj',
    **COMMON_rc_PROPS,
    name='њSJ Rm',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(100),
    weight=90,
    introduction_date=date(1990, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)

s_e_rm_3_sj = Train(
    id='s_e_rm_3_sj',
    **COMMON_rc_PROPS,
    name='њGC Rm',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(100),
    weight=90,
    introduction_date=date(2001, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)

s_e_rm_4_sj = Train(
    id='s_e_rm_4_sj',
    **COMMON_rc_PROPS,
    name='њTÅGAB Rm',
    liveries=make_psd_cc_liveries(
        'pp/7Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["RED"]
    ),
    company='na',
    max_speed=Train.kmhish(100),
    weight=90,
    introduction_date=date(2023, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)
