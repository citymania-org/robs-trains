import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_1500v

d_e_stog1_1_dsb = Train(
    id='d_e_stog1_1_dsb',
    name='њDSB S-Tog 1 "De Brune S-Tog"',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading=('mm',),
        paint=('mmdsb1',),
        overlay=('mmlight'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(90),
    power=1288,
    introduction_date=date(1933, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=137,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=248, #245 seats, 0 collapsible seats, ca 105 standing = 350
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers, two of these make a "whole train"',
        'Info': 'These sets are no longer standard after 1936 but saw some use into the early 1950s',
        'Class': 'MM-FM-MM',
    }),
).add_articulated_part(
    id='d_e_stog12_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='fm',
        paint='fmdsb1',
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=101,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog13_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='mmr',
        paint='fsdsb1',
        overlay=('mmrlight'),
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_stog1_2_dsb = Train(
    id='d_e_stog1_2_dsb',
    name='њDSB S-Tog 1 "De Brune S-Tog"',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading=('mm',),
        paint=('mmdsb1',),
        overlay=('mmlight'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(90),
    power=644,
    introduction_date=date(1936, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=77,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=205, #136 seats, 0 collapsible seats, ca 70 standing = 206
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers, "quarter train" combine with each other or "half train" to make a "whole train"',
        'Class': 'MM-FS',
    }),
).add_articulated_part(
    id='d_e_stog12_2_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='fs',
        paint='fsdsb1',
        overlay=('fslight'),
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_stog1_3_dsb = Train(
    id='d_e_stog1_3_dsb',
    name='њDSB S-Tog 1 "De Brune S-Tog"',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading=('mm',),
        paint=('mmdsb1',),
        overlay=('mmlight'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(90),
    power=1288,
    introduction_date=date(1936, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=172,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=225, #338 seats, 0 collapsible seats, ca 140 standing = 478
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers, "half train" combine with each other or "quarter train" to make a "whole train"',
        'Info': 'These sets are no longer standard after 1968 and "half train" became mostly made up of two permanently tied "quarter train"',
        'Class': 'MM-FM-FM-MM',
    }),
).add_articulated_part(
    id='d_e_stog12_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='fm',
        paint='fmdsb1',
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=251,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog13_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='fm',
        paint='fmdsb1',
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog14_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='mmr',
        paint='fsdsb1',
        overlay=('mmrlight'),
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

#60s

d_e_stog1_4_dsb = Train(
    id='d_e_stog1_4_dsb',
    name='њDSB S-Tog 1 "De Brune S-Tog"', #with 1 instead of 2 pantos
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading=('mm',),
        paint=('mmdsb1',),
        overlay=('modmmlight'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(90),
    power=644,
    introduction_date=date(1961, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=77,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=205, #136 seats, 0 collapsible seats, ca 70 standing = 206
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers, "quarter train" combine with each other or "half train" to make a "whole train"',
        'Class': 'MM-FS',
    }),
).add_articulated_part(
    id='d_e_stog12_4_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='fs',
        paint='fsdsb1',
        overlay=('fslight'),
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_e_stog1_5_dsb = Train(
    id='d_e_stog1_5_dsb',
    name='њDSB S-Tog 1 "De Brune S-Tog"', #with 1 instead of 2 pantos
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading=('mm',),
        paint=('mmdsb1',),
        overlay=('modmmlight'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(90),
    power=1288,
    introduction_date=date(1961, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=172,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=225, #338 seats, 0 collapsible seats, ca 140 standing = 478
    cost_factor=25,
    loading_speed=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Short distance local passengers, "half train" combine with each other or "quarter train" to make a "whole train"',
        'Info': 'These sets are no longer standard after 1968 and "half train" became mostly made up of two permanently tied "quarter train"',
        'Class': 'MM-FM-FM-MM',
    }),
).add_articulated_part(
    id='d_e_stog12_5_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='fm',
        paint='fmdsb1',
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=251,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog13_5_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='fm',
        paint='fmdsb1',
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='d_e_stog14_5_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/stog1.psd',
        shading='mmr',
        paint='fsdsb1',
        overlay=('modmmrlight'),
        cc_replace=colours['MAROON'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
