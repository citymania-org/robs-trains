import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_type62_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(70),
    power=470,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=43,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=73,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='norway',
)

no_e_type62_1 = Train(
    **COMMON_type62_PROPS,
    id='no_e_type62_1',
    name='ЊNSB Type 62',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    company='na',
    introduction_date=date(1931, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)
