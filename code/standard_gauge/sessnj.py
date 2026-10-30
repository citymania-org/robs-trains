import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, metro, standard_gauge_1500v

COMMON_XF_PROPS = dict(
    length=4,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_1500v,
    max_speed=Train.kmhish(50),
    power=299,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=28,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=164,
    loading_speed=20,
    cost_factor=25,
)

se_e_xf_1 = Train(
    **COMMON_XF_PROPS,
    id='se_e_xf_1',
    name='њSSnJ XF',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='4a',
        paint='4b',
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    company='na',
    introduction_date=date(1946, 1, 1),
    refittable_cargo_classes= (grf.CargoClass.MAIL),
    non_refittable_cargo_classes= (grf.CargoClass.HAZARDOUS + grf.CargoClass.PASSENGERS),
    cargo_allow_refit= [g.get_cargo_id("MAIL"), g.get_cargo_id("FOOD"), g.get_cargo_id("GOOD")],
    callbacks= {
                'cargo_capacity': Train.Luggage.sw_capacity_calculaiton_lug(2, g),  #1,5t irl
            },
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal, luggage',
    }),
)
