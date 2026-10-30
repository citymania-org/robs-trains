import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

#Љ Do not add this train to generate.py until the addition of Template.psd layer "2a" and "2b" or when this loco gets its .psd


COMMON_M3t_PROPS = dict(
    length=6,
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
    power=1500,
    weight=135,
)

se_s_m3t_1 = Train(
    **COMMON_M3t_PROPS,
    id='se_s_m3t_1',
    purchase_sprite_towed_id='se_s_m3t_2',
    name='ЉњOFWJ M3t ',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    max_speed=Train.kmhish(70),
    introduction_date=date(1930, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
        'Trivia': 'Later known as "TGOJ M3t". One of few successful steam turbine locomotives, all three untis of this has class have been preserved'
    }),
).add_articulated_part(
    id='se_s_m3t_2',
    length=2,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading='2a',   #Does not exist - yet
        paint='2b',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY10'],
    ),
)