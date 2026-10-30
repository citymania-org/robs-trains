import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, metro, standard_gauge


COMMON_C20_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=metro,
    max_speed=Train.kmhish(90),
    power=435,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=67,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=133, #(397 per set)
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

se_e_C20_1 = Train(
    **COMMON_C20_PROPS,
    id='se_e_C20_1',
    name='SL C20',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a'),
        paint=('7b'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY10"]
    ),
    company='sl',
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Stockholm Metro trains',
    }),
).add_articulated_part(
    id='se_e_C20_1_car2',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a'),
        paint=('7b'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY10'],
    ),
    cargo_capacity=132,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='se_e_C20_1_car3',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a'),
        paint=('7b'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY10'],
    ),
    cargo_capacity=132,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_C20U_PROPS = dict(
    length=7,
    misc_flags=Train.Flags.MULTIPLE_UNIT + Train.Flags.USE_2CC,
    power_type='3rd',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=metro,
    max_speed=Train.kmhish(90),
    power=435,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=67,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=138, #(416 per set)
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

se_e_C20u_1 = Train(
    **COMMON_C20U_PROPS,
    id='se_e_C20u_1',
    name='SL C20U',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a'),
        paint=('7b'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY10"]
    ),
    company='sl',
    introduction_date=date(2021, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Stockholm Metro trains',
        'Trivia': '''C20 half-life refurbishment''',
    }),
).add_articulated_part(
    id='se_e_C20u_1_car2',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a'),
        paint=('7b'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY10'],
    ),
    cargo_capacity=140,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='se_e_C20u_1_car3',
    length=7,
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('7a'),
        paint=('7b'),
        cc_replace=colours['SLBLUE'],
        cc2_replace=colours['GREY10'],
    ),
    cargo_capacity=138,
    loading_speed=40,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

#2059: Puma
#2150: OMX
#2202: Interflora/Puma
#2205: Digital-TV (≤2007)
#2208: Kommunal
#2210: Head & Shoulders
#2211: Sveriges Radio (2009)
#2215: Pepsodent (2009)
#2216: Aftonbladet/Sportbladet (≤2005)
#2218: Stargate Atlantis
#2224: Heinz (≤2004)
#2228: Go training
#2233: Sony Ericsson
#2238: MTV
#2245: Hyresgästföreningen
#2257: Gallerian (≤2005)
#2264: Lätta 
#2269: Eniro (≤2005)
#SD2022 (2022)