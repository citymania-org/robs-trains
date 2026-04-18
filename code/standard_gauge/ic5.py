import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_ic5_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    weight=270,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_p_ic5_1_dsb = Train(
    **COMMON_ic5_PROPS,
    id='d_p_ic5_1_dsb',
    name='DSB APO Lyntog Prototype (IC5)',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('bfsr',),
        paint=('bfs1r',),
        overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    purchase_sprite_towed_id='d_p_ic52_1_dsb',
    country='denmark',
    company='na',
    introduction_date=date(1981, 1, 1),
    power=1,
    callbacks={'properties': {'power': 0},},
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, basically a DVT on steroids',
        'Trivia': 'This is a prototype set, two were built, it was designed specifically to go on ferries between Danish islands but it was too long and too heavy. The findings from this experiment led to the much more successful IC3 and IR4',
    }),
).add_articulated_part(
    id='d_p_ic52_1_dsb',
    length=12,
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading='afm',
        paint='afm1',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic53_1_dsb',
    length=12,
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading='cfm',
        paint='cfm1',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic54_1_dsb',
    length=12,
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading='bfm',
        paint='bfm1',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic55_1_dsb',
    length=12,
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading='bfs',
        paint='bfs1',
        overlay='light',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_p_ic5_2_dsb = Train(
    **COMMON_ic5_PROPS,
    id='d_p_ic5_2_dsb',
    name='DSB APO Lyntog Prototype (IC5)',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('bfsr',),
        paint=('bfs1r',),
        overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='d_p_ic52_2_dsb',
    country='denmark',
    company='na',
    introduction_date=date(1988, 1, 1),
    power=1,
    callbacks={'properties': {'power': 0},},
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, basically a DVT on steroids',
        'Trivia': 'This is a prototype set, two were built, it was designed specifically to go on ferries between Danish islands but it was too long and too heavy. The findings from this experiment led to the much more successful IC3 and IR4',
    }),
).add_articulated_part(
    id='d_p_ic52_2_dsb',
    length=12,
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading='afm',
        paint='afm1',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic53_2_dsb',
    length=12,
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading='cfm',
        paint='cfm1',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic54_2_dsb',
    length=12,
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading='bfm',
        paint='bfm1',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic55_2_dsb',
    length=12,
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading='bfs',
        paint='bfs1',
        overlay='light',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_ic5a_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    weight=54,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_ic5a_1 = Train(
    **COMMON_ic5a_PROPS,
    id='dk_p_ic5a_1',
    name='DSB Afm',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('afm',),
        paint=('afm1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1981, 1, 1),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

dk_p_ic5a_2 = Train(
    **COMMON_ic5a_PROPS,
    id='dk_p_ic5a_2',
    name='DSB Afm',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('afm',),
        paint=('afm1',),
        cc_replace=colours["RED"],
        cc2_replace=colours['GREY1'],
    ),
    country='denmark',
    company='na',
    introduction_date=date(1988, 1, 1),
    cargo_capacity=60,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

dk_p_ic5a_3 = Train(
    **COMMON_ic5a_PROPS,
    id='dk_p_ic5a_3',
    name='DSB Bfm',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('bfm',),
        paint=('bfm1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1981, 1, 1),
    cargo_capacity=72,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

dk_p_ic5a_4 = Train(
    **COMMON_ic5a_PROPS,
    id='dk_p_ic5a_4',
    name='DSB Bfm',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('bfm',),
        paint=('bfm1',),
        cc_replace=colours["RED"],
        cc2_replace=colours['GREY1'],
    ),
    country='denmark',
    company='na',
    introduction_date=date(1988, 1, 1),
    cargo_capacity=72,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

dk_p_ic5a_5 = Train(
    **COMMON_ic5a_PROPS,
    id='dk_p_ic5a_5',
    name='DSB Cfm',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('cfm',),
        paint=('cfm1',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1981, 1, 1),
    cargo_capacity=22,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Kiosk car, 2nd class',
    }),
)

dk_p_ic5a_6 = Train(
    **COMMON_ic5a_PROPS,
    id='dk_p_ic5a_6',
    name='DSB Cfm',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('cfm',),
        paint=('cfm1',),
        cc_replace=colours["RED"],
        cc2_replace=colours['GREY1'],
    ),
    country='denmark',
    company='na',
    introduction_date=date(1988, 1, 1),
    cargo_capacity=22,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Kiosk car, 2nd class',
    }),
)

COMMON_ic5b_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=1,
    callbacks={'properties': {'power': 0},},
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    weight=54,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_ic5b_1 = Train(
    **COMMON_ic5b_PROPS,
    id='dk_p_ic5b_1',
    name='DSB Bfs',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('bfs',),
        paint=('bfs1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours['RED'],
    ),
    country='denmark',
    company='na',
    introduction_date=date(1981, 1, 1),
    cargo_capacity=74,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

dk_p_ic5b_2 = Train(
    **COMMON_ic5b_PROPS,
    id='dk_p_ic5b_2',
    name='DSB Bfs',
    liveries=make_psd_cc_liveries(
        'pp/ic5.psd',
        shading=('bfs',),
        paint=('bfs1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours['GREY1'],
    ),
    country='denmark',
    company='na',
    introduction_date=date(1988, 1, 1),
    cargo_capacity=74,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)
