import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_frichs_467to475_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=61,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_d_frichs_467_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_1',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_1_1952.png', cc_replace=colours["RED"], cc2_replace=colours["RED"]),
        '2CC': Livery('1952_DK_Frichs_467_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_467_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_2',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_2_1958.png', cc_replace=colours["RED"], cc2_replace=colours["RED"]),
        '2CC': Livery('1952_DK_Frichs_467_2_1958.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1958, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_467_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_3',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_3_1960.png', cc_replace=colours["RED"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1952_DK_Frichs_467_3_1960.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_467_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_4',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_4_1981.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_467_4_1981.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1981, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_467_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_5',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_5_1997.png', cc_replace=colours["RED"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1952_DK_Frichs_467_5_1997.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_468_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_468_1',
    name='OHJ Frichs 468',
    liveries={
        'Default': Livery('1952_DK_Frichs_468_1_1952.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_468_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_468_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_468_2',
    name='OHJ Frichs 468',
    liveries={
        'Default': Livery('1952_DK_Frichs_468_2_1984.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_468_2_1984.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_468_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_468_3',
    name='OHJ Frichs 468',
    liveries={
        'Default': Livery('1952_DK_Frichs_468_3_2017.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_468_3_2017.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(2017, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_1',
    name='LJ Frichs 469/470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["MAROON"]),
        '2CC': Livery('1952_DK_Frichs_469_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_2',
    name='LJ Frichs 469/470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_2_1960.png', cc_replace=colours["MAROON"], cc2_replace=colours["MAROON"]),
        '2CC': Livery('1952_DK_Frichs_469_2_1960.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_3',
    name='LJ Frichs 469/470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_3_1974.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_469_3_1974.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1974, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_4',
    name='LJ Frichs 469/470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_4_1976.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_469_4_1976.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1976, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_8 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_8',
    name='SB Frichs 469',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_8_1992.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_469_8_1992.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1992, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_5',
    name='LJ Frichs 470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_5_1994.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_469_5_1994.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1994, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_6 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_6',
    name='LJ Frichs 470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_6_2007.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_469_6_2007.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(2007, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_7 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_7',
    name='Contec Frichs 470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_7_2008.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_469_7_2008.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_1',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["DCREAM"]),
        '2CC': Livery('1952_DK_Frichs_471_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_2',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_2_1977.png', cc_replace=colours["RED"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1952_DK_Frichs_471_2_1977.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_3',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_3_1988.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_471_3_1988.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(1988, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_4',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_4_1995.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_471_4_1995.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_5',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_5_2000.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_471_5_2000.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(2000, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_6 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_6',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_6_2014.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_471_6_2014.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(2014, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_1',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["MAROON"]),
        '2CC': Livery('1952_DK_Frichs_472_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_2',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_2_1968.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_472_2_1968.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_3',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_3_1980.png', cc_replace=colours["ORANGE"], cc2_replace=colours["CREAM"]),
        '2CC': Livery('1952_DK_Frichs_472_3_1980.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(1980, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_4',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_4_1997.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_472_4_1997.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_5',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_5_2009.png', cc_replace=colours["MAROON"], cc2_replace=colours["MAROON"]),
        '2CC': Livery('1952_DK_Frichs_472_5_2009.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(2009, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_473_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_473_1',
    name='GDS Frichs 473',
    liveries={
        'Default': Livery('1952_DK_Frichs_473_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["DCREAM"]),
        '2CC': Livery('1952_DK_Frichs_473_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_473_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_473_2',
    name='GDS Frichs 473',
    liveries={
        'Default': Livery('1952_DK_Frichs_473_2_1963.png', cc_replace=colours["MAROON"], cc2_replace=colours["DCREAM"]),
        '2CC': Livery('1952_DK_Frichs_473_2_1963.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1963, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_473_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_473_3',
    name='GDS Frichs 473',
    liveries={
        'Default': Livery('1952_DK_Frichs_473_3_2006.png', cc_replace=colours["MAROON"], cc2_replace=colours["DCREAM"]),
        '2CC': Livery('1952_DK_Frichs_473_3_2006.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_1',
    name='FFJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_1_1952.png', cc_replace=colours["MAROON"], cc2_replace=colours["GREY10"]),
        '2CC': Livery('1952_DK_Frichs_474_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_2',
    name='OHJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_2_1969.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_474_2_1969.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1969, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_3',
    name='OHJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_3_1986.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_474_3_1986.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1986, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_4',
    name='OHJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_4_1990.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_474_4_1990.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1990, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_5',
    name='OHJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_5_1993.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_474_5_1993.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1993, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_475_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_475_1',
    name='AHJ Frichs 475',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_1_1952.png', cc_replace=colours["RED"], cc2_replace=colours["GREY10"]),
        '2CC': Livery('1952_DK_Frichs_475_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_475_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_475_2',
    name='SB Frichs 475',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_2_1976.png', cc_replace=colours["MAROON"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_475_2_1976.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1976, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_475_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_475_3',
    name='SB Frichs 475',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_3_1977.png', cc_replace=colours["RED"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('1952_DK_Frichs_475_3_1977.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_475_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_475_4',
    name='AHJ Frichs 475',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_4_2008.png', cc_replace=colours["MAROON"], cc2_replace=colours["GREY10"]),
        '2CC': Livery('1952_DK_Frichs_475_4_2008.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)
