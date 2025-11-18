import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_ic2_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(140),
    power=840,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=64,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_ic2_1_dsb = Train(
    id='d_d_ic2_1_dsb',
    **COMMON_ic2_PROPS,
    name='њMF (IC2)',
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    country='denmark',
    introduction_date=date(1997, 1, 1),
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'GDS, LJ, OHJ, VL, RTOG',
        'Trivia': 'All thirteen locomotives obtained by RTOG in 2009',
    }),
).add_articulated_part(
    id='d_d_ic22_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=62,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_ic2_2_dsb = Train( # AC units on roof
    id='d_d_ic2_2_dsb',
    **COMMON_ic2_PROPS,
    name='њMF (IC2)',
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    country='denmark',
    introduction_date=date(2013, 1, 1),
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'RTOG, LT',
        'Trivia': 'All thirteen locomotives obtained by LT in 2015',
    }),
).add_articulated_part(
    id='d_d_ic22_2_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=62,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
