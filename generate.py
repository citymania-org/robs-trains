import os
from datetime import date

import grf

import lib

from common import g, Livery, Train, modern_diesel_sound, standard_gauge, standard_gauge_15kv, standard_gauge_25kv, standard_gauge_dc, standard_gauge_multi, metro, p_gauge, make_psd_cc_liveries, colours


PURCHASE_ICONS_DIR = 'purchase list'
DEBUG_DIR = 'debug'

os.makedirs(DEBUG_DIR, exist_ok=True)

# steam

s_s_N_ii_1_sj = Train(
    id='s_s_N_ii_1_sj',
    name='SJ N II',
    length=5,
    liveries={
        'Default': Livery('1900_SE_N_II_1.png', cc_replace=colours["GREY10"], cc2_replace=colours["GREY10"]),
        '2CC': Livery('1900_SE_N_II_1.png', auto_cc=lib.CC_DEFAULT),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='steam',
    engine_class=Train.EngineClass.STEAM,
    track_type=standard_gauge,
    max_speed=Train.kmhish(45),
    power=1000, # come up with value
    introduction_date=date(1900, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=55,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Shunting',
        'Builder': 'Multiple',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

s_s_Sa_sj = Train(
    id='s_s_Sa_sj',
    name='SJ Sa',
    length=5,
    liveries=make_psd_cc_liveries(
        'pp/1908_SE_Sa.psd',
        shading='Sa',
        paint='SJ',
        overlay=('Lights'),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY10"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='steam',
    engine_class=Train.EngineClass.STEAM,
    track_type=standard_gauge,
    max_speed=Train.kmhish(45),
    power=1000, # come up with value
    introduction_date=date(1908, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=60,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'universal',
        'Builder': 'Multiple',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

# diesel

# frichs marcipanbrød

'''
from code.standard_gauge.dk467 import d_d_frichs_467_1, d_d_frichs_467_2, d_d_frichs_467_3, d_d_frichs_467_4, d_d_frichs_467_5, d_d_frichs_468_1, d_d_frichs_468_2, d_d_frichs_468_3, d_d_frichs_469_1, d_d_frichs_469_2, d_d_frichs_469_3, d_d_frichs_469_4, d_d_frichs_469_8, d_d_frichs_469_5, d_d_frichs_469_6, d_d_frichs_469_7, d_d_frichs_471_1, d_d_frichs_471_2, d_d_frichs_471_3, d_d_frichs_471_4, d_d_frichs_471_5, d_d_frichs_471_6, d_d_frichs_472_1, d_d_frichs_472_2, d_d_frichs_472_3, d_d_frichs_472_4, d_d_frichs_472_5, d_d_frichs_473_1, d_d_frichs_473_2, d_d_frichs_473_3, d_d_frichs_474_1, d_d_frichs_474_2, d_d_frichs_474_3, d_d_frichs_474_4, d_d_frichs_474_5, d_d_frichs_475_1, d_d_frichs_475_2, d_d_frichs_475_3, d_d_frichs_475_4
'''

from code.standard_gauge.be201 import be_d_201_1_nmbs, be_d_201_2_nmbs, be_d_201_3_nmbs, be_d_201_4_nmbs

# nohab

from code.standard_gauge.nohab import hu_d_m61_1_mav, hu_d_m61_2_mav, hu_d_m61_3_mav, hu_d_m61_4_mav

from code.standard_gauge.my import d_d_mye_ii_1_dsb, d_d_my_ii_1_dsb, d_d_my_ii_2_dsb, d_d_my_ii_8_taagab, d_d_my_ii_7_dsb, d_d_my_ii_9_taagab, d_d_my_ii_12_njj, d_d_my_ii_11_dsb, d_d_my_ii_10_dsb, d_d_my_ii_5_contec, d_d_my_ii_3_ttt, d_d_my_ii_13_cflcd, d_d_my_ii_6_mjbad, d_d_my_ii_4_lt, d_d_my_ii_14_vik
        
from code.standard_gauge.mx import d_d_mx_ii_1_dsb, d_d_mx_ii_2_dsb, d_d_mx_ii_8_ohj, d_d_mx_ii_3_vltj, d_d_mx_ii_9_sb, d_d_mx_ii_10_cflcd, d_d_mx_ii_7_contec, d_d_mx_ii_5_lb, d_d_mx_ii_4_ttt, d_d_mx_ii_6_lt, d_d_mx_ii_11_vik

# toaster

from code.standard_gauge.mz import d_d_mz_i_1_dsb, d_d_mz_i_2_dsb, d_d_mz_i_3_dsb, d_d_mz_i_4_ttt, d_d_mz_ii_1_dsb, d_d_mz_ii_2_dsb, d_d_mz_ii_3_dsb, d_d_mz_ii_4_taagab, d_d_mz_ii_5_ibab, d_d_mz_iii_1_dsb, d_d_mz_iii_2_dsb, d_d_mz_iv_1_dsb, d_d_mz_iv_2_dbcsc

from code.standard_gauge.me import d_d_me_ii_1_dsb, d_d_me_ii_2_dsb, d_d_me_ii_3_dsb, d_d_me_ii_4_dsb, d_d_me_ii_5_nrfab, d_d_me_ii_6_mav, d_d_me_ii_7_skpl

# electric 15

'''
rc1 = Train(
    id='rc1',
    name='Rc1',
    shorten_by=2,
    liveries=make_liveries(6, {
        'Orange & Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue & Red': '1967_SE_Rc1_2_1990.png',
    }),
    country='sweden',
    company='na',
    power_type='15kv',
    purchase_sprite_towed_id='rc1',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1967, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

rc2 = Train(
    id='rc2',
    name='Rc2',
    shorten_by=2,
    liveries=make_liveries(6, {
        'Orange & Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue & Red Old': '1967_SE_Rc1_2_1990.png',
        'Blue & Red New': '1969_SE_Rc2_3_1990.png',
        'Black': '1969_SE_Rc2_4_2006.png',
    }),
    country='sweden',
    company='na',
    power_type='15kv',
    purchase_sprite_towed_id='rc2',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1969, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

rc3 = Train(
    id='rc3',
    name='Rc3',
    shorten_by=2,
    liveries=make_liveries(6, {
        'Orange & Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue & Red': '1969_SE_Rc2_3_1990.png',
        'Black': '1969_SE_Rc2_4_2006.png',
    }),
    country='sweden',
    company='na',
    power_type='15kv',
    purchase_sprite_towed_id='rc3',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1970, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

rc4 = Train(
    id='rc4',
    name='Rc4',
    shorten_by=2,
    liveries=make_liveries(6, {
        'Orange & Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue & Red': '1969_SE_Rc2_3_1990.png',
    }),
    country='sweden',
    company='na',
    power_type='15kv',
    purchase_sprite_towed_id='rc4',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1975, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

rc5 = Train(
    id='rc5',
    name='Rc5',
    shorten_by=2,
    liveries=make_liveries(6, {
        'Orange & Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue & Red': '1969_SE_Rc2_3_1990.png',
    }),
    country='sweden',
    company='na',
    power_type='15kv',
    purchase_sprite_towed_id='rc5',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1982, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

rc6 = Train(
    id='rc6',
    name='Rc6',
    shorten_by=2,
    liveries=make_liveries(6, {
        'Orange & Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue & Red': '1969_SE_Rc2_3_1990.png',
        'Dark Blue': '1984_SE_Rc6_1_2005.png',
        'Black': '1969_SE_Rc2_4_2006.png',
    }),
    country='sweden',
    company='na',
    power_type='15kv',
    purchase_sprite_towed_id='rc6',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_15kv,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1984, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'A Cool train',
    }),
)'''

# electric 25

from code.standard_gauge.ea import d_e_ea_1_dsb, d_e_ea_2_dsb, d_e_ea_4_bulmarket, d_e_ea_5_db, d_e_ea_3_dsb

# electric dc

# electric 3rd

# dmu

d_d_ml_1_dsb = Train(
    id='d_d_ml_1_dsb',
    name='?DSB ML',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/w_ml.psd',
        shading=('ml',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(75),
    power=240,
    introduction_date=date(1929, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=44,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

d_d_ml_2_dsb = Train(
    id='d_d_ml_2_dsb',
    name='?DSB ML',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/w_ml.psd',
        shading=('ml',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=colours["BROWN"],
        cc2_replace=colours["BROWN"]
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(75),
    power=300,
    introduction_date=date(1945, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=44,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=70,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
    }),
)

from code.standard_gauge.mq import d_d_mq_1_dsb, d_d_mp_1_dsb, d_d_mo_ii_1_dsb, d_d_mo_iv_1_dsb, d_d_mo_v_1_dsb

from code.standard_gauge.Yd import s_d_Yd_1_sj, s_d_Yd_2_hnj, s_d_Yd_3_msj

from code.standard_gauge.Yo import s_d_Yo_1_sj, s_d_Yo_2_hnj

from code.standard_gauge.Yo1s import s_d_Yo1s_1_sj, s_d_Yo1s_2_bj, s_d_Yo1s_3_tgoj

'''
mf_ic3 = Train(
    id='mf_ic3',
    name='MF IC3',
    liveries=make_liveries(8, {
        'White & Red': '1989_DK_MF_IC3_MFA_1_1989.png',
        'Grey, Blue & Green': '1989_DK_MF_IC3_MFA_2_2005.png',
        'Grey, Blue & Red': '1989_DK_MF_IC3_MFA_3_2012.png',
        'Red & Black': '1989_DK_MF_IC3_MFA_4_2018.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='mf_ic3_car2',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1989, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
).add_articulated_part(
    id='mf_ic3_car2',
    liveries=make_liveries(8, {
        'White & Red': '1989_DK_MF_IC3_FF_1_1989.png',
        'Grey, Blue & Green': '1989_DK_MF_IC3_FF_2_2005.png',
        'Grey, Blue & Red': '1989_DK_MF_IC3_FF_3_2012.png',
        'Red & Black': '1989_DK_MF_IC3_FF_4_2018.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='mf_ic3_car3',
    liveries=make_liveries(8, {
        'White & Red': '1989_DK_MF_IC3_MFB_1_1989.png',
        'Grey, Blue & Green': '1989_DK_MF_IC3_MFB_2_2005.png',
        'Grey, Blue & Red': '1989_DK_MF_IC3_MFB_3_2012.png',
        'Red & Black': '1989_DK_MF_IC3_MFB_4_2018.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)'''

# emu 15

from code.standard_gauge.Xoa4 import s_e_Xoa4_1_sj, s_e_Xoa4_2_sj, s_e_Cox4_1_sj, s_e_Cox4_2_sj

from code.standard_gauge.Xoa3 import s_e_Xoa3_1_bj, s_e_Xoa3_2_sj

from code.standard_gauge.X1 import s_e_X1_1_sj, s_e_X1_2_sl, s_e_X1_3_sl

# emu 25

'''
er_ir4 = Train(
    id='er_ir4',
    name='ER IR4',
    liveries=make_liveries(8, {
        'White & Red': '1993_DK_ER_IR4_ER20_1_1993.png',
        'Grey, Blue & Green': '1993_DK_ER_IR4_ER20_2_2005.png',
        'Grey, Blue & Red': '1993_DK_ER_IR4_ER20_3_2012.png',
        'Red & Black': '1993_DK_ER_IR4_ER20_4_2021.png',
    }),
    country='denmark',
    company='na',
    power_type='25kv',
    purchase_sprite_towed_id='er_ir4_car2',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_25kv,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1993, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
).add_articulated_part(
    id='er_ir4_car2',
    liveries=make_liveries(8, {
        'White & Red': '1993_DK_ER_IR4_FR22_1_1993.png',
        'Grey, Blue & Green': '1993_DK_ER_IR4_FR22_2_2005.png',
        'Grey, Blue & Red': '1993_DK_ER_IR4_FR22_3_2012.png',
        'Red & Black': '1993_DK_ER_IR4_FR22_4_2021.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='er_ir4_car3',
    liveries=make_liveries(8, {
        'White & Red': '1993_DK_ER_IR4_FR23_1_1993.png',
        'Grey, Blue & Green': '1993_DK_ER_IR4_FR23_2_2005.png',
        'Grey, Blue & Red': '1993_DK_ER_IR4_FR23_3_2012.png',
        'Red & Black': '1993_DK_ER_IR4_FR23_4_2021.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='er_ir4_car4',
    liveries=make_liveries(8, {
        'White & Red': '1993_DK_ER_IR4_ER21_1_1993.png',
        'Grey, Blue & Green': '1993_DK_ER_IR4_ER21_2_2005.png',
        'Grey, Blue & Red': '1993_DK_ER_IR4_ER21_3_2012.png',
        'Red & Black': '1993_DK_ER_IR4_ER21_4_2021.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)'''

# emu dc

from code.standard_gauge.HKB_Wes_1 import n_o_Wes_1_hkb

from code.standard_gauge.OS_T import n_o_T_1_os, n_o_T_2_os

'''stog_1_2 = Train(
    id='stog_1_2',
    name='S-Tog 1 (2 Car)',
    liveries=make_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_MM_1_1933.png',
    }),
    country='denmark',
    company='stog',
    power_type='dc',
    purchase_sprite_towed_id='stog_1_2_car2',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_dc,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1933, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Can be combined with 2 & 4 car sets to make sets of 6 & 8',
    }),
).add_articulated_part(
    id='stog_1_2_car2',
    liveries=make_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FS_1_1933.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

stog_1_4 = Train(
    id='stog_1_4',
    name='S-Tog 1 (4 Car)',
    liveries=make_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_MM_1_1933.png',
    }),
    country='denmark',
    company='stog',
    power_type='dc',
    purchase_sprite_towed_id='stog_1_4_car2',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_dc,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1933, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Can be combined with 2 & 4 car sets to make sets of 6 & 8',
    }),
).add_articulated_part(
    id='stog_1_4_car2',
    liveries=make_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FM_1_1933.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='stog_1_4_car3',
    liveries=make_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FM_1_1933.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='stog_1_4_car4',
    liveries=make_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FS_1_1933.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)'''

# emu 3rd

from code.standard_gauge.C1 import s_e_C1_1_ss

# carriages

'''abs1 = Train(
    id='abs1',
    name='ABs',
    liveries=make_liveries(11, {
        'White, Blue & Green': '2002_DK_ABs_1_2002.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=0,
    introduction_date=date(2002, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

abs2 = Train(
    id='abs2',
    name='ABs',
    liveries=make_liveries(11, {
        'White, Blue & Red': '2002_DK_ABs_2_2012.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=0,
    introduction_date=date(2012, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

b_ii1 = Train(
    id='b_ii1',
    name='B II',
    liveries=make_liveries(10, {
        'White, Blue & Green': '2002_DK_B_II_1_2002.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=0,
    introduction_date=date(2002, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

b_ii2 = Train(
    id='b_ii2',
    name='B II',
    liveries=make_liveries(10, {
        'White, Blue & Red': '2002_DK_B_II_2_2012.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=0,
    introduction_date=date(2012, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)'''

from code.standard_gauge.dk30stock import d_p_cr_1_dsb, d_p_ca_1_dsb, d_p_car_1_dsb, d_p_cae_1_dsb, d_p_ac_i_1_dsb, d_p_ac_ii_1_dsb, d_p_ag_1_dsb, d_p_ag_2_dsb, d_p_au_1_dsb, d_p_aul_1_dsb, d_p_av_1_dsb, d_p_abv_1_dsb, d_p_abg_1_dsb, d_p_bv_1_dsb, d_p_cc_1_dsb, d_p_bg_1_dsb, d_p_bg_2_dsb, d_p_b_1_lj, d_p_b_2_lj

from code.standard_gauge.uicy import d_p_a_1_dsb, d_p_a_2_dsb, d_p_a_3_dsb, d_p_ab_1_dsb, d_p_ab_2_dsb, d_p_ab_3_dsb, d_p_b_1_dsb, d_p_b_i_1_dsb, d_p_bk_i_1_dsb, d_p_bk_i_2_dsb, d_p_bd_1_dsb, d_p_bd_2_dsb, d_p_an_1_dsb, d_p_an_2_dsb, d_p_an_3_dsb, d_p_bn_1_dsb, d_p_bn_2_dsb, d_p_bn_3_dsb, d_p_bn_4_dsb, d_p_bn_5_dsb, d_p_bn_6_dsb, fr_p_a_1_sncf, fr_p_a_2_sncf, fr_p_a_3_sncf, fr_p_ab_1_sncf, fr_p_ab_2_sncf, fr_p_ab_3_sncf, fr_p_b_1_sncf, fr_p_b_2_sncf, fr_p_b_3_sncf, fr_p_ad_1_sncf, fr_p_ad_2_sncf, fr_p_ad_3_sncf, fr_p_bd_1_sncf, fr_p_bd_2_sncf

d_p_b_ii_1_dsb = Train(
    id='d_p_b_ii_1_dsb',
    name='DSB B II',
    length=12,
    liveries={
        'Default': Livery('2002_DK_B_II_1_2002.png', cc_replace=colours["COLBALT"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('2002_DK_B_II_1_2002.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('2002_DK_B_II_1_2002.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(2002, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=50,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=110,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_b_ii_2_dsb = Train(
    id='d_p_b_ii_2_dsb',
    name='DSB B II',
    length=12,
    liveries={
        'Default': Livery('2002_DK_B_II_2_2012.png', cc_replace=colours["COLBALT"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('2002_DK_B_II_2_2012.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('2002_DK_B_II_2_2012.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(2012, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=50,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=110,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_bk_iii_1_dsb = Train(
    id='d_p_bk_iii_1_dsb',
    name='DSB Bk III',
    length=12,
    liveries={
        'Default': Livery('2002_DK_Bk_III_1_2002.png', cc_replace=colours["COLBALT"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('2002_DK_Bk_III_1_2002.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('2002_DK_Bk_III_1_2002.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(2002, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=50,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=102,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_bk_iii_2_dsb = Train(
    id='d_p_bk_iii_2_dsb',
    name='DSB Bk III',
    length=12,
    liveries={
        'Default': Livery('2002_DK_Bk_III_2_2012.png', cc_replace=colours["COLBALT"], cc2_replace=colours["GREY1"]),
        '2CC': Livery('2002_DK_Bk_III_2_2012.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('2002_DK_Bk_III_2_2012.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(2012, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=50,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=102,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

# wagons

s_w_Gblssy_2_gc = Train(
    id='s_w_Gblssy_2_gc',
    name='GC Gblss-y',
    length=7,
    liveries={
        'Default': Livery('2000_SE_Gblssy_2_2000.png'),
        '2CC': Livery('2000_SE_Gblssy_2_2000.png', mask='2000_SE_Gblssy_2_2000_MASK.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(2000, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=17,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=1, # to be decided
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.MAIL,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Dedicated mail trains',
    }),
)

s_w_Hbis_sj = Train(
    id='s_w_Hbis_sj',
    name='SJ Hbis',
    length=7,
    liveries={
        'Default': Livery('1972_SE_Hbis_1972.png', cc_replace=colours["REDBROWN"], cc2_replace=colours["REDBROWN"]),
        '2CC': Livery('1972_SE_Hbis_1972.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1972_SE_Hbis_1972.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(100),
    power=0,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=17,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=1, # to be decided
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PIECE_GOODS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Freight',
    }),
)

# 891mm narrow gauge

from code.narrow_gauge.X10p import s_p_UBp_ii_1, s_e_X10p_1_sl, s_e_X10p_2_sl

from code.narrow_gauge.Z4p import s_d_Z4p_1_srj, s_d_Z4p_2, s_d_Z4p_3_nklj, s_d_Z4p_4, s_d_Z4p_5_donj, s_d_Z4p_6_sl, s_d_Z4p_7_sl

from code.narrow_gauge.other import s_d_Tp_1_sj, s_p_Co_1

'''

x15p = Train(
    id='x15p',
    name='X15p',
    length=9,
    liveries=make_liveries({
        'Original': 'xxxx_SE_X10p_X10p_1_xxxx.png',
    }),
    country='sweden', 
    company='sl',
    power_type='dc',
    purchase_sprite_towed_id='x15p_car2',
    engine_class=Train.EngineClass.ELECTRIC, 
    sound_effects=modern_diesel_sound,
    track_type=p_gauge_dc,
    max_speed=Train.kmhish(120),
    power=536,
    introduction_date=date(1990, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(27.7+15.8+16.6)),
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=72,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Needs stats',
    }),
).add_articulated_part(
    id='x15p_car2',
    length=9,
    liveries=make_liveries({
        'Original': 'xxxx_SE_X10p_UBp_1_xxxx.png',
    }),
    cargo_capacity=80,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='x15p_car3',
    length=9,
    liveries=make_liveries({
        'Original': 'xxxx_SE_X10p_UBxp_1_xxxx.png',
    }),
    cargo_capacity=76,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
'''
purchase_icon = lambda fname: grf.FileSprite(grf.ImageFile(os.path.join(PURCHASE_ICONS_DIR, fname)), 0, 0, None, None)


COUNTRY_SPRITES = {
    'austria': purchase_icon('fat.png'),
    'belgium': purchase_icon('fbe.png'),
    'bulgaria': purchase_icon('fbg.png'),
    'switzerland': purchase_icon('fch.png'),
    'czechrepublic': purchase_icon('fcz.png'),
    'germany': purchase_icon('fde.png'),
    'denmark': purchase_icon('fdk.png'),
    'france': purchase_icon('ffr.png'),
    'hrvatska': purchase_icon('fhr.png'),
    'hungary': purchase_icon('fhu.png'),
    'italy': purchase_icon('fit.png'),
    'luxembourg': purchase_icon('flu.png'),
    'norway': purchase_icon('fno.png'),
    'poland': purchase_icon('fpl.png'),
    'srbija': purchase_icon('frs.png'),
    'russia': purchase_icon('fru.png'),
    'sweden': purchase_icon('fse.png'),
    'slovenija ': purchase_icon('fsi.png'),
    'slovakia ': purchase_icon('fsk.png'),
    'ussr': purchase_icon('fsu.png'),
    'jugoslavija': purchase_icon('fyu.png'),
    'na': purchase_icon('blank.png'),
}


COMPANY_SPRITES = {
    'na': purchase_icon('blank.png'),
    'cmetro': purchase_icon('lcmetro.png'),
    'øresundståg': purchase_icon('loeresundstaag.png'),
    'stog': purchase_icon('lstog.png'),
    'sl': purchase_icon('lsl.png'),
    'taagab': purchase_icon('ltaagab.png'),
    'sj_70s': purchase_icon('lsj70s.png'),
    'tgojnew': purchase_icon('ltgojnew.png'),
    'maelartaag': purchase_icon('lmaelartaag.png'),
    'hectorrail': purchase_icon('lhectorrail.png'),
    'ss': purchase_icon('lss.png'),
}


POWER_TYPE_SPRITES = {
    'diesel': purchase_icon('pdiesel.png'),
    '3rd': purchase_icon('pelectric3.png'),
    'dual': purchase_icon('pelectricdv.png'),
    'metro': purchase_icon('pelectric3.png'),
    'steam': purchase_icon('psteam.png'),
    'multi': purchase_icon('pelectricdv.png'),  # replece these sprites
    'dc': purchase_icon('pelectricdc1500.png'),
    'dc3000': purchase_icon('pelectricdc3000.png'),
    '15kv': purchase_icon('pelectric15.png'),
    '25kv': purchase_icon('pelectric25.png'),
    'na': purchase_icon('blank.png')
}

lib.make_purchase_sprites(
    newgrf=g,
    xofs=-29,
    yofs=-9,
    parts=[
        {
            'offset': (0, 1),
            'property': 'country',
            'sprites': COUNTRY_SPRITES,
        }, {
            'offset': (2, 1),
            'property': 'company',
            'sprites': COMPANY_SPRITES,
        }, {
            'offset': (2, 1),
            'property': 'power_type',
            'sprites': POWER_TYPE_SPRITES,
        }, {
            'offset': (10, 10),
            'property': 'self',
        }, {
            'offset': (-1, 10),
            'property': 'towed[0]',
        }, {
            'offset': (-1, 10),
            'property': 'towed[1]',
        },
    ],
    effects={
        'crop_x': 127,
        'checker': (-4, 4),
    },
    # debug_dir=DEBUG_DIR,
)

# chronological order within the categories
# standard gauge -> narrow gauge
(g.add(grf.SetPurchaseOrder(
    # steam
    s_s_N_ii_1_sj,
    s_s_Sa_sj,
    # diesel
    #grf.VariantGroup('Frichs 467-475 "Marcipanbrød"', d_d_frichs_467_1, d_d_frichs_467_2, d_d_frichs_467_3, d_d_frichs_467_4, d_d_frichs_467_5, d_d_frichs_468_1, d_d_frichs_468_2, d_d_frichs_468_3, d_d_frichs_469_1, d_d_frichs_469_2, d_d_frichs_469_3, d_d_frichs_469_4, d_d_frichs_469_8, d_d_frichs_469_5, d_d_frichs_469_6, d_d_frichs_469_7, d_d_frichs_471_1, d_d_frichs_471_2, d_d_frichs_471_3, d_d_frichs_471_4, d_d_frichs_471_5, d_d_frichs_471_6, d_d_frichs_472_1, d_d_frichs_472_2, d_d_frichs_472_3, d_d_frichs_472_4, d_d_frichs_472_5, d_d_frichs_473_1, d_d_frichs_473_2, d_d_frichs_473_3, d_d_frichs_474_1, d_d_frichs_474_2, d_d_frichs_474_3, d_d_frichs_474_4, d_d_frichs_474_5, d_d_frichs_475_1, d_d_frichs_475_2, d_d_frichs_475_3, d_d_frichs_475_4),
    grf.VariantGroup('201', be_d_201_1_nmbs, be_d_201_2_nmbs, be_d_201_3_nmbs, be_d_201_4_nmbs),
    d_d_mye_ii_1_dsb,
    grf.VariantGroup('MX II', d_d_mx_ii_1_dsb, d_d_mx_ii_2_dsb, d_d_mx_ii_8_ohj, d_d_mx_ii_3_vltj, d_d_mx_ii_9_sb, d_d_mx_ii_10_cflcd, d_d_mx_ii_7_contec, d_d_mx_ii_5_lb, d_d_mx_ii_4_ttt, d_d_mx_ii_6_lt, d_d_mx_ii_11_vik),
    grf.VariantGroup('M61', hu_d_m61_1_mav, hu_d_m61_2_mav, hu_d_m61_3_mav, hu_d_m61_4_mav),
    grf.VariantGroup('MY II', d_d_my_ii_1_dsb, d_d_my_ii_2_dsb, d_d_my_ii_8_taagab, d_d_my_ii_7_dsb, d_d_my_ii_9_taagab, d_d_my_ii_12_njj, d_d_my_ii_11_dsb, d_d_my_ii_10_dsb, d_d_my_ii_5_contec, d_d_my_ii_3_ttt, d_d_my_ii_13_cflcd, d_d_my_ii_6_mjbad, d_d_my_ii_4_lt, d_d_my_ii_14_vik),
    grf.VariantGroup('MZ I', d_d_mz_i_1_dsb, d_d_mz_i_2_dsb, d_d_mz_i_3_dsb, d_d_mz_i_4_ttt),
    grf.VariantGroup('MZ II', d_d_mz_ii_1_dsb, d_d_mz_ii_2_dsb, d_d_mz_ii_3_dsb, d_d_mz_ii_4_taagab, d_d_mz_ii_5_ibab),
    grf.VariantGroup('MZ III', d_d_mz_iii_1_dsb, d_d_mz_iii_2_dsb),
    grf.VariantGroup('MZ IV', d_d_mz_iv_1_dsb, d_d_mz_iv_2_dbcsc),
    grf.VariantGroup('ME II', d_d_me_ii_1_dsb, d_d_me_ii_2_dsb, d_d_me_ii_3_dsb, d_d_me_ii_4_dsb, d_d_me_ii_5_nrfab, d_d_me_ii_7_skpl, d_d_me_ii_6_mav),
    # electric 15
    #grf.VariantGroup(
    #    'Rc',
        #rc1,
        #rc2,
        #rc3,
        #rc4,
        #rc5,
        #rc6,
    #),
    # electric 25
    grf.VariantGroup('EA', d_e_ea_1_dsb, d_e_ea_2_dsb, d_e_ea_4_bulmarket, d_e_ea_5_db, d_e_ea_3_dsb),
    # electric dc
    # electric 3rd
    # dmu
    d_d_ml_1_dsb,
    d_d_ml_2_dsb,
    d_d_mq_1_dsb,
    d_d_mp_1_dsb,
    grf.VariantGroup('MO', d_d_mo_ii_1_dsb, d_d_mo_iv_1_dsb, d_d_mo_v_1_dsb),
    grf.VariantGroup('Yd', s_d_Yd_1_sj, s_d_Yd_2_hnj, s_d_Yd_3_msj),
    grf.VariantGroup('Yo', s_d_Yo_1_sj, s_d_Yo_2_hnj),
    grf.VariantGroup('Yo1s', s_d_Yo1s_1_sj, s_d_Yo1s_2_bj, s_d_Yo1s_3_tgoj),
    #mf_ic3,
    # emu 15
    grf.VariantGroup('Xoa3', s_e_Xoa3_1_bj, s_e_Xoa3_2_sj,),
    grf.VariantGroup('Xoa4', s_e_Xoa4_1_sj, s_e_Xoa4_2_sj, s_e_Cox4_1_sj, s_e_Cox4_2_sj,),
    grf.VariantGroup('X1', s_e_X1_1_sj, s_e_X1_2_sl, s_e_X1_3_sl,),
    # emu 25
    #er_ir4,
    # emu dc
    n_o_Wes_1_hkb,
    grf.VariantGroup('OS T', n_o_T_1_os, n_o_T_2_os,),
    #stog_1_2,
    #stog_1_4,
    # emu 3rd
    s_e_C1_1_ss,
    # carriages
    #grf.VariantGroup(
    #    'ABs',
        #abs1,
        #abs2,
    #),
    grf.VariantGroup('CR', d_p_cr_1_dsb, d_p_ca_1_dsb, d_p_car_1_dsb, d_p_cae_1_dsb),
    grf.VariantGroup('Danish 30s stock 1st class', d_p_ac_i_1_dsb, d_p_ac_ii_1_dsb, d_p_ag_1_dsb, d_p_ag_2_dsb),
    grf.VariantGroup('Danish 30s stock 1st & 2nd class', d_p_au_1_dsb, d_p_aul_1_dsb, d_p_av_1_dsb, d_p_abv_1_dsb, d_p_abg_1_dsb, d_p_bv_1_dsb),
    grf.VariantGroup('Danish 30s stock 2nd class', d_p_cc_1_dsb, d_p_bg_1_dsb, d_p_bg_2_dsb, d_p_b_1_lj, d_p_b_2_lj),
    grf.VariantGroup('UIC-Y 1st class', d_p_a_1_dsb, d_p_a_2_dsb, d_p_a_3_dsb, fr_p_a_1_sncf, fr_p_a_2_sncf, fr_p_a_3_sncf),
    grf.VariantGroup('UIC-Y 1st & 2nd class', d_p_ab_1_dsb, d_p_ab_2_dsb, d_p_ab_3_dsb, fr_p_ab_1_sncf, fr_p_ab_2_sncf, fr_p_ab_3_sncf),
    grf.VariantGroup('UIC-Y 2nd class', d_p_b_1_dsb, d_p_b_i_1_dsb, fr_p_b_1_sncf, fr_p_b_2_sncf, fr_p_b_3_sncf),
    grf.VariantGroup('UIC-Y dining & kiosk', d_p_bk_i_1_dsb, d_p_bk_i_2_dsb),
    grf.VariantGroup('UIC-Y luggage', d_p_bd_1_dsb, d_p_bd_2_dsb, fr_p_ad_1_sncf, fr_p_ad_2_sncf, fr_p_ad_3_sncf, fr_p_bd_1_sncf, fr_p_bd_2_sncf),
    grf.VariantGroup('An', d_p_an_1_dsb, d_p_an_2_dsb, d_p_an_3_dsb),
    grf.VariantGroup('Bn', d_p_bn_1_dsb, d_p_bn_2_dsb, d_p_bn_5_dsb, d_p_bn_6_dsb, d_p_bn_4_dsb, d_p_bn_3_dsb),
    grf.VariantGroup('B II', d_p_b_ii_1_dsb, d_p_bk_iii_1_dsb, d_p_b_ii_2_dsb, d_p_bk_iii_2_dsb),
    #grf.VariantGroup(
    #    'B II',
    #    b_ii1,
    #    b_ii2,
    #),
    # wagons
    s_w_Hbis_sj,
    s_w_Gblssy_2_gc,
    # narrow gauge
    grf.VariantGroup('Z4p', s_d_Z4p_1_srj, s_d_Z4p_2, s_d_Z4p_3_nklj, s_d_Z4p_4, s_d_Z4p_5_donj, s_d_Z4p_6_sl, s_d_Z4p_7_sl,),
    s_d_Tp_1_sj,
    grf.VariantGroup('X10p', s_e_X10p_1_sl, s_e_X10p_2_sl),
    s_p_Co_1,
    s_p_UBp_ii_1,
).set_variant_callbacks(g)))

grf.main(g, 'KST_Kitchen_Sink_Trains.grf')
