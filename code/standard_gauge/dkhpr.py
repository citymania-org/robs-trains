import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_hpr_PROPS = dict(
    length=5,
    misc_flags=Train.Flags.USE_2CC,
    power_type='steam',
    engine_class=Train.EngineClass.STEAM, 
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
)

dk_s_pii_1 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_pii_1',
    purchase_sprite_towed_id='dk_s_pii2_1',
    name='DSB P II',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(120),
    power=1250,
    weight=117,
    country='denmark',
    company='na',
    introduction_date=date(1907, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='dk_s_pii2_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_hi_1 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_hi_1',
    purchase_sprite_towed_id='dk_s_hi2_1',
    name='DSB H I',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(70),
    power=1185,
    weight=129,
    country='denmark',
    company='na',
    introduction_date=date(1923, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
).add_articulated_part(
    id='dk_s_hi2_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_hii_1 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_hii_1',
    purchase_sprite_towed_id='dk_s_hii2_1',
    name='DSB H II',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(80),
    power=1185,
    weight=138,
    country='denmark',
    company='na',
    introduction_date=date(1941, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
).add_articulated_part(
    id='dk_s_hii2_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_hii_2 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_hii_2',
    purchase_sprite_towed_id='dk_s_hii2_2',
    name='DSB H II', #steam things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(80),
    power=1185,
    weight=138,
    country='denmark',
    company='na',
    introduction_date=date(1950, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
).add_articulated_part(
    id='dk_s_hii2_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_pr_1 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_pr_1',
    purchase_sprite_towed_id='dk_s_pr2_1',
    name='DSB PR',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(100),
    power=1500,
    weight=131,
    country='denmark',
    company='na',
    introduction_date=date(1943, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='dk_s_pr2_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_ri_1 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_ri_1',
    purchase_sprite_towed_id='dk_s_ri2_1',
    name='DSB R I',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(100),
    power=1160,
    weight=118,
    country='denmark',
    company='na',
    introduction_date=date(1912, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='dk_s_ri2_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_ri_2 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_ri_2',
    purchase_sprite_towed_id='dk_s_ri2_2',
    name='DSB R I', #steam things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(100),
    power=1160,
    weight=118,
    country='denmark',
    company='na',
    introduction_date=date(1933, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='dk_s_ri2_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_rii_1 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_rii_1',
    purchase_sprite_towed_id='dk_s_rii2_1',
    name='DSB R II',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(100),
    power=1150,
    weight=122,
    country='denmark',
    company='na',
    introduction_date=date(1921, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='dk_s_rii2_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_rii_2 = Train(
    **COMMON_hpr_PROPS,
    id='dk_s_rii_2',
    purchase_sprite_towed_id='dk_s_rii2_2',
    name='DSB R II', #steam things
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(100),
    power=1150,
    weight=122,
    country='denmark',
    company='na',
    introduction_date=date(1933, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='dk_s_rii2_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)
