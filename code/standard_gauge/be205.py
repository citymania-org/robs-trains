import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_205_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 6),
    max_speed=Train.kmhish(120),
    power=1950,
    weight=110,
)

be_d_205_1 = Train(
    **COMMON_205_PROPS,
    id='be_d_205_1',
    name='NMBS HLD 205',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    country='belgium',
    company='na',
    introduction_date=date(1961, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Later classed as HLD 55',
    }),
)

lu_d_205_1 = Train(
    **COMMON_205_PROPS,
    id='lu_d_205_1',
    name='CFL 1800',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["YELLOW"]
    ),
    country='luxembourg',
    company='na',
    introduction_date=date(1963, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Used in Denmark from at least the mid 00s and Sweden from 2013',
    }),
)

dk_d_205_1 = Train(
    **COMMON_205_PROPS,
    id='dk_d_205_1',
    name='VIK 1800',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["YELLOW"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2023, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Several locomotives bought in 2023/5',
    }),
)

se_d_205_1 = Train(
    **COMMON_205_PROPS,
    id='se_d_205_1',
    name='STAB 1800',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["ORANGE"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2018, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought in 2013 #1802',
    }),
)
