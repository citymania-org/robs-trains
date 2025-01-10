import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

d_d_mx_i_1_dsb = Train(
    id='d_d_mx_i_1_dsb',
    name='DSB MX I',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/mxe.psd',
        shading=('mxe',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["MAROON"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(110),
    power=850,
    introduction_date=date(1932, 1, 1),
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=103,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Operated on Jylland, only 2 made, #131 was scrapped in 1960 & #132 is preserved at Marselv as of 2024',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)
