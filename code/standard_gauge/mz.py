import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, dsb_mz_sound

COMMON_mze_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(143),
    power=3300,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=117,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    sound_effects=dsb_mz_sound,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 7),
)

d_d_mz_i_1_dsb = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_i_1_dsb',
    name='DSB MZ I/II',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz1',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["MAROON"],
        cc2_replace=colours["DCREAM"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1967, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Note': 'MZ II introduced in 1970',
    }),
)

d_d_mz_i_2_dsb = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_i_2_dsb',
    name='DSB MZ I/II',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz1',),
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

d_d_mz_i_3_dsb = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_i_3_dsb',
    name='DSB MZ I/II',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz2',),
        paint=('dsb2',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1986, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_mz_i_4_ttt = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_i_4_ttt',
    name='TTT TMZ I',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz2',),
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
        'Trivia': 'One locomotive bought from TÅGAB in 2005 #1407',
    }),
)

d_d_mz_i_5_vida = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_i_5_vida',
    name='VIDA TMZ I',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz2',),
        paint=('vida1',),
        overlay=('light'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2004, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from STT in 2004 #1406',
    }),
)

d_d_mz_ii_4_taagab = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_ii_4_taagab',
    name='TÅGAB TMZ II',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz2',),
        paint=('tågab1',),
        overlay=('light'),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["RED"]
    ),
    country='sweden',
    company='taagab',
    introduction_date=date(2004, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two locomotives bought from DSB in 2004 #1423 & 2006 #1426',
    }),
)

d_d_mz_ii_5_ibab = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_ii_5_ibab',
    name='IBAB TMZ II',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz2',),
        paint=('ibab1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2012, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Two locomotives bought from NRFAB in 2012 #1421, named Cathis & 2013 #1413, named Betty',
    }),
)

d_d_mz_ii_6_stab = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_ii_6_stab',
    name='STAB TMZ II',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz2',),
        paint=('stab1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2015, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from DSB in 2015 #1425',
    }),
)

d_d_mz_ii_7_stab = Train(
    **COMMON_mze_PROPS,
    id='d_d_mz_ii_7_stab',
    name='STAB TMZ II',
    liveries=make_psd_cc_liveries(
        'pp/mz1.psd',
        shading=('mz2',),
        paint=('stab2',),
        overlay=('light'),
        cc_replace=colours["GREY9"],
        cc2_replace=colours["GREY3"]
    ),
    country='sweden',
    company='na',
    introduction_date=date(2013, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'One locomotive bought from Stena in 2010 #1418',
    }),
)

COMMON_mzl_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(165),
    power=3900,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    sound_effects=dsb_mz_sound,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 7),
)

d_d_mz_iii_1_dsb = Train(
    **COMMON_mzl_PROPS,
    id='d_d_mz_iii_1_dsb',
    name='DSB MZ III',
    liveries=make_psd_cc_liveries(
        'pp/mz3.psd',
        shading=('mz1',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    weight=125,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_mz_iii_2_dsb = Train(
    **COMMON_mzl_PROPS,
    id='d_d_mz_iii_2_dsb',
    name='DSB MZ III',
    liveries=make_psd_cc_liveries(
        'pp/mz3.psd',
        shading=('mz2',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1986, 1, 1),
    weight=125,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_mz_iv_1_dsb = Train(
    **COMMON_mzl_PROPS,
    id='d_d_mz_iv_1_dsb',
    name='DSB MZ IV',
    liveries=make_psd_cc_liveries(
        'pp/mz4.psd',
        shading=('mz1',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(1977, 1, 1),
    weight=123,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_mz_iv_2_dbcsc = Train(
    **COMMON_mzl_PROPS,
    id='d_d_mz_iv_2_dbcsc',
    name='DBCSC MZ IV',
    liveries=make_psd_cc_liveries(
        'pp/mz4.psd',
        shading=('mz1',),
        paint=('dbcsc1',),
        overlay=('light'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    company='na',
    introduction_date=date(2018, 1, 1),
    weight=123,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': 'Four locomotives bought from RSC in 2016 #1449, #1453, #1457 & #1459',
    }),
)
