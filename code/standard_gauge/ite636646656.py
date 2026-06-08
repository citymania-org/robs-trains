import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_guage_3kv

COMMON_6x6_PROPS = dict(
    length=4,
    misc_flags=Train.Flags.USE_2CC,
    power_type='dc3000',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_guage_3kv,
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

it_e_636_1 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_636_1',
    purchase_sprite_towed_id='it_e_6362_1',
    name='FS E.636',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["YELLOWBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(120),
    power=2855,
    weight=101,
    introduction_date=date(1940, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6362_1',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['YELLOWBROWN'],
        cc2_replace=colours['REDBROWN'],
    ),
).add_articulated_part(
    id='it_e_6363_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['YELLOWBROWN'],
        cc2_replace=colours['REDBROWN'],
    ),
)

it_e_636_2 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_636_2',
    purchase_sprite_towed_id='it_e_6362_2',
    name='FS E.636',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(120),
    power=2855,
    weight=101,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6362_2',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY2'],
    ),
).add_articulated_part(
    id='it_e_6363_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY2'],
    ),
)

it_e_636_3 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_636_3',
    purchase_sprite_towed_id='it_e_6362_3',
    name='FS E.636',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(120),
    power=2855,
    weight=101,
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6362_3',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['GREY2'],
    ),
).add_articulated_part(
    id='it_e_6363_3',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['GREY2'],
    ),
)

it_e_646_1 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_646_1',
    purchase_sprite_towed_id='it_e_6462_1',
    name='FS E.646 series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(140),
    power=5874,
    weight=110,
    introduction_date=date(1958, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6462_1',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['GREEN'],
        cc2_replace=colours['GREY2'],
    ),
).add_articulated_part(
    id='it_e_6463_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['GREEN'],
        cc2_replace=colours['GREY2'],
    ),
)

it_e_646_2 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_646_2',
    purchase_sprite_towed_id='it_e_6462_2',
    name='FS E.646 series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["YELLOWBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(140),
    power=5874,
    weight=110,
    introduction_date=date(1962, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6462_2',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['YELLOWBROWN'],
        cc2_replace=colours['REDBROWN'],
    ),
).add_articulated_part(
    id='it_e_6463_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['YELLOWBROWN'],
        cc2_replace=colours['REDBROWN'],
    ),
)

it_e_646_3 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_646_3',
    purchase_sprite_towed_id='it_e_6462_3',
    name='FS E.646 series 1',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(140),
    power=5874,
    weight=110,
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6462_3',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['GREY2'],
    ),
).add_articulated_part(
    id='it_e_6463_3',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['GREY2'],
    ),
)

it_e_646_4 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_646_4',
    purchase_sprite_towed_id='it_e_6462_4',
    name='FS E.646 series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(140),
    power=5874,
    weight=110,
    introduction_date=date(1961, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6462_4',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['GREEN'],
        cc2_replace=colours['GREY2'],
    ),
).add_articulated_part(
    id='it_e_6463_4',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['GREEN'],
        cc2_replace=colours['GREY2'],
    ),
)

it_e_646_5 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_646_5',
    purchase_sprite_towed_id='it_e_6462_5',
    name='FS E.646 series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["YELLOWBROWN"],
        cc2_replace=colours["REDBROWN"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(140),
    power=5874,
    weight=110,
    introduction_date=date(1963, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6462_5',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['YELLOWBROWN'],
        cc2_replace=colours['REDBROWN'],
    ),
).add_articulated_part(
    id='it_e_6463_5',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['YELLOWBROWN'],
        cc2_replace=colours['REDBROWN'],
    ),
)

it_e_646_6 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_646_6',
    purchase_sprite_towed_id='it_e_6462_6',
    name='FS E.646 series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["DPURPLE"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(140),
    power=5874,
    weight=110,
    introduction_date=date(1981, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6462_6',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['ORANGE'],
        cc2_replace=colours['DPURPLE'],
    ),
).add_articulated_part(
    id='it_e_6463_6',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['ORANGE'],
        cc2_replace=colours['DPURPLE'],
    ),
)

it_e_646_7 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_646_7',
    purchase_sprite_towed_id='it_e_6462_7',
    name='FS E.646 series 2',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(140),
    power=5874,
    weight=110,
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6462_7',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['GREY2'],
    ),
).add_articulated_part(
    id='it_e_6463_7',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['GREY2'],
    ),
)

it_e_656_1 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_656_1',
    purchase_sprite_towed_id='it_e_6562_1',
    name='FS E.656',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(150),
    power=6526,
    weight=120,
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6562_1',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY2'],
    ),
).add_articulated_part(
    id='it_e_6563_1',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['GREY2'],
    ),
)

it_e_656_2 = Train(
    **COMMON_6x6_PROPS,
    id='it_e_656_2',
    purchase_sprite_towed_id='it_e_6562_2',
    name='FS E.656',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading=('4a',),
        paint=('4b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY2"]
    ),
    country='italy',
    company='na',
    max_speed=Train.kmhish(150),
    power=6526,
    weight=120,
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='it_e_6562_2',
    length=1,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 0
        shading='3a', #should be 0
        paint='3b', #should be 0
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['GREY2'],
    ),
).add_articulated_part(
    id='it_e_6563_2',
    length=4,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd', #draw as 4,5
        shading='4a',
        paint='4b',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['GREY2'],
    ),
)
