import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge_15kv

se_e_blhj6_1 = Train(
    id='se_e_blhj6_1',
    name='њBLHJ 6',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC + Train.Flags.USE_CARGO_MULT,
    country='sweden',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(70),
    power=200,
    introduction_date=date(1916, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=26,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=2,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes= (grf.CargoClass.MAIL),
    non_refittable_cargo_classes= (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
    cargo_allow_refit= [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
    callbacks= {
        'cargo_capacity': Train.Luggage.sw_capacity_calculaiton_lug(2, g),
        },
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal, luggage',
        'Trivia': 'Its angled cab windows gave it the nickname "Vindögde Per" (Cross-eyed Per)'
    }),
)

se_e_blhj7_1 = Train(
    id='se_e_blhj7_1',
    name='њBLHJ 7',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(70),
    power=101,
    introduction_date=date(1927, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=20,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=40,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

    