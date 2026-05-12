import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

dk_d_lm21_1 = Train(
    id='dk_d_lm21_1',
    name='LNJ Lm',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["SLBLUE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    purchase_sprite_towed_id='dk_d_lm212_1',
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=620,
    introduction_date=date(1996, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=33,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=67,
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Trivia': 'Used on Nærumbanen',
    }),
).add_articulated_part(
    id='dk_d_lm212_1',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 2
        shading='3a', #should be 1
        paint='3b', #should be 1
        cc_replace=colours['COLBALT'],
        cc2_replace=colours['SLBLUE'],
    ),
    cargo_capacity=50,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='dk_d_lm213_1',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='5a',
        paint='5b',
        cc_replace=colours['COLBALT'],
        cc2_replace=colours['SLBLUE'],
    ),
    cargo_capacity=57,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_d_lm21_2 = Train(
    id='dk_d_lm21_2',
    name='LB Lm',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY7"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    purchase_sprite_towed_id='dk_d_lm212_2',
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=620,
    introduction_date=date(2009, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=33,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=67,
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers',
        'Trivia': 'Used on Nærumbanen',
    }),
).add_articulated_part(
    id='dk_d_lm212_2',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 2
        shading='3a', #should be 1
        paint='3b', #should be 1
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY7'],
    ),
    cargo_capacity=50,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='dk_d_lm213_2',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='5a',
        paint='5b',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY7'],
    ),
    cargo_capacity=57,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
