import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge_15kv, standard_gauge

COMMON_XOA4_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    power=500,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=46,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=75,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
    mid_stats={
        'cargo_capacity': 1,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

se_e_Xa_1 = Train(
    **COMMON_XOA4_PROPS,
    id='se_e_Xa_1',
    name='њDJ Xa',
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Xoa4.psd',
        shading='Xoa4',
        paint='sj/dj_original',
        overlay=('Lights', 'Electrical equipment'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    max_speed=Train.kmhish(120),
    introduction_date=date(1939, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 3rd class',
        'Trivia': '''Was geared for higher speeds to gain experience for the acquisition of BJ's GDG-Expressen; BJ XoA, later SJ Xoa8'''
    }),
)

s_e_Xoa4_1_sj = Train(
    **COMMON_XOA4_PROPS,
    id='s_e_Xoa4_1_sj',
    name='њSJ Xoa4',
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Xoa4.psd',
        shading='Xoa4',
        paint='sj/dj_original',
        overlay=('Lights', 'Electrical equipment'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    max_speed=Train.kmhish(90),
    introduction_date=date(1939, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 3rd class',
        'Trivia': 'Cox4 and Co6 were usually sanwhiched between the multiple units'
    }),
)

s_e_Xoa4_2_sj = Train(
    **COMMON_XOA4_PROPS,
    id='s_e_Xoa4_2_sj',
    name='њSJ Xoa4',
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Xoa4.psd',
        shading='Xoa4',
        paint='sj_brown',
        overlay=('Lights', 'Electrical equipment'),
        cc_replace=colours["REDBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    company='na',
    max_speed=Train.kmhish(90),
    introduction_date=date(1944, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 3rd class',
    }),
)

COMMON_COX4_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=34,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=95,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_Cox4_1_sj = Train(
    **COMMON_COX4_PROPS,
    id='s_e_Cox4_1_sj',
    name='њSJ Cox4',
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Cox4.psd',
        shading='Cox4',
        paint='sj/dj_original',
        overlay='Lights',
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1939, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 3rd class',
    }),
)

s_e_Cox4_2_sj = Train(
    **COMMON_COX4_PROPS,
    id='s_e_Cox4_2_sj',
    name='њSJ Cox4',
    liveries=make_psd_cc_liveries(
        'pp/1939_SE_Cox4.psd',
        shading='Cox4',
        paint='sj_brown',
        overlay='Lights',
        cc_replace=colours["REDBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    company='na',
    introduction_date=date(1944, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 3rd class',
    }),
)

COMMON_XmCDFo_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=34,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=54,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
    
)

se_p_XmCDFo_1 = Train(
    **COMMON_XmCDFo_PROPS,
    id='se_w_XmCDFo_1',
    name='њDJ XmCDFo',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1944, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 3rd class',
    }),
)

se_p_XmCDFo_2 = Train(
    **COMMON_XmCDFo_PROPS,
    id='se_w_XmCDFo_2',
    name='њSJ CDFox4',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours["REDBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    company='na',
    introduction_date=date(1948, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 3rd class',
    }),
)
