import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_teak_PROPS = dict(
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    max_speed=Train.kmhish(100),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dk_p_teak_1 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_1',
    name='DSB AM II', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=9,
    cargo_capacity=36,
    weight=39,
    country='denmark',
    company='na',
    introduction_date=date(1903, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '1st & 2nd class',
    }),
)

dk_p_teak_2 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_2',
    name='DSB AN I', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=8,
    cargo_capacity=32,
    weight=31,
    country='denmark',
    company='na',
    introduction_date=date(1908, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '1st & 2nd class',
    }),
)

dk_p_teak_3 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_3',
    name='DSB AN VI', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    length=8,
    cargo_capacity=32,
    weight=35,
    country='denmark',
    company='na',
    introduction_date=date(1922, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '1st & 2nd class',
    }),
)

dk_p_teak_4 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_4',
    name='DSB AF III', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=8,
    cargo_capacity=36,
    weight=35,
    country='denmark',
    company='na',
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '1st class',
    }),
)

dk_p_teak_5 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_5',
    name='DSB AR I', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    length=9,
    cargo_capacity=58,
    weight=39,
    country='denmark',
    company='na',
    introduction_date=date(1939, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '1st & 2nd class',
    }),
)

dk_p_teak_6 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_6',
    name='DSB AR I', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=9,
    cargo_capacity=58,
    weight=39,
    country='denmark',
    company='na',
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '1st & 2nd class',
    }),
)

dk_p_teak_7 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_7',
    name='DSB BL III', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=9,
    cargo_capacity=70,
    weight=28,
    country='denmark',
    company='na',
    introduction_date=date(1902, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
    }),
)

dk_p_teak_8 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_8',
    name='DSB BM III', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=8,
    cargo_capacity=36,
    weight=30,
    country='denmark',
    company='na',
    introduction_date=date(1910, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
    }),
)

dk_p_teak_9 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_9',
    name='DSB BP I', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=9,
    cargo_capacity=58,
    weight=38,
    country='denmark',
    company='na',
    introduction_date=date(1910, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd & 3rd class',
    }),
)

dk_p_teak_10 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_10',
    name='DSB CM VI', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=9,
    cargo_capacity=72,
    weight=29,
    country='denmark',
    company='na',
    introduction_date=date(1896, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)

dk_p_teak_11 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_11',
    name='DSB CM I', #metal
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=9,
    cargo_capacity=72,
    weight=35,
    country='denmark',
    company='na',
    introduction_date=date(1909, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)

dk_p_teak_12 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_12',
    name='DSB CM II', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    length=9,
    cargo_capacity=72,
    weight=34,
    country='denmark',
    company='na',
    introduction_date=date(1914, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)

dk_p_teak_13 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_13',
    name='DSB CM II', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=9,
    cargo_capacity=72,
    weight=34,
    country='denmark',
    company='na',
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
    }),
)

dk_p_teak_14 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_14',
    name='DSB CL IV', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    length=9,
    cargo_capacity=82,
    weight=30,
    country='denmark',
    company='na',
    introduction_date=date(1936, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)

dk_p_teak_15 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_15',
    name='DSB CO I', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=9,
    cargo_capacity=82,
    weight=30,
    country='denmark',
    company='na',
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
    }),
)

dk_p_teak_16 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_16',
    name='DSB CX XIV', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    length=8,
    cargo_capacity=67,
    weight=33,
    country='denmark',
    company='na',
    introduction_date=date(1937, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class',
    }),
)

dk_p_teak_17 = Train(
    **COMMON_teak_PROPS,
    id='dk_p_teak_17',
    name='DSB CP VIII', #wood
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    length=8,
    cargo_capacity=67,
    weight=33,
    country='denmark',
    company='na',
    introduction_date=date(1951, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '2nd class',
    }),
)
