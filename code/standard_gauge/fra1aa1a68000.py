import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_68000_PROPS = dict(
    length=8,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
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
    max_speed=Train.kmhish(130),
    power=2257,
    weight=105,
)

fr_d_68000_1 = Train(
    **COMMON_68000_PROPS,
    id='fr_d_68000_1',
    name='SNCF A1A-A1A 68000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    introduction_date=date(1963, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_68000_2 = Train(
    **COMMON_68000_PROPS,
    id='fr_d_68000_2',
    name='SNCF A1A-A1A 68000', #new cabs with different windows from 68018
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["NAVY"]
    ),
    country='france',
    company='na',
    introduction_date=date(1964, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

fr_d_68000_3 = Train(
    **COMMON_68000_PROPS,
    id='fr_d_68000_3',
    name='SNCF A1A-A1A 68000',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('8a',),
        paint=('8b',),
        cc_replace=colours["MBC"],
        cc2_replace=colours["GREY3"]
    ),
    country='france',
    company='na',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
