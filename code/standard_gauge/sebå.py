import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_B_PROPS = dict(
    length=4,
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
    power=310,
    weight=38,
)

se_s_b_1 = Train(
    **COMMON_B_PROPS,
    id='se_s_b_1',
    purchase_sprite_towed_id='se_s_b_2',
    name='ЉњSJ B ',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('5a',),
        paint=('5b',),
        cc_replace=colours["SBB"], #ЉCheck
        cc2_replace=colours["RED"] #ЉCheck
    ),
    country='sweden',
    company='na',
    max_speed=Train.kmhish(60),
    introduction_date=date(1856, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
).add_articulated_part(
    id='se_s_b_2',
    length=2,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='2a',   #Does not exist - yet
        paint='2b',
        cc_replace=colours['SBB'],
        cc2_replace=colours['RED'],
    ),
)
