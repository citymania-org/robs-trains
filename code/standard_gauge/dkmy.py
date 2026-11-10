import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, badges

d_d_mye_ii_1_dsb = Train(
    id='d_d_mye_ii_1_dsb',
    name='DSB MY II (MV II)',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsb1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["CREAM"]
    ),
    misc_flags=Train.Flags.USE_2CC,
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
        'Trivia': '''Denmark's first mass-produced modern diesel locomotive''',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/dsb'],
        'manufacturer': [],
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 6),
)

lu_d_1600_1_cfl = Train(
    id='lu_d_1600_1_cfl',
    name='CFL 1600',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('cfl1',),
        overlay=('bllight'),
        r_overlay=('bllightr'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["YELLOW"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=1750,
    introduction_date=date(1955, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=108,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'CFL bought four of these',
    }),
    badges=badges.set_train_badges({
        'flag': ['LU'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['LU/cfl'],
        'manufacturer': [],
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 6),
)

COMMON_my_ii_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
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
    visual_effect=(Train.VisualEffect.DIESEL, 6),
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
        r_overlay=('lightr'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["CREAM"]
    ),
    introduction_date=date(1964, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'A more powerful version of the famous MY locomotive, like the MX it is still used today across Europe by private operators, often in pairs with other loco types such as the MZ & CFL 1800',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/dsb'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    introduction_date=date(1972, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/dsb'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2012, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Two locomotives bought from Stena in 2010 #1110 & from RCT in 20XX #1157, in service by 2012',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['SE/ttt'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(2020, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from RTOG in 2015 #1145',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/lt'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(2009, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from CFLCD in 2008 #1158',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/contec'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2016, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from VLTJ in 2008 #1152, named Victoria',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/mjbad'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY10"]
    ),
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''Used to service & maintain Denmark's railways in the 90s #1108, named Den Flyvende Hollænder''',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/dsb'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(1993, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Three locomotives bought from DSB in 1993 #1121, #1123, #1128 & a fourth also from DSB in 1996 #1113',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['SE/taagab'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["MECONIUM"],
        cc2_replace=colours["ORANGE"]
    ),
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''One locomotive bought from DSB in 1999 #1108, painted in the Great Northern style for it's role in the film "Dancer in the Dark" starring Björk''',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['SE/taagab'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["NAVY"]
    ),
    introduction_date=date(2005, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '#1101 was the 1st locomotive of the MY class, it is now a museum train & was given a new livery in 2005 to commemorate the 200th anniversary of the birth of the famous Danish author Hans Christian Andersen, known for his works such as "The Little Mermaid" & "The Ugly Duckling"',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/dsb'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(2004, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''Used to service & maintain Denmark's railways in the 00s & later as a snow plough loco #1135, named Carina''',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/dsb'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["COBALT"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(2002, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from DSB in 2002 #1146',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/njj'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(2013, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from NJJ in 2008 #1146',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/cflcd'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(2023, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Two locomotives bought from CFLCD in 2023 #1146 & #1152',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/vik'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["BLUE"]
    ),
    introduction_date=date(2000, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from BSM in 2000 #1111',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['SE/bk'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["DBLUE"]
    ),
    introduction_date=date(2002, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from DSB in 2002 #1153',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/lj'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["GREY8"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2010, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from STRABAG in 2010 #1142',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DE/bsbs'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1998, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Ten locomotives bought from DSB in 1998 & 1999',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DE/et'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["DBLUE"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from Euro-Track in 2003 #1147',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DE/er'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    introduction_date=date(2007, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from Eichholz in 2007 #1125',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DE/strabag'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY3"]
    ),
    introduction_date=date(2012, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from STRABAG in 2012 #1125',
    }),
    badges=badges.set_train_badges({
        'flag': ['HU'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['HU/mav'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from DSB in 1999 #1142',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DE/et'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["GREY1"]
    ),
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from Eichholz in 2007 #1131',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DE/strabag'],
        'manufacturer': [],
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
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    introduction_date=date(1996, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from DSB in 1996 #1111',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['SE/bsx'],
        'manufacturer': [],
    }),
)

d_d_my_ii_25_strabag = Train(
    **COMMON_my_ii_PROPS,
    id='d_d_my_ii_25_strabag',
    name='STRABAG MY II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('strabag2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["YELLOW"]
    ),
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'One locomotive bought from Eichholz in 2007 and later painted in the "Kansas City" design #1151',
    }),
    badges=badges.set_train_badges({
        'flag': ['DE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DE/strabag'],
        'manufacturer': [],
    }),
)

hu_d_m61_1_mav = Train(
    id='hu_d_m61_1_mav',
    name='MÁV M61',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('mav1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["ORANGE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=1650,
    introduction_date=date(1963, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=106,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    visual_effect=(Train.VisualEffect.DIESEL, 6),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['HU'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['HU/mav'],
        'manufacturer': [],
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

hu_d_m61_2_mav = Train(
    id='hu_d_m61_2_mav',
    name='MÁV M61',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('mav2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["ORANGE"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=1650,
    introduction_date=date(1963, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=106,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    visual_effect=(Train.VisualEffect.DIESEL, 6),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['HU'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['HU/mav'],
        'manufacturer': [],
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)


hu_d_m61_3_mav = Train(
    id='hu_d_m61_3_mav',
    name='MÁV M61',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('mav3',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(105),
    power=1650,
    introduction_date=date(1963, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=106,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    visual_effect=(Train.VisualEffect.DIESEL, 6),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['HU'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['HU/mav'],
        'manufacturer': [],
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

COMMON_202_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=1750,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=108,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 6),
)

be_d_202_1_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_1_nmbs',
    name='NMBS HLD 202/203', # 1 stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('52/53',),
        paint=('nmbs1',),
        overlay=('bllight'),
        r_overlay=('bllightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(120),
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as HLD 52/53',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

be_d_202_2_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_2_nmbs',
    name='NMBS HLD 202/203', # 2 stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('52/53',),
        paint=('nmbs3',),
        overlay=('bllight'),
        r_overlay=('bllightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(120),
    introduction_date=date(1955, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as HLD 52/53',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

be_d_202_3_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_3_nmbs',
    name='NMBS HLD 52/53', # thick stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('52/53',),
        paint=('nmbs2',),
        overlay=('bllight'),
        r_overlay=('bllightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(120),
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

be_d_202_4_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_4_nmbs',
    name='њNMBS HLD 52/53', # modern
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(120),
    introduction_date=date(1979, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'New cab to improve drivability',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

be_d_202_5_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_5_nmbs',
    name='NMBS HLD 204', # 1 stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('nmbs1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(140),
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as HLD 54',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

be_d_202_6_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_6_nmbs',
    name='NMBS HLD 204', # 2 stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('nmbs3',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(140),
    introduction_date=date(1957, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Later classed as HLD 54',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

be_d_202_7_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_7_nmbs',
    name='NMBS HLD 54', # thick stripe
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('nmbs2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(140),
    introduction_date=date(1970, 1, 1),
    additional_text=grf.fake_vehicle_info({
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)

be_d_202_8_nmbs = Train(
    **COMMON_202_PROPS,
    id='be_d_202_8_nmbs',
    name='њNMBS HLD 54', # modern
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('9a',),
        paint=('9b',),
        cc_replace=colours["DGREEN"],
        cc2_replace=colours["YELLOW"]
    ),
    max_speed=Train.kmhish(120),
    introduction_date=date(1979, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'New cab to improve drivability',
    }),
    badges=badges.set_train_badges({
        'flag': ['BE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['BE/nmbs'],
        'manufacturer': [],
    }),
)
