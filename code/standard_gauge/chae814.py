import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_814_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
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

ch_e_ae814_1 = Train(
    **COMMON_814_PROPS,
    id='ch_e_ae814_1',
    purchase_sprite_towed_id='ch_e_ae8142_1',
    name='SBB Ae 8/14 11801',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    max_speed=Train.kmhish(100),
    power=7497,
    weight=240,
    company='na',
    introduction_date=date(1931, 1, 1),
    country='switzerland',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Visually and technically similar to the Ae 4/7',
    }),
).add_articulated_part(
    id='ch_e_ae8142_1',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['SBB'],
        cc2_replace=colours['SBB'],
    ),
)

ch_e_ae814_2 = Train(
    **COMMON_814_PROPS,
    id='ch_e_ae814_2',
    purchase_sprite_towed_id='ch_e_ae8142_2',
    name='SBB Ae 8/14 11801',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["TURQUOISE"]
    ),
    max_speed=Train.kmhish(100),
    power=7497,
    weight=240,
    company='na',
    introduction_date=date(1955, 1, 1),
    country='switzerland',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Painted like this from 1955 to 1961',
    }),
).add_articulated_part(
    id='ch_e_ae8142_2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['TURQUOISE'],
    ),
)

ch_e_ae814_3 = Train(
    **COMMON_814_PROPS,
    id='ch_e_ae814_3',
    purchase_sprite_towed_id='ch_e_ae8142_3',
    name='SBB Ae 8/14 11851',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    max_speed=Train.kmhish(100),
    power=8797,
    weight=246,
    company='na',
    introduction_date=date(1932, 1, 1),
    country='switzerland',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'More technically advanced than 11801',
    }),
).add_articulated_part(
    id='ch_e_ae8142_3',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['SBB'],
        cc2_replace=colours['SBB'],
    ),
)

ch_e_ae814_4 = Train(
    **COMMON_814_PROPS,
    id='ch_e_ae814_4',
    purchase_sprite_towed_id='ch_e_ae8142_4',
    name='SBB Ae 8/14 11851',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["TURQUOISE"]
    ),
    max_speed=Train.kmhish(100),
    power=8797,
    weight=246,
    company='na',
    introduction_date=date(1953, 1, 1),
    country='switzerland',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Painted like this from 1953 to 1961',
    }),
).add_articulated_part(
    id='ch_e_ae8142_4',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['TURQUOISE'],
    ),
)


ch_e_ae814_5 = Train(
    **COMMON_814_PROPS,
    id='ch_e_ae814_5',
    purchase_sprite_towed_id='ch_e_ae8142_5',
    name='SBB Ae 8/14 11852 "Landi-Lok"',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["TURQUOISE"]
    ),
    max_speed=Train.kmhish(110),
    power=11097,
    weight=236,
    company='na',
    introduction_date=date(1938, 1, 1),
    country='switzerland',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Upon construction it was the most powerful locomotive in the world',
    }),
).add_articulated_part(
    id='ch_e_ae8142_5',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['TURQUOISE'],
    ),
)

ch_e_ae814_6 = Train(
    **COMMON_814_PROPS,
    id='ch_e_ae814_6',
    purchase_sprite_towed_id='ch_e_ae8142_6',
    name='SBB Ae 8/14 11852 "Landi-Lok"',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    max_speed=Train.kmhish(110),
    power=11097,
    weight=236,
    company='na',
    introduction_date=date(1964, 1, 1),
    country='switzerland',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Painted like this from 1964 to 1971',
    }),
).add_articulated_part(
    id='ch_e_ae8142_6',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['SBB'],
        cc2_replace=colours['SBB'],
    ),
)

ch_e_ae814_7 = Train(
    **COMMON_814_PROPS,
    id='ch_e_ae814_7',
    purchase_sprite_towed_id='ch_e_ae8142_7',
    name='SBB Ae 8/14 11851',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["SBB"],
        cc2_replace=colours["SBB"]
    ),
    max_speed=Train.kmhish(100),
    power=8247,
    weight=244,
    company='na',
    introduction_date=date(1961, 1, 1),
    country='switzerland',
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'A rebuild with cabs like the Ae 6/6',
    }),
).add_articulated_part(
    id='ch_e_ae8142_7',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='8a',
        paint='8b',
        cc_replace=colours['SBB'],
        cc2_replace=colours['SBB'],
    ),
)

look up about pantos
