import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_f_PROPS = dict(
    length=6,
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
    power=1529,
    weight=131,
)

#length is 2127, in 1393 and 734 so it could be 6/4 or 7/3
#ones made by frichs have more dome thingies

se_s_f_1 = Train(
    **COMMON_f_PROPS,
    id='se_s_f_1',
    purchase_sprite_towed_id='se_s_f2_1',
    name='SJ F',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    max_speed=Train.kmhish(90),
    introduction_date=date(1914, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='se_s_f2_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

se_s_f_2 = Train(
    **COMMON_f_PROPS,
    id='se_s_f_2',
    purchase_sprite_towed_id='se_s_f2_2',
    name='DSB E',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(110),
    introduction_date=date(1937, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='se_s_f2_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)

se_s_f_3 = Train(
    **COMMON_f_PROPS,
    id='se_s_f_3',
    purchase_sprite_towed_id='se_s_f2_3',
    name='DSB E',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    max_speed=Train.kmhish(110),
    introduction_date=date(1942, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='se_s_f2_3',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)
