import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_cmb17_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(100),
    power=120,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=10,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=45,
    loading_speed=10,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

no_d_cmb17_1 = Train(
    **COMMON_cmb17_PROPS,
    id='no_d_cmb17_1',
    name='њNSB Cmb17a',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='6a',
        paint='6b',
        cc_replace=colours["NAVY"],
        cc2_replace=colours["DCREAM"]
    ),
    company='na',
    introduction_date=date(1935, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)