import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_o_PROPS = dict(
    length=5,
    misc_flags=Train.Flags.USE_2CC,
    power_type='steam',
    engine_class=Train.EngineClass.STEAM, 
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    max_speed=Train.kmhish(70),
    power=500,
    weight=54,
)

dk_s_o_1 = Train(
    **COMMON_o_PROPS,
    id='dk_s_o_1',
    name='DSB O',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1896, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

dk_s_o_2 = Train(
    **COMMON_o_PROPS,
    id='dk_s_o_2',
    name='DSB O', #new coal box
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1932, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)
