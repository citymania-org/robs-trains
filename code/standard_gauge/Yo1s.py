import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_Yo1s_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=155,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=13,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=48,
    loading_speed=5,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_d_Yo1s_1_sj = Train(
    **COMMON_Yo1s_PROPS,
    id='s_d_Yo1s_1_sj',
    name='SJ Yo1s',
    liveries=make_psd_cc_liveries(
        'pp/1946_SE_Yo1s.psd',
        shading='Yo1s',
        paint='SJ',
        overlay=('Lights', 'Details'),
        cc_replace=colours["CREAM"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1946, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SJ',
        'Use': 'Local trains, 3rd class',
        'Builder': 'Hilding Carlsson',
        'Trivia': '''Larger post-war variant of the HC railbus with more spacious interior''',
    }),
)
s_d_Yo1s_2_bj = Train(
    **COMMON_Yo1s_PROPS,
    id='s_d_Yo1s_2_bj',
    name='BJ Yo8',
    liveries=make_psd_cc_liveries(
        'pp/1946_SE_Yo1s.psd',
        shading='Yo1s',
        paint='BJ',
        overlay=('Lights', 'Details'),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1947, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'BJ',
        'Use': 'Local trains, 3rd class',
        'Builder': 'Hilding Carlsson'
    }),
)
s_d_Yo1s_3_tgoj = Train(
    **COMMON_Yo1s_PROPS,
    id='s_d_Yo1s_3_tgoj',
    name='TGOJ Yo8',
    liveries=make_psd_cc_liveries(
        'pp/1946_SE_Yo1s.psd',
        shading='Yo1s',
        paint='TGOJ_new',
        overlay=('Lights', 'Details'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["CREAM"]
    ),
    company='na',
    introduction_date=date(1947, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'TGOJ',
        'Use': 'Local trains, 3rd class',
        'Builder': 'Hilding Carlsson'
    }),
)
