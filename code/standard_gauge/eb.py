import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv_15kv

COMMON_eb_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv/25kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_25kv_15kv,
    max_speed=Train.kmhish(200),
    power=8583,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=86,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_e_eb_1_dsb = Train(
    **COMMON_eb_PROPS,
    id='d_e_eb_1_dsb',
    name='DSB EB "Vectron"',
    liveries=make_psd_cc_liveries(
        'pp/eb.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2020, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_e_eb_2_dsb = Train(
    **COMMON_eb_PROPS,
    id='d_e_eb_2_dsb',
    name='DSB EB "Vectron"',
    liveries=make_psd_cc_liveries(
        'pp/eb.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2021, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
