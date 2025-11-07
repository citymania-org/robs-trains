import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_ic5_PROPS = dict(
    length=11,
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
    name='њDSB IC5',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1981, 1, 1),
    power=0,
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, basically a DVT on steroids',
        'Trivia': 'This is a prototype set, two were built, it was designed specifically to go on ferries between Danish islands but it was too long and too heavy. The findings from this experiment led to the much more successful IC3 and IR4',
    }),
).add_articulated_part(
    id='d_p_ic52_1_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic53_1_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic54_1_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic55_1_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
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
    name='њDSB IC5',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1988, 1, 1),
    power=0,
    cargo_capacity=62,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, basically a DVT on steroids',
        'Trivia': 'This is a prototype set, two were built, it was designed specifically to go on ferries between Danish islands but it was too long and too heavy. The findings from this experiment led to the much more successful IC3 and IR4',
    }),
).add_articulated_part(
    id='d_p_ic52_2_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic53_2_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic54_2_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic55_2_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_p_ic5_3_dsb = Train(
    **COMMON_ic5_PROPS,
    id='d_p_ic5_3_dsb',
    name='њDSB IC5',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1981, 1, 1),
    power=1,
    cargo_capacity=62,
    visual_effect=(Train.VisualEffect.DISABLE, 7),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, basically a DVT on steroids',
        'Trivia': 'USE AT OWN RISK',
    }),
).add_articulated_part(
    id='d_p_ic52_3_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic53_3_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic54_3_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic55_3_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_p_ic5_4_dsb = Train(
    **COMMON_ic5_PROPS,
    id='d_p_ic5_4_dsb',
    name='њDSB IC5',
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1988, 1, 1),
    power=1,
    cargo_capacity=62,
    visual_effect=(Train.VisualEffect.DISABLE, 7),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Intercity passengers, basically a DVT on steroids',
        'Trivia': 'USE AT OWN RISK',
    }),
).add_articulated_part(
    id='d_p_ic52_4_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic53_4_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic54_4_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_p_ic55_4_dsb',
    length=11,
    liveries=make_psd_cc_liveries(
        'pp/11Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=60,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
