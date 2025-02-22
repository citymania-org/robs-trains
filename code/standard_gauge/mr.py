import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_mr_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=636,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=70,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_1_dsb = Train(
    id='d_d_mr_1_dsb',
    **COMMON_mr_PROPS,
    name='њDSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb1',),
        overlay=('mrlight'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1978, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='d_d_mrd_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb1',
        overlay='mrdlight',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=48,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_2_dsb = Train(
    id='d_d_mr_2_dsb',
    **COMMON_mr_PROPS,
    name='њDSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb2',),
        overlay=('mrlight'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1994, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='d_d_mrd_2_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb2',
        overlay='mrdlight',
        cc_replace=colours['GREY1'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=48,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_3_dsb = Train(
    id='d_d_mr_3_dsb',
    **COMMON_mr_PROPS,
    name='њDSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb3',),
        overlay=('mrlight'),
        cc_replace=colours["GREY6"],
        cc2_replace=colours["COLBALT"]
    ),
    introduction_date=date(2004, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='d_d_mrd_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb3',
        overlay='mrdlight',
        cc_replace=colours['GREY6'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=48,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_4_dsb = Train(
    id='d_d_mr_4_dsb',
    **COMMON_mr_PROPS,
    name='њArriva MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb1',),
        overlay=('mrlight'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["TURQUOISE"]
    ),
    introduction_date=date(2003, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='d_d_mrd_4_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb1',
        overlay='mrdlight',
        cc_replace=colours['GREY1'],
        cc2_replace=colours['TURQUOISE'],
    ),
    cargo_capacity=48,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_5_dsb = Train(
    id='d_d_mr_5_dsb',
    **COMMON_mr_PROPS,
    name='њArriva MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb1',),
        overlay=('mrlight'),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["CREAM"]
    ),
    introduction_date=date(2005, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='d_d_mrd_5_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb1',
        overlay='mrdlight',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['CREAM'],
    ),
    cargo_capacity=48,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_6_dsb = Train(
    id='d_d_mr_6_dsb',
    **COMMON_mr_PROPS,
    name='њDSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb4',),
        overlay=('mrlight'),
        cc_replace=colours["GREY6"],
        cc2_replace=colours["COLBALT"]
    ),
    introduction_date=date(2012, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='d_d_mrd_6_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb4',
        overlay='mrdlight',
        cc_replace=colours['GREY6'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=48,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
