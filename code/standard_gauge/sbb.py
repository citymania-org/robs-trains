import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

ch_p_2pax_1_sbb = Train(
    id='ch_p_2pax_1_sbb',
    name='SBB 2 Axle Carriage',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/ш2pax.psd',
        overlay=('2pax'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='switzerland',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(60),
    power=0,
    introduction_date=date(1899, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=15,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=36,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local and branch lines',
    }),
)

ch_p_2bag_1_sbb = Train(
    id='ch_p_2bag_1_sbb',
    name='SBB 2 Axle Baggage Wagon',
    length=6,
    liveries=make_psd_cc_liveries(
        'pp/ш2pax.psd',
        overlay=('2bag'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='switzerland',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(60),
    power=0,
    introduction_date=date(1899, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=30,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local and branch lines',
    }),
)

ch_p_4pax_1_sbb = Train(
    id='ch_p_4pax_1_sbb',
    name='SBB 4 Axle Carriage',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/ш4pax.psd',
        overlay=('4pax'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='switzerland',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=0,
    introduction_date=date(1899, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=19,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=42,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local and branch lines',
    }),
)

ch_p_4bag_1_sbb = Train(
    id='ch_p_4bag_1_sbb',
    name='SBB 4 Axle Baggage Wagon',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/ш4pax.psd',
        overlay=('4bag'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='switzerland',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=0,
    introduction_date=date(1899, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=18,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=35,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local and branch lines',
    }),
)
