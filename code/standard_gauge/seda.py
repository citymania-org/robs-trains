import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge_15kv

COMMON_da_PROPS = dict(
    length=6,
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
    country='sweden',
    max_speed=Train.kmhish(100),
    power=2502,
    weight=75,
)

se_e_da_1 = Train(
    **COMMON_da_PROPS,
    id='se_e_da_1',
    name='SJ Da',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SEBROWN"],
        cc2_replace=colours["SEBROWN"]
    ),
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_da_2 = Train(
    **COMMON_da_PROPS,
    id='se_e_da_2',
    name='BK Da', #https://www.svenska-lok.se/Fotos/PbaneSJ/TAB/TAB_Da_887_2006.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["BLUE"]
    ),
    company='na',
    introduction_date=date(1998, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_da_3 = Train(
    **COMMON_da_PROPS,
    id='se_e_da_3',
    name='TAB Da', #https://www.svenska-lok.se/Fotos/PbaneSJ/TAB/TAB_Da_887_2006.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY1"]
    ),
    company='na',
    introduction_date=date(2005, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

se_e_da_4 = Train(
    **COMMON_da_PROPS,
    id='se_e_da_4',
    name='NR Da', #https://www.svenska-lok.se/Fotos/PbaneSJ/NR/NR_Da_903_2015.jpg
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('6a',),
        paint=('6b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["DGREEN"]
    ),
    company='na',
    introduction_date=date(2015, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
