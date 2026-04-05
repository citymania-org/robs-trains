import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_44_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(125),
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

ch_e_re44i_1 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44i_1',
    name='SBB Re 4/4 I series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    weight=56,
    power=2515,
    introduction_date=date(1946, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44i_2 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44i_2',
    name='SBB Re 4/4 I series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["COLBALT"]
    ),
    country='switzerland',
    company='na',
    weight=56,
    power=2515,
    introduction_date=date(1956, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44i_3 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44i_3',
    name='SBB Re 4/4 I series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    weight=56,
    power=2515,
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44i_4 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44i_4',
    name='SBB Re 4/4 I series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    country='switzerland',
    company='na',
    weight=57,
    power=2583,
    introduction_date=date(1949, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

ch_e_re44i_5 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44i_5',
    name='SBB Re 4/4 I series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["DCREAM"]
    ),
    country='switzerland',
    company='na',
    weight=57,
    power=2583,
    introduction_date=date(1972, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers',
        'Trivia': 'Used on the TEE',
    }),
)

ch_e_re44i_6 = Train(
    **COMMON_44_PROPS,
    id='ch_e_re44i_6',
    name='SBB Re 4/4 I series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a',),
        paint=('7b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY5"]
    ),
    country='switzerland',
    company='na',
    weight=57,
    power=2583,
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
