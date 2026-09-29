import grf, lib

from datetime import date

from common import  g, Train, colours, make_psd_cc_liveries, make_psd_cc_liveries_flippable, standard_gauge

import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro, standard_gauge_1500v

COMMON_500_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(60),
    power=580,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=35,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=134,
    loading_speed=20,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='norway',
)

no_e_500_1 = Train(
    **COMMON_500_PROPS,
    id='no_e_500_1',
    name='њHKB 500-serien',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    purchase_sprite_towed_id='no_e_500_1_car2',
    company='na',
    introduction_date=date(1947, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1435mm',
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='no_e_500_1_car2',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours['BROWN'],
        cc2_replace=colours['BROWN'],
    ),
    cargo_capacity=134,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

no_e_500_2 = Train(
    **COMMON_500_PROPS,
    id='no_e_500_2',
    name='њHKB 500-serien',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours["MAROON"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='no_e_500_2_car2',
    company='na',
    introduction_date=date(1962, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1435mm',
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='no_e_500_2_car2',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=134,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

no_e_500_3 = Train(
    **COMMON_500_PROPS,
    id='no_e_500_3',
    name='њOS 500-serien',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours["NSBRED"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='no_e_500_3_car2',
    company='na',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1435mm',
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='no_e_500_3_car2',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours['NSBRED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=134,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

no_e_500_4 = Train(
    **COMMON_500_PROPS,
    id='no_e_500_4',
    name='њOS 500-serien',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='no_e_500_4_car2',
    company='na',
    introduction_date=date(1981, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1435mm',
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='no_e_500_4_car2',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=134,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

no_e_500_5 = Train(
    **COMMON_500_PROPS,
    id='no_e_500_5',
    name='њOS 500-serien',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours["RED"],
        cc2_replace=colours["BLUE"]
    ),
    purchase_sprite_towed_id='no_e_500_5_car2',
    company='na',
    introduction_date=date(1989, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Gauge': '1435mm',
        'Use': 'Local passengers',
    }),
).add_articulated_part(
    id='no_e_500_5_car2',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours['RED'],
        cc2_replace=colours['BLUE'],
    ),
    cargo_capacity=134,
    loading_speed=20,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)