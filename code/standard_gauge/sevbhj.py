import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

#DMU (Vehicles that ended up at SNJ can be found in 'sesnj.py')

se_d_MCo_1 = Train(
    id='se_d_MCo_1',
    name='њVBHJ MCo 1-3', 
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["DCREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(80),
    power=175,
    introduction_date=date(1930, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=32,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=72,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Loading speed': '10',
        'Use': '3rd class, luggage',
    }),
    mid_stats={
        'cargo_capacity': 2,
        'refittable_cargo_classes': (grf.CargoClass.MAIL),
        'non_refittable_cargo_classes': (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
        'cargo_allow_refit': [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
        'loading_speed': 10,
        'callbacks': {
            'cargo_capacity': Train.Luggage.switch_cargo_capacity(4, g),
            'cargo_subtype_text': Train.Luggage.switch_subtype(g),
        },
    },
)

# Carriages

# VBHJ Bco 56

se_p_BCo_1 = Train( #Do not push until the capacity has been established
    id='se_p_BCo_1',
    name='њVBHJ BCo', 
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["DCREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1938, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(30)),
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=68,  #Estimate
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class, 3rd class',
    }),
)