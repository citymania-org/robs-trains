import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_25kv_3kv_1500v, badges

COMMON_36000_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_25kv_3kv_1500v,
    max_speed=Train.kmhish(200),
    power=7614,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

fr_e_bb36000_1 = Train(
    **COMMON_36000_PROPS,
    id='fr_e_bb36000_1',
    name='SNCF BB 36000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['FR'],
        'role': ['freight'],
        'power': ['electric/acdc/1500v_3kv_25kv', 'electric/dc/1500v', 'electric/dc/3kv', 'electric/ac/25kv'],
        'operator': ['FR/sncf'],
        'manufacturer': [],
    }),
)

fr_e_bb36000_2 = Train(
    **COMMON_36000_PROPS,
    id='fr_e_bb36000_2',
    name='SNCF BB 36000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["GREY3"]
    ),
    introduction_date=date(2003, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['FR'],
        'role': ['freight'],
        'power': ['electric/acdc/1500v_3kv_25kv', 'electric/dc/1500v', 'electric/dc/3kv', 'electric/ac/25kv'],
        'operator': ['FR/sncf'],
        'manufacturer': [],
    }),
)
