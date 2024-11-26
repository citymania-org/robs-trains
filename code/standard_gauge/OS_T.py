import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro, standard_gauge_1500v

COMMON_T_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(60),
    power=400,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=164,
    loading_speed=20,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='norway',
)

n_o_T_1_os = Train(
    **COMMON_T_PROPS,
    id='n_o_T_1_os',
    name='њOS T',
    liveries=make_psd_cc_liveries(
        'pp/1959_NO_T.psd',
        shading='T',
        paint='OS',
        overlay=('Lights',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    introduction_date=date(1959, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'os',
        'Use': 'Oslo light rail',
        'Builder': 'Strømmen',
        'Trivia': '''Metro train prototype.''',
    }),
)

n_o_T_2_os = Train(
    **COMMON_T_PROPS,
    id='n_o_T_2_os',
    name='њOS T',
    liveries=make_psd_cc_liveries(
        'pp/1959_NO_T.psd',
        shading='T',
        paint='OS',
        overlay=('Lights', 'Window',),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'os',
        'Use': 'Oslo light rail',
        'Builder': 'Strømmen',
        'Trivia': '''Metro train prototype transferred to the Kolsås line.''',
    }),
)
