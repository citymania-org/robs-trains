import grf, lib

from datetime import date

from common import Train, Livery, colours, make_psd_cc_liveries, standard_gauge

COMMON_mbrød_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(90),
    power=750,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=61,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    country='denmark',
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

dk_d_mbrød_467_1 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_467_1',
    name='HFHJ M 8',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_1_1952.png', cc_replace=colours["RED"], cc2_replace=colours["RED"]),
        '2CC': Livery('1952_DK_Frichs_467_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_467_2 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_467_2',
    name='HFHJ M 8',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_3_1960.png', cc_replace=colours["RED"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1952_DK_Frichs_467_3_1960.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Reapplied in 1997',
    }),
)

dk_d_mbrød_467_3 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_467_3',
    name='HFHJ M 8',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_4_1981.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_467_4_1981.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1981, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_468_1 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_468_1',
    name='OHJ 24',
    liveries={
        'Default': Livery('1952_DK_Frichs_468_1_1952.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_468_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_469_1 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_469_1',
    name='LJ M 31/32',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["MAROON"]),
        '2CC': Livery('1952_DK_Frichs_469_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'This vehicle is also VLTJ ML 12. VLTJ ML 12 had this livery reapplied in 2009',
    }),
)

dk_d_mbrød_469_2 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_469_2',
    name='LJ M 31/32',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_3_1974.png', cc_replace=colours["SCARLET"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_469_3_1974.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1974, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'From 1991 M 31 was run by SB as SB M 8 and in 2008 M 32 was run by Contec as Contec M32',
    }),
)

dk_d_mbrød_471_1 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_471_1',
    name='HHJ M 3',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["DCREAM"]),
        '2CC': Livery('1952_DK_Frichs_471_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_471_2 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_471_2',
    name='HHJ DL 11',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_2_1971.png', cc_replace=colours["SCARLET"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1952_DK_Frichs_471_2_1971.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1971, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_471_3 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_471_3',
    name='HHJ DL 11',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_4_1995.png', cc_replace=colours["SCARLET"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_471_4_1995.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_472_2 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_472_2',
    name='VLTJ ML 12',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_2_1968.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_472_2_1968.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_472_3 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_472_3',
    name='VLTJ ML 12',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_3_1980.png', cc_replace=colours["ORANGE"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1952_DK_Frichs_472_3_1980.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1980, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_472_4 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_472_4',
    name='VLTJ ML 12',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_4_1997.png', cc_replace=colours["RED"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1952_DK_Frichs_472_4_1997.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_473_1 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_473_1',
    name='GDS L 1',
    liveries={
        'Default': Livery('1952_DK_Frichs_473_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["DCREAM"]),
        '2CC': Livery('1952_DK_Frichs_473_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Reapplied in 2005',
    }),
)

dk_d_mbrød_473_2 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_473_2',
    name='GDS L 1',
    liveries={
        'Default': Livery('1952_DK_Frichs_473_2_1963.png', cc_replace=colours["MAROON"], cc2_replace=colours["DCREAM"]),
        '2CC': Livery('1952_DK_Frichs_473_2_1963.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1963, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_474_1 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_474_1',
    name='FFJ ML 1216',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["GREY10"]),
        '2CC': Livery('1952_DK_Frichs_474_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_474_2 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_474_2',
    name='OHJ 39',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_2_1969.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_474_2_1969.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1969, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Reapplied in 1993',
    }),
)

dk_d_mbrød_474_3 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_474_3',
    name='OHJ 39',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_4_1987.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_474_4_1987.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1987, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_475_1 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_475_1',
    name='AHJ ML 5206',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_1_1952.png', cc_replace=colours["RED"], cc2_replace=colours["GREY10"]),
        '2CC': Livery('1952_DK_Frichs_475_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_475_2 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_475_2',
    name='SB M 5',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_2_1973.png', cc_replace=colours["MAROON"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_475_2_1973.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1973, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_475_3 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_475_3',
    name='SB M 5',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_3_1977.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_475_3_1977.png', auto_cc=lib.CC_DEFAULT),
    },
    company='na',
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

dk_d_mbrød_475_4 = Train(
    **COMMON_mbrød_PROPS,
    id='dk_d_mbrød_475_4',
    name='AHJ ML 5206',
    liveries={
            'Default': Livery('1952_DK_Frichs_475_4_2008.png', cc_replace=colours["MAROON"], cc2_replace=colours["GREY10"]),
            '2CC': Livery('1952_DK_Frichs_475_4_2008.png', auto_cc=lib.CC_DEFAULT),
        },
    company='na',
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
