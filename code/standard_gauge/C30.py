import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro, standard_gauge


COMMON_C30_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=metro,
    max_speed=Train.kmhish(90),
    power=1360,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=116,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=215,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_e_C30_1_sl = Train(
    **COMMON_C30_PROPS,
    id='s_e_C30_1_sl',
    name='SL C30',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a'),
        paint=('9b'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["SLBLUE"]
    ),
    purchase_sprite_towed_id='s_e_C30_1_sl_car2',
    company='sl',
    introduction_date=date(2018, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Stockholm Metro',
        'Builder': 'Bombardier',
        'Trivia': '''Replaced the last Cx units. Certain units bear names connected to culture such as "Siw Malmkvist", "Noice" and "Ebba Grön"''',
    }),
).add_articulated_part(
    id='s_e_C30_1_sl_car2',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a'),
        paint=('8b'),
        cc_replace=colours['GREY1'],
        cc2_replace=colours['SLBLUE'],
    ),
    cargo_capacity=215,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='s_e_C30_1_sl_car3',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a'),
        paint=('8b'),
        cc_replace=colours['GREY1'],
        cc2_replace=colours['SLBLUE'],
    ),
    cargo_capacity=215,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='s_e_C30_1_sl_car4',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a'),
        paint=('9b'),
        cc_replace=colours['GREY1'],
        cc2_replace=colours['SLBLUE'],
    ),
    cargo_capacity=215,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

