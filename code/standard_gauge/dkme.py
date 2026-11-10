import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge, badges

COMMON_me_ii_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    max_speed=Train.kmhish(175),
    power=3300,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=122,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
    visual_effect=(Train.VisualEffect.DIESEL, 6),
)

d_d_me_ii_1_dsb = Train(
    **COMMON_me_ii_PROPS,
    id='d_d_me_ii_1_dsb',
    name='DSB ME II',
    liveries=make_psd_cc_liveries(
        'pp/me.psd',
        shading=('me',),
        paint=('dsb1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY10"]
    ),
    introduction_date=date(1981, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''Denmark's final diesel locomotive''',
    }),
    badges=badges.set_train_badges({
        'flag': ['DK'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['DK/dsb'],
        'manufacturer': [],
    }),
)

d_d_me_ii_2_dsb = Train(
    **COMMON_me_ii_PROPS,
    id='d_d_me_ii_2_dsb',
    name='DSB ME II',
    liveries=make_psd_cc_liveries(
        'pp/me.psd',
        shading=('me',),
        paint=('dsb2',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["NAVY"]
    ),
    introduction_date=date(2000, 1, 1),
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

d_d_me_ii_3_dsb = Train(
    **COMMON_me_ii_PROPS,
    id='d_d_me_ii_3_dsb',
    name='DSB ME II',
    liveries=make_psd_cc_liveries(
        'pp/me.psd',
        shading=('me',),
        paint=('dsb3',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["NAVY"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2002, 1, 1),
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

d_d_me_ii_4_dsb = Train(
    **COMMON_me_ii_PROPS,
    id='d_d_me_ii_4_dsb',
    name='DSB ME II',
    liveries=make_psd_cc_liveries(
        'pp/me.psd',
        shading=('me',),
        paint=('dsb4',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    introduction_date=date(2016, 1, 1),
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

d_d_me_ii_5_nrfab = Train(
    **COMMON_me_ii_PROPS,
    id='d_d_me_ii_5_nrfab',
    name='NRFAB TME II',
    liveries=make_psd_cc_liveries(
        'pp/me.psd',
        shading=('me',),
        paint=('nrfab1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["APPLE"]
    ),
    introduction_date=date(2020, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Eight locomotives bought from DSB in 2020 #1509, #1513 & #1527 & in 2021 #1504, #1518, #1523, #1525 & #1529',
    }),
    badges=badges.set_train_badges({
        'flag': ['SE'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['SE/nrfab'],
        'manufacturer': [],
    }),
)

d_d_me_ii_6_mav = Train(
    **COMMON_me_ii_PROPS,
    id='d_d_me_ii_6_mav',
    name='MÁV TME II',
    liveries=make_psd_cc_liveries(
        'pp/me.psd',
        shading=('me',),
        paint=('mav1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["SKY"]
    ),
    introduction_date=date(2024, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Fifteen locomotives leased from NRFAB in 2024',
    }),
    badges=badges.set_train_badges({
        'flag': ['HU'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['HU/mav'],
        'manufacturer': [],
    }),
)

d_d_me_ii_7_skpl = Train(
    **COMMON_me_ii_PROPS,
    id='d_d_me_ii_7_skpl',
    name='SKPL SU175',
    liveries=make_psd_cc_liveries(
        'pp/me.psd',
        shading=('me',),
        paint=('skpl1',),
        overlay=('light'),
        r_overlay=('lightr'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY7"]
    ),
    introduction_date=date(2022, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'Six locomotives leased from NRFAB in 2022',
    }),
    badges=badges.set_train_badges({
        'flag': ['PL'],
        'role': ['freight', 'regional_passenger', 'express_passenger'],
        'power': ['diesel'],
        'operator': ['PL/skpl'],
        'manufacturer': [],
    }),
)
