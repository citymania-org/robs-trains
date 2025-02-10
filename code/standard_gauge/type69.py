import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_type69_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(130),
    power=1632,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=108,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=158,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='norway',
)

n_o_BM69A_1_nsb = Train(
    **COMMON_type69_PROPS,
    id='n_o_BM69A_1_nsb',
    name='NSB Type 69A',
    liveries=make_psd_cc_liveries(
        'pp/1970_NO_BM69A.psd',
        shading='BM69A',
        paint='NSB_1',
        overlay=('Lights', 'Roof shading',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["YELLOW"]
    ),
    company='na',
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'NSB',
        'Use': 'Commuter trains',
        'Builder': 'Strømmen',
    }),
).add_articulated_part(
    id='n_o_BS69A_1_nsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/1970_NO_BS69A.psd',
        shading='BS69A',
        paint='NSB_1',
        overlay=['Lights', 'Roof shading',],
        cc_replace=colours['MAROON'],
        cc2_replace=colours['YELLOW'],
    ),
    cargo_capacity=158,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

n_o_BM69A_2_nsb = Train(
    **COMMON_type69_PROPS,
    id='n_o_BM69A_2_nsb',
    name='NSB Type 69A',
    liveries=make_psd_cc_liveries(
        'pp/1970_NO_BM69A.psd',
        shading='BM69A',
        paint='NSB_2',
        overlay=('Lights',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    company='na',
    introduction_date=date(1985, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'NSB',
        'Use': 'Commuter trains',
        'Builder': 'Strømmen',
    }),
).add_articulated_part(
    id='n_o_BS69A_2_nsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/1970_NO_BS69A.psd',
        shading='BS69A',
        paint='NSB_2',
        overlay=['Lights',],
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY10'],
    ),
    cargo_capacity=158,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

n_o_BM69A_3_nsb = Train(
    **COMMON_type69_PROPS,
    id='n_o_BM69A_3_nsb',
    name='NSB Type 69A',
    liveries=make_psd_cc_liveries(
        'pp/1970_NO_BM69A.psd',
        shading='BM69A',
        paint='NSB_3',
        overlay=('Lights', 'Roof shading',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY5"]
    ),
    company='na',
    introduction_date=date(2005, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'NSB',
        'Use': 'Commuter trains',
        'Builder': 'Strømmen',
    }),
).add_articulated_part(
    id='n_o_BS69A_3_nsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/1970_NO_BS69A.psd',
        shading='BS69A',
        paint='NSB_3',
        overlay=['Lights', 'Roof shading',],
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY5'],
    ),
    cargo_capacity=158,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
