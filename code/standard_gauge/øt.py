import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv_15kv

COMMON_et_PROPS = dict(
    length=11,
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='15kv/25kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_25kv_15kv,
    max_speed=Train.kmhish(180),
    power=2843,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=156,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_et_1_dsb = Train(
    id='d_e_et_1_dsb',
    **COMMON_et_PROPS,
    name='њSJ X31K/DSB ET (Øresundståg)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["DPURPLE"]
    ),
    introduction_date=date(2000, 1, 1),
    cargo_capacity=86,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, up to 5 Øresundståg can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_e_et2_1_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['DPURPLE'],
    ),
    cargo_capacity=58,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_et3_1_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['DPURPLE'],
    ),
    cargo_capacity=79,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_et_2_dsb = Train(
    id='d_e_et_2_dsb',
    **COMMON_et_PROPS,
    name='њSJ X31K/DSB ET (Øresundståg)',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["GREY9"]
    ),
    introduction_date=date(2018, 1, 1),
    cargo_capacity=86,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, up to 5 Øresundståg can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_e_et2_2_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['GREY9'],
    ),
    cargo_capacity=58,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_et3_2_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['GREY9'],
    ),
    cargo_capacity=79,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
