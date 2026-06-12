import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_lint41_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    power=911,
    weight=67,
    cargo_capacity=65,
    loading_speed=10,
)

dk_d_lint41_1 = Train(
    id='dk_d_lint41_1',
    **COMMON_lint41_PROPS,
    purchase_sprite_towed_id='dk_d_lint412_1',
    name='Arriva AR 1001-2053',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["CREAM"]
    ),
    max_speed=Train.kmhish(120),
    country='denmark',
    company='na',
    introduction_date=date(2003, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'All passed to GCR',
    }),
).add_articulated_part(
    id='dk_d_lint412_1',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['CREAM'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_d_lint41_2 = Train(
    id='dk_d_lint41_2',
    **COMMON_lint41_PROPS,
    purchase_sprite_towed_id='dk_d_lint412_2',
    name='LB 101-127',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY7"]
    ),
    max_speed=Train.kmhish(120),
    country='denmark',
    company='na',
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'All passed to LT',
    }),
).add_articulated_part(
    id='dk_d_lint412_2',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY7'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_d_lint41_3 = Train(
    id='dk_d_lint41_3',
    **COMMON_lint41_PROPS,
    purchase_sprite_towed_id='dk_d_lint412_3',
    name='VL 2024-2032',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    max_speed=Train.kmhish(120),
    country='denmark',
    company='na',
    introduction_date=date(2007, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'All passed to RTOG and then LT',
    }),
).add_articulated_part(
    id='dk_d_lint412_3',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['RED'],
        cc2_replace=colours['DBLUE'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_d_lint41_4 = Train(
    id='dk_d_lint41_4',
    **COMMON_lint41_PROPS,
    purchase_sprite_towed_id='dk_d_lint412_4',
    name='NJJ LM',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["GREY1"]
    ),
    max_speed=Train.kmhish(140),
    country='denmark',
    company='na',
    introduction_date=date(2016, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='dk_d_lint412_4',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['COBALT'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_d_lint41_5 = Train(
    id='dk_d_lint41_5',
    **COMMON_lint41_PROPS,
    purchase_sprite_towed_id='dk_d_lint412_5',
    name='NJJ LM',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["SKY"]
    ),
    max_speed=Train.kmhish(140),
    country='denmark',
    company='na',
    introduction_date=date(2021, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='dk_d_lint412_5',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['COBALT'],
        cc2_replace=colours['SKY'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_d_lint41_6 = Train(
    id='dk_d_lint41_6',
    **COMMON_lint41_PROPS,
    purchase_sprite_towed_id='dk_d_lint412_6',
    name='GCR 2043',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(120),
    country='denmark',
    company='na',
    introduction_date=date(2024, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='dk_d_lint412_6',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['GREY3'],
        cc2_replace=colours['YELLOW'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
