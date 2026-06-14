import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_iore_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    power_type='15kv',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=standard_gauge_15kv,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    max_speed=Train.kmhish(80),
    power=14684,
    weight=360,
)

se_e_iore_1 = Train(
    **COMMON_iore_PROPS,
    id='se_e_iore_1',
    purchase_sprite_towed_id='se_e_iore2_1',
    name='MTAB Iore',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('10a',),
        paint=('10b',),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["SCARLET"]
    ),
    company='na',
    introduction_date=date(2000, 1, 1),
    country='sweden',
    additional_text=grf.fake_vehicle_info({
        'Toilet': 'Yes',
        'Use': 'Iron ore trains in northern Sweden',
    }),
).add_articulated_part(
    id='se_e_iore2_1',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='10a',
        paint='10b',
        cc_replace=colours['COBALT'],
        cc2_replace=colours['SCARLET'],
    ),
)
