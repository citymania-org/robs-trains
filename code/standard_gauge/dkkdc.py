import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_kdc_PROPS = dict(
    length=4,
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

dk_s_di_1 = Train(
    **COMMON_kdc_PROPS,
    id='dk_s_di_1',
    purchase_sprite_towed_id='dk_s_di2_1',
    name='DSB D I-III',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(60),
    power=610,
    weight=72,
    country='denmark',
    company='na',
    introduction_date=date(1902, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
).add_articulated_part(
    id='dk_s_di2_1',
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='3a',
        paint='3b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_di_2 = Train(
    **COMMON_kdc_PROPS,
    id='dk_s_di_2',
    purchase_sprite_towed_id='dk_s_di2_2',
    name='DSB D IV',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(70),
    power=640,
    weight=75,
    country='denmark',
    company='na',
    introduction_date=date(1925, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
).add_articulated_part(
    id='dk_s_di2_2',
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='3a',
        paint='3b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_k_1 = Train(
    **COMMON_kdc_PROPS,
    id='dk_s_k_1',
    purchase_sprite_towed_id='dk_s_k2_1',
    name='DSB K',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(90),
    power=525,
    weight=69,
    country='denmark',
    company='na',
    introduction_date=date(1894, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='dk_s_k2_1',
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='3a',
        paint='3b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_k_2 = Train(
    **COMMON_kdc_PROPS,
    id='dk_s_k_2',
    purchase_sprite_towed_id='dk_s_k2_2',
    name='DSB K',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(100),
    power=525,
    weight=72,
    country='denmark',
    company='na',
    introduction_date=date(1925, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='dk_s_k2_2',
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='3a',
        paint='3b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

dk_s_cii_1 = Train(
    **COMMON_kdc_PROPS,
    id='dk_s_cii_1',
    purchase_sprite_towed_id='dk_s_cii2_1',
    name='DSB C II',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    max_speed=Train.kmhish(100),
    power=550,
    weight=69,
    country='denmark',
    company='na',
    introduction_date=date(1903, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Express passengers',
    }),
).add_articulated_part(
    id='dk_s_cii2_1',
    length=3,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='3a',
        paint='3b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)
