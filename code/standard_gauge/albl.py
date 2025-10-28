import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_albl_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    max_speed=Train.kmhish(140),
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

# al

d_p_al_1_dsb = Train(
    **COMMON_albl_PROPS,
    id='d_p_al_1_dsb',
    name='DSB AL',
    liveries=make_psd_cc_liveries(
        'pp/albl.psd',
        shading=('al',),
        paint=('old1',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1958, 1, 1),
    weight=35,
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

d_p_al_2_dsb = Train(
    **COMMON_albl_PROPS,
    id='d_p_al_2_dsb',
    name='DSB Bfh',
    liveries=make_psd_cc_liveries(
        'pp/albl.psd',
        shading=('al',),
        paint=('old',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_al_3_dsb = Train(
    **COMMON_albl_PROPS,
    id='d_p_al_3_dsb',
    name='DSB Bfh',
    liveries=make_psd_cc_liveries(
        'pp/albl.psd',
        shading=('al',),
        paint=('new',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=37,
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_al_4_dsb = Train(
    **COMMON_albl_PROPS,
    id='d_p_al_4_dsb',
    name='DSB Af',
    liveries=make_psd_cc_liveries(
        'pp/albl.psd',
        shading=('al',),
        paint=('new1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1985, 1, 1),
    weight=36,
    cargo_capacity=42,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

d_p_al_5_dsb = Train(
    **COMMON_albl_PROPS,
    id='d_p_al_5_dsb',
    name='NSB B6',
    liveries=make_psd_cc_liveries(
        'pp/albl.psd',
        shading=('al',),
        paint=('nsb1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='norway',
    company='na',
    introduction_date=date(1991, 1, 1),
    weight=36,
    cargo_capacity=42,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

# bl

d_p_bl_1_dsb = Train(
    **COMMON_albl_PROPS,
    id='d_p_bl_1_dsb',
    name='DSB BL',
    liveries=make_psd_cc_liveries(
        'pp/albl.psd',
        shading=('bl',),
        paint=('old',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1959, 1, 1),
    weight=34,
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_bl_2_dsb = Train(
    **COMMON_albl_PROPS,
    id='d_p_bl_2_dsb',
    name='DSB Bf',
    liveries=make_psd_cc_liveries(
        'pp/albl.psd',
        shading=('bl',),
        paint=('new',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=34,
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_bl_3_dsb = Train(
    **COMMON_albl_PROPS,
    id='d_p_bl_3_dsb',
    name='OHJ Bf',
    liveries=make_psd_cc_liveries(
        'pp/albl.psd',
        shading=('bl',),
        paint=('ohj1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1993, 1, 1),
    weight=34,
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)
