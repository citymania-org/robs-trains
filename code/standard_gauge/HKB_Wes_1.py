import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro, standard_gauge_dc

COMMON_HKBw_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_dc,
    max_speed=Train.kmhish(35),
    power=252,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=164,
    loading_speed=5,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='norway',
)

n_o_Wes_1_hkb = Train(
    **COMMON_HKBw_PROPS,
    id='n_o_Wes_1_hkb',
    name='''HKB 'trunke' ''',
    liveries=make_psd_cc_liveries(
        'pp/1910_NO_Wes_1.psd',
        shading='Trunken',
        paint='HKB',
        overlay=('Lights',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    company='',
    introduction_date=date(1910, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'HKB',
        'Use': 'Holmenkollbanen',
        'Builder': 'Skabo',
        'Trivia': '''First heavy train stock for HKB. Previously they only used trams.''',
    }),
)
