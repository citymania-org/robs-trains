import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_mki_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=1000,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=122,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mki_1_dsb = Train(
    id='d_d_mki_1_dsb',
    **COMMON_mki_PROPS,
    name='DSB MK I',
    liveries=make_psd_cc_liveries(
        'pp/mki.psd',
        shading=('mki',),
        paint=('mkidsb1',),
        overlay=('mkilight'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    purchase_sprite_towed_id='d_d_fk_1_dsb',
    country='denmark',
    introduction_date=date(1943, 1, 1),
    cargo_capacity=58,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers & light freight',
    }),
).add_articulated_part(
    id='d_d_fk_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mki.psd',
        shading='fk',
        paint='fkdsb1',
        overlay='fklight',
        cc_replace=colours['MAROON'],
        cc2_replace=colours['MAROON'],
    ),
    cargo_capacity=58,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
