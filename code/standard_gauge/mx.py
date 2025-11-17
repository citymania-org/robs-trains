import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_mx_ii_PROPS = dict(
    length=9,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(133),
    power=1445,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=89,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 7),
)

d_d_mx_ii_1_dsb = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_1_dsb',
    name='DSB MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["DCREAM"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Designed to be used on branch lines where a lighter locomotive is needed, like the MY it is still used today across Europe by private operators, often in pairs with other loco types such as the MZ & CFL 1800',
    }),
)

d_d_mx_ii_2_dsb = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_2_dsb',
    name='DSB MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
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

d_d_mx_ii_3_vltj = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_3_vltj',
    name='VLTJ MX II "Tørfisken"',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('vltj1',),
        overlay=('light'),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1994, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from DSB in 1993 #1025, named Tørfisken'
    }),
)

d_d_mx_ii_4_ttt = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_4_ttt',
    name='TTT TMX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
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
        'Trivia': 'One locomotive bought from RCT in 2012 #1015'
    }),
)

d_d_mx_ii_5_lb = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_5_lb',
    name='LB MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('lb1',),
        overlay=('light'),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["YELLOW"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2010, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from HFHJ in 2002 #1045'
    }),
)

d_d_mx_ii_6_lt = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_6_lt',
    name='LT MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('lt1',),
        overlay=('light'),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["YELLOW"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2017, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from RTOG in 2015 #1043'
    }),
)

d_d_mx_ii_7_contec = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_7_contec',
    name='Contec MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('contec1',),
        overlay=('light'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2010, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from CFLCD in 2009 #1008'
    }),
)

d_d_mx_ii_8_ohj = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_8_ohj',
    name='OHJ MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('ohj1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1987, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Three locomotives bought from DSB in 1987 #1008, #1009, #1010 & a fourth also from DSB in 1988 #1029'
    }),
)

d_d_mx_ii_9_sb = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_9_sb',
    name='SB MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('sb1',),
        overlay=('light'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1994, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two locomotives bought from DSB in 1993 #1041 & from OHJ in 1994 #1038, both sold to NJJ in 2001'
    }),
)

d_d_mx_ii_10_cflcd = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_10_cflcd',
    name='CFLCD MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('cflcd1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["YELLOW"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2009, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two locomotives bought from ØSJS & DJ in 2007 #1023 & #1029'
    }),
)

d_d_mx_ii_11_vik = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_11_vik',
    name='VIK MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
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
        'Trivia': 'One locomotive bought from CFLCD in 2023 #1029'
    }),
)

d_d_mx_ii_12_bk = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_12_bk',
    name='BK TMX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
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
        'Trivia': 'Two locomotives bought from BSM in 2000 #1024 & #1042'
    }),
)

d_d_mx_ii_13_lj = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_13_lj',
    name='LJ MX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('lj1',),
        overlay=('light'),
        cc_replace=colours["SCARLET"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1990, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two locomotives bought from DSB in 1988 #1031 & #1033'
    }),
)

d_d_mx_ii_14_bsx = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_14_bsx',
    name='BSX TMX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('bsx1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1994, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from DSB in 1994 #1012'
    }),
)

d_d_mx_ii_15_bsx = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_15_bsx',
    name='BSX TMX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('bsx2',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1994, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two locomotives bought from DSB in 1994 #1024 & #1042'
    }),
)

d_d_mx_ii_16_bsm = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_16_bsm',
    name='BSM TMX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('bsm1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from BSX in 1997 #1012'
    }),
)

d_d_mx_ii_17_stab = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_17_stab',
    name='STAB TMX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('stab1',),
        overlay=('light'),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["ORANGE"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2022, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from RCT in 2022 #1021'
    }),
)

d_d_mx_ii_18_vida = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_18_vida',
    name='VIDA TMX II',
    liveries=make_psd_cc_liveries(
        'pp/mx.psd',
        shading=('mx',),
        paint=('vida1',),
        overlay=('light'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2019, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive rented from NRFAB in 2019 #1024'
    }),
)
