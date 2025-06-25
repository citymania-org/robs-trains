import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

d_d_mye_ii_1_dsb = Train(
    id='d_d_mye_ii_1_dsb',
    name='DSB MY II (early)',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["DCREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(133),
    power=1700,
    introduction_date=date(1954, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=102,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's first mass-produced modern diesel locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 7),
)

COMMON_my_ii_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(133),
    power=1950,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=102,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 7),
)

d_d_my_ii_1_dsb = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_1_dsb',
    name='DSB MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["DCREAM"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1964, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'A more powerful version of the famous MY locomotive, like the MX it is still used today across Europe by private operators, often in pairs with other loco types such as the MZ & CFL 1800',
    }),
)

d_d_my_ii_2_dsb = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_2_dsb',
    name='DSB MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsb2',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_my_ii_3_ttt = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_3_ttt',
    name='TTT TMY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('ttt1',),
        overlay=('light'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2012, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two locomotives bought from Stena in 2010 #1110 & from RCT in 20XX #1157, in service by 2012',
    }),
)

d_d_my_ii_4_lt = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_4_lt',
    name='LT MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('lt1',),
        overlay=('light'),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["YELLOW"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2020, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from RTOG in 2015 #1145',
    }),
)

d_d_my_ii_5_contec = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_5_contec',
    name='Contec MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('contec1',),
        overlay=('light'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2009, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from CFLCD in 2008 #1158',
    }),
)

d_d_my_ii_6_mjbad = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_6_mjbad',
    name='MjbaD MY II "Victoria"',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('mjbad1',),
        overlay=('light'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2016, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from VLTJ in 2008 #1152, named Victoria',
    }),
)

d_d_my_ii_7_dsb = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_7_dsb',
    name='DSB MY II Service Locomotive "Den Flyvende Hollænder"',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsb3',),
        overlay=('light'),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Used to service & maintain Denmark's railways in the 90s #1108, named Den Flyvende Hollænder''',
    }),
)

d_d_my_ii_8_taagab = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_8_taagab',
    name='TÅGAB TMY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('tågab1',),
        overlay=('light'),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='taagab',
    introduction_date=date(1993, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Three locomotives bought from DSB in 1993 #1121, #1123, #1128 & a fourth also from DSB in 1996 #1113',
    }),
)

d_d_my_ii_9_taagab = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_9_taagab',
    name='TÅGAB TMY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('tågab2',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["ORANGE"]
    ),
    country='sweden',
    company='taagab',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''One locomotive bought from DSB in 1999 #1108, painted in the Great Northern style for it's role in the film "Dancer in the Dark" starring Björk''',
    }),
)

d_d_my_ii_10_dsb = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_10_dsb',
    name='DSB MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsb4',),
        overlay=('light'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["DBLUE"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2005, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '#1101 was the 1st locomotive of the MY class, it is now a museum train & was given a new livery in 2005 to commemorate the 200th anniversary of the birth of the famous Danish author Hans Christian Andersen, known for his works such as "The Little Mermaid" & "The Ugly Duckling"',
    }),
)

d_d_my_ii_11_dsb = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_11_dsb',
    name='DSB MY II Service Locomotive "Carina"',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsb5',),
        overlay=('light'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["YELLOW"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2004, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Used to service & maintain Denmark's railways in the 00s & later as a snow plough loco #1135, named Carina''',
    }),
)

d_d_my_ii_12_njj = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_12_njj',
    name='NJJ MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('njj1',),
        overlay=('light'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2002, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from DSB in 2002 #1146',
    }),
)

d_d_my_ii_13_cflcd = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_13_cflcd',
    name='CFLCD MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('cflcd1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["YELLOW"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2013, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from NJJ in 2008 #1146',
    }),
)

d_d_my_ii_14_vik = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_14_vik',
    name='VIK MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('cflcd1',),
        overlay=('light'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["YELLOW"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2023, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two locomotives bought from CFLCD in 2023 #1146 & #1152',
    }),
)

d_d_my_ii_15_bk = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_15_bk',
    name='BK TMY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('bk1',),
        overlay=('light'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2000, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from BSM in 2000 #1111',
    }),
)

d_d_my_ii_16_lj = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_16_lj',
    name='LJ MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('lj1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2002, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from DSB in 2002 #1153',
    }),
)

d_d_my_ii_17_bsbs = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_17_bsbs',
    name='BSBS MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('bsbs1',),
        overlay=('light'),
        cc_replace=colours["GREY8"],
        cc2_replace=colours["RED"]
    ),
    country='germany',
    company='na',
    introduction_date=date(2010, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from STRABAG in 2010 #1142',
    }),
)

d_d_my_ii_18_et = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_18_et',
    name='Euro-Track MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('et1',),
        overlay=('light'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1998, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Ten locomotives bought from DSB in 1998 & 1999',
    }),
)

d_d_my_ii_19_er = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_19_er',
    name='Eichholz Rail MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('er1',),
        overlay=('light'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from Euro-Track in 2003 #1147',
    }),
)

d_d_my_ii_20_strabag = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_20_strabag',
    name='STRABAG MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('strabag1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    country='germany',
    company='na',
    introduction_date=date(2007, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from Eichholz in 2007 #1125',
    }),
)

d_d_my_ii_21_mav = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_21_mav',
    name='MÁV MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('mav4',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    country='hungary',
    company='na',
    introduction_date=date(2012, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from STRABAG in 2012 #1125',
    }),
)

d_d_my_ii_22_et = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_22_et',
    name='Euro-Track MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('et1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from DSB in 1999 #1142',
    }),
)

d_d_my_ii_23_strabag = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_23_strabag',
    name='STRABAG MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('er1',),
        overlay=('light'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from Eichholz in 2007 #1131',
    }),
)

d_d_my_ii_24_bsx = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_24_bsx',
    name='BSX TMY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('bsx1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from DSB in 1996 #1111',
    }),
)
