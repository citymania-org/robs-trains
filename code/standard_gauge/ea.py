import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv

COMMON_ea_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='25kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_25kv,
    max_speed=Train.kmhish(175),
    power=5400,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=84,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_e_ea_1_dsb = Train(
    **COMMON_ea_PROPS,
    id='d_e_ea_1_dsb',
    name='DSB EA',
    liveries=make_psd_cc_liveries(
        'pp/ea.psd',
        shading=('ea',),
        paint=('dsb1',),
        overlay=('light', 'leccy'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's first electric locomotive''',
    }),
)

d_e_ea_2_dsb = Train(
    **COMMON_ea_PROPS,
    id='d_e_ea_2_dsb',
    name='DSB EA',
    liveries=make_psd_cc_liveries(
        'pp/ea.psd',
        shading=('ea',),
        paint=('dsb2',),
        overlay=('light', 'leccy'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_e_ea_3_dsb = Train(
    **COMMON_ea_PROPS,
    id='d_e_ea_3_dsb',
    name='DSB EA',
    liveries=make_psd_cc_liveries(
        'pp/ea.psd',
        shading=('ea',),
        paint=('dsb3',),
        overlay=('light', 'leccy'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2017, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_e_ea_4_bulmarket = Train(
    **COMMON_ea_PROPS,
    id='d_e_ea_4_bulmarket',
    name='Bulmarket EA',
    liveries=make_psd_cc_liveries(
        'pp/ea.psd',
        shading=('ea',),
        paint=('bulmarket1',),
        overlay=('light', 'leccy'),
        cc_replace=colours["RED"],
        cc2_replace=colours["BLUE"]
    ),
    country='na',
    company='na',
    introduction_date=date(2007, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
        'Trivia': 'Some locos sold to Bulmarket in 2007 for liquified gas trains',
    }),
)

d_e_ea_5_db = Train(
    **COMMON_ea_PROPS,
    id='d_e_ea_5_db',
    name='DB Schenker Bulgaria EA',
    liveries=make_psd_cc_liveries(
        'pp/ea.psd',
        shading=('ea',),
        paint=('db1',),
        overlay=('light', 'leccy'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='na',
    company='na',
    introduction_date=date(2010, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
        'Trivia': 'Some locos sold to DB Schenker Bulgaria in 2010',
    }),
)
