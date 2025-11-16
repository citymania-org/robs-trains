import os
from datetime import date

import grf

import lib

from common import g, Livery, Train, modern_diesel_sound, standard_gauge, standard_gauge_15kv, standard_gauge_25kv, standard_gauge_1500v, standard_gauge_25kv_15kv, metro, extra_narrow_gauge, make_psd_cc_liveries, colours


PURCHASE_ICONS_DIR = 'purchase list'
DEBUG_DIR = 'debug'

os.makedirs(DEBUG_DIR, exist_ok=True)

# steam

s_s_N_ii_1_sj = Train(
    id='s_s_N_ii_1_sj',
    name='љњSJ N II',
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
    power=500, # come up with value
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
    name='љњSJ Sa',
    length=6,
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
    power=750, # come up with value
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
        'Use': 'Universal',
        'Builder': 'Multiple',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

# diesel

from code.standard_gauge.mxe import d_d_mx_i_1_dsb
from code.standard_gauge.mbrød import dk_d_mbrød_467_1, dk_d_mbrød_467_2, dk_d_mbrød_467_3, dk_d_mbrød_468_1, dk_d_mbrød_469_1, dk_d_mbrød_469_2, dk_d_mbrød_471_1, dk_d_mbrød_471_2, dk_d_mbrød_471_3, dk_d_mbrød_472_2, dk_d_mbrød_472_3, dk_d_mbrød_472_4, dk_d_mbrød_473_1, dk_d_mbrød_473_2, dk_d_mbrød_474_1, dk_d_mbrød_474_2, dk_d_mbrød_474_3, dk_d_mbrød_475_1, dk_d_mbrød_475_2, dk_d_mbrød_475_3, dk_d_mbrød_475_4
from code.standard_gauge.sbm6 import d_d_sbm6_1_dsb, d_d_sbm6_2_dsb
from code.standard_gauge.be201 import be_d_201_1_nmbs, be_d_201_2_nmbs, be_d_201_3_nmbs, be_d_201_4_nmbs, be_d_201_5_nmbs
from code.standard_gauge.be202 import be_d_202_1_nmbs, be_d_202_2_nmbs, be_d_202_3_nmbs, be_d_202_4_nmbs, be_d_202_5_nmbs, be_d_202_6_nmbs, be_d_202_7_nmbs, be_d_202_8_nmbs
from code.standard_gauge.m61 import hu_d_m61_1_mav, hu_d_m61_2_mav, hu_d_m61_3_mav
from code.standard_gauge.my import d_d_mye_ii_1_dsb, d_d_my_ii_1_dsb, d_d_my_ii_2_dsb, d_d_my_ii_8_taagab, d_d_my_ii_7_dsb, d_d_my_ii_9_taagab, d_d_my_ii_15_bk, d_d_my_ii_16_lj, d_d_my_ii_12_njj, d_d_my_ii_11_dsb, d_d_my_ii_10_dsb, d_d_my_ii_5_contec, d_d_my_ii_3_ttt, d_d_my_ii_13_cflcd, d_d_my_ii_6_mjbad, d_d_my_ii_4_lt, d_d_my_ii_14_vik, d_d_my_ii_17_bsbs, d_d_my_ii_18_et, d_d_my_ii_19_er, d_d_my_ii_20_strabag, d_d_my_ii_21_mav, d_d_my_ii_22_et, d_d_my_ii_23_strabag, d_d_my_ii_24_bsx, d_d_my_ii_25_strabag, lu_d_1600_1_cfl
from code.standard_gauge.mx import d_d_mx_ii_1_dsb, d_d_mx_ii_2_dsb, d_d_mx_ii_8_ohj, d_d_mx_ii_13_lj, d_d_mx_ii_3_vltj, d_d_mx_ii_9_sb, d_d_mx_ii_12_bk, d_d_mx_ii_10_cflcd, d_d_mx_ii_7_contec, d_d_mx_ii_5_lb, d_d_mx_ii_4_ttt, d_d_mx_ii_6_lt, d_d_mx_ii_11_vik, d_d_mx_ii_14_bsx, d_d_mx_ii_15_bsx, d_d_mx_ii_16_bsm, d_d_mx_ii_17_stab
from code.standard_gauge.mz import d_d_mz_i_1_dsb, d_d_mz_i_2_dsb, d_d_mz_i_3_dsb, d_d_mz_i_4_ttt, d_d_mz_ii_4_taagab, d_d_mz_ii_5_ibab, d_d_mz_iii_1_dsb, d_d_mz_iii_2_dsb, d_d_mz_iv_1_dsb, d_d_mz_iv_2_dbcsc, d_d_mz_ii_6_stab
from code.standard_gauge.me import d_d_me_ii_1_dsb, d_d_me_ii_2_dsb, d_d_me_ii_3_dsb, d_d_me_ii_4_dsb, d_d_me_ii_5_nrfab, d_d_me_ii_6_mav, d_d_me_ii_7_skpl

# electric 15

from code.standard_gauge.dre9394 import de_e_dre93_1_dr, de_e_dre94_1_dr
from code.standard_gauge.ra import s_e_ra_1_sj, s_e_ra_2_sj, s_e_ra_3_sj, s_e_ra_4_sj, s_e_ra_5_sj
from code.standard_gauge.rc import s_e_rc36_1_sj, s_e_rc36_2_sj, s_e_rc36_3_sj, s_e_rc36_4_sj, s_e_rc36_5_sj, s_e_rc36_6_sj, s_e_rc7_1_sj, s_e_rm_1_sj, s_e_rm_2_sj, s_e_rm_3_sj, s_e_rm_4_sj, s_e_rc36_7_sj, s_e_rc1245_1_sj, s_e_rc1245_2_sj, s_e_rc1245_3_sj, s_e_rc1245_4_sj, s_e_rc1245_5_sj, s_e_rc1245_6_sj, s_e_rc1245_7_sj, s_e_rc36_8_sj, s_e_rc1245_8_sj, s_e_rc1245_9_sj, s_e_rc1245_10_sj
from code.standard_gauge.db103 import de_e_db103_1_db, de_e_db103_2_db, de_e_db103_3_db, de_e_db103_4_radve
from code.standard_gauge.tgvpse import fr_e_pse_1_sncf, fr_e_pse_2_sncf, fr_e_pse_3_sncf
from code.standard_gauge.tgvm import fr_e_m_1_sncf, fr_e_m_2_sncf, fr_e_m_3_sncf

# electric 25

from code.standard_gauge.ea import d_e_ea_1_dsb, d_e_ea_2_dsb, d_e_ea_4_bulmarket, d_e_ea_5_db, d_e_ea_3_dsb
from code.standard_gauge.eg import d_e_eg_1_dsb, d_e_eg_2_dsb, d_e_eg_3_dsb
from code.standard_gauge.eb import d_e_eb_1_dsb, d_e_eb_2_dsb

# electric dc

# electric 3rd

# dmu

from code.standard_gauge.mq import d_d_ml_1_dsb, d_d_ml_2_dsb, d_d_mq_1_dsb, d_d_mp_1_dsb, d_d_mo_ii_1_dsb, d_d_mo_iv_1_dsb, d_d_mo_v_1_dsb
from code.standard_gauge.ms import d_d_ms_1_dsb, d_d_mb_1_dsb
from code.standard_gauge.mki import d_d_mki_1_dsb
from code.standard_gauge.Yd import s_d_Yd_1_sj, s_d_Yd_2_hnj, s_d_Yd_3_msj
from code.standard_gauge.Yo import s_d_Yo_1_sj, s_d_Yo_2_hnj
from code.standard_gauge.Yo1s import s_d_Yo1s_1_sj, s_d_Yo1s_2_bj, s_d_Yo1s_3_tgoj
from code.standard_gauge.ma import d_d_ma_1_dsb, d_d_ma_2_dsb, d_d_ma_3_dsb, d_d_ma_4_dsb, d_d_ma_5_dsb, d_d_ma_6_dsb, d_d_ma_7_dsb, d_d_ma_8_dsb, d_d_ma_9_dsb, d_d_ma_10_dsb, d_d_ma_11_dsb, d_d_ma_12_dsb
from code.standard_gauge.ytog import d_d_y1_1_dsb, d_d_y2_1_dsb, d_d_y2_2_dsb, d_d_y3_1_dsb, d_d_y4_1_dsb, d_d_y5_1_dsb, d_d_y6_1_dsb, d_d_y6_2_dsb, d_d_y6_3_dsb, d_d_y7_1_dsb, d_d_y7_2_dsb, d_d_y7_3_dsb, d_d_y8_1_dsb, d_d_y8_2_dsb, d_d_y8_3_dsb, d_d_y8_4_dsb, d_d_y9_1_dsb
from code.standard_gauge.mr import d_d_mr_1_dsb, d_d_mr_2_dsb, d_d_mr_3_dsb, d_d_mr_4_dsb, d_d_mr_5_dsb, d_d_mr_6_dsb, d_d_mr_7_dsb, d_d_mr_8_dsb, d_d_mr_9_dsb, dl_d_mr_1_dlj
from code.standard_gauge.ic3 import d_d_mf_1_dsb, d_d_mf_2_dsb, d_d_mf_3_dsb, d_d_mf_4_dsb, s_d_mf_5_sj, s_d_mf_6_sj
from code.standard_gauge.ic2 import d_d_ic2_1_dsb
from code.standard_gauge.mq2 import d_d_mq2_1_dsb, d_d_mq2_2_dsb, d_d_mq2_3_dsb, d_d_mq2_4_dsb, d_d_mq2_5_dsb, d_d_mq2_6_dsb, d_d_mq2_7_dsb, d_d_mq2_8_dsb, d_d_mq2_9_dsb, d_d_mq2_10_dsb, d_d_mq2_11_dsb
from code.standard_gauge.mp import d_d_mp2_1_dsb, d_d_mp2_2_dsb, d_d_mg_1_dsb, d_d_mg_2_dsb

# emu 15

from code.standard_gauge.type64 import n_e_type64_1_nsb
from code.standard_gauge.Xoa3 import s_e_Xoa3_1_bj, s_e_Xoa3_2_sj
from code.standard_gauge.Xoa4 import s_e_Xoa4_1_sj, s_e_Xoa4_2_sj, s_e_Cox4_1_sj, s_e_Cox4_2_sj
from code.standard_gauge.X1 import s_e_X1a_1_sj, s_e_X1a_2_sj, s_e_X1a_3_sj
from code.standard_gauge.x10111214 import s_e_x10_1_sj, s_e_x10_2_sj, s_e_x10_3_sj, s_e_x10_4_sj, s_e_x10_5_sj, s_e_x10_6_sj, s_e_x10_7_sj, s_e_x11_1_sj, s_e_x11_2_sj, s_e_x11_3_sj, s_e_x11_4_sj, s_e_x11_5_sj, s_e_x12_1_sj, s_e_x12_2_sj, s_e_x12_3_sj, s_e_x14_1_sj, s_e_x14_2_sj, s_e_x14_3_sj, s_e_x14_4_sj, s_e_x14_5_sj, s_e_x14_6_sj
from code.standard_gauge.x606162 import s_e_x60_1_sj, s_e_x61_1_sj, s_e_x61_2_sj, s_e_x61_3_sj, s_e_x61_4_sj, s_e_x62_1_sj
from code.standard_gauge.type69 import n_o_BM69A_1_nsb, n_o_BM69A_2_nsb, n_o_BM69A_3_nsb

# emu 25

from code.standard_gauge.ir4 import d_e_er_1_dsb, d_e_er_2_dsb, d_e_er_3_dsb, d_e_er_4_dsb
from code.standard_gauge.øt import d_e_et_1_dsb, d_e_et_2_dsb

# emu dc

from code.standard_gauge.HKB_Wes_1 import n_o_Wes_1_hkb
from code.standard_gauge.stog1 import d_e_stog1_1_dsb, d_e_stog1_2_dsb, d_e_stog1_3_dsb, d_e_stog1_4_dsb, d_e_stog1_5_dsb
from code.standard_gauge.OS_T import n_o_T_1_os, n_o_T_2_os
from code.standard_gauge.stog2 import d_e_stog2_1_dsb, d_e_stog2_2_dsb, d_e_stog2_9_dsb, d_e_stog2_3_dsb, d_e_stog2_4_dsb, d_e_stog2_5_dsb, d_e_stog2_6_dsb, d_e_stog2_7_dsb, d_e_stog2_8_dsb, d_e_stog2_10_dsb, d_e_stog2_11_dsb, d_e_stog2_12_dsb
from code.standard_gauge.stog3 import d_e_stog3_1_dsb, d_e_stog3_2_dsb, d_e_stog3_3_dsb, d_e_stog3_4_dsb
from code.standard_gauge.stog4 import d_e_stog4_1_dsb, d_e_stog4_2_dsb, d_e_stog4_3_dsb, d_e_stog4_4_dsb, d_e_stog4_5_dsb

# emu 3rd

from code.standard_gauge.Cx import s_e_C2_1_ss, s_e_C3_1_ss, s_e_C4_1_ss, s_e_C4_2_sl, s_e_C5_1_ss

# carriages

from code.standard_gauge.dk30stock import d_p_cr_1_dsb, d_p_ca_1_dsb, d_p_car_1_dsb, d_p_cae_1_dsb, d_p_ac_i_1_dsb, d_p_ac_ii_1_dsb, d_p_ag_1_dsb, d_p_ag_2_dsb, d_p_au_1_dsb, d_p_aul_1_dsb, d_p_av_1_dsb, d_p_abv_1_dsb, d_p_abg_1_dsb, d_p_bv_1_dsb, d_p_crl_1_dsb, d_p_cb_1_dsb, d_p_cc_1_dsb, d_p_bg_1_dsb, d_p_bg_2_dsb, d_p_b_1_lj, d_p_b_2_lj, d_p_cl_1_dsb, d_p_cl_2_dsb, d_p_cl_3_dsb, d_p_cl_4_dsb, d_p_cl_5_dsb, d_p_cl_6_dsb, d_p_cl_7_dsb, d_p_cl_8_dsb, d_p_cl_9_dsb, d_p_cl_10_dsb, d_p_cl_11_dsb, d_p_bu_1_dsb, d_p_bu_2_dsb, d_p_bu_3_dsb, d_p_bdg_1_dsb
from code.standard_gauge.albl import d_p_al_1_dsb, d_p_al_2_dsb, d_p_al_3_dsb, d_p_al_4_dsb, d_p_bl_1_dsb, d_p_bl_2_dsb, d_p_al_5_dsb, d_p_bl_3_dsb
from code.standard_gauge.uicy import d_p_a_1_dsb, d_p_a_2_dsb, d_p_a_3_dsb, d_p_ab_1_dsb, d_p_ab_2_dsb, d_p_ab_3_dsb, d_p_b_1_dsb, d_p_b_i_1_dsb, d_p_bk_i_1_dsb, d_p_bk_i_2_dsb, d_p_bd_1_dsb, d_p_bd_2_dsb, d_p_an_1_dsb, d_p_an_2_dsb, d_p_an_3_dsb, d_p_bn_1_dsb, d_p_bn_2_dsb, d_p_bn_3_dsb, d_p_bn_4_dsb, d_p_bn_5_dsb, d_p_bn_6_dsb, fr_p_a_1_sncf, fr_p_a_2_sncf, fr_p_a_3_sncf, fr_p_ab_1_sncf, fr_p_ab_2_sncf, fr_p_ab_3_sncf, fr_p_b_1_sncf, fr_p_b_2_sncf, fr_p_b_3_sncf, fr_p_ad_1_sncf, fr_p_ad_2_sncf, fr_p_ad_3_sncf, fr_p_bd_1_sncf, fr_p_bd_2_sncf, d_p_bns_1_dsb, d_p_bns_2_dsb, d_p_bns_3_dsb, d_p_bns_4_dsb, d_p_bns_5_dsb, d_p_bns_1_dsb_test, d_p_bns_2_dsb_test, d_p_bns_3_dsb_test, d_p_bns_4_dsb_test, d_p_bns_5_dsb_test, d_p_bns_6_dsb, d_p_bns_6_dsb_test, d_p_bd_3_dsb
from code.standard_gauge.ic5 import d_p_ic5_1_dsb, d_p_ic5_2_dsb, d_p_ic5_3_dsb, d_p_ic5_4_dsb
from code.standard_gauge.bii import d_p_b_ii_1_dsb, d_p_b_ii_2_dsb, d_p_b_ii_3_dsb, d_p_bk_iii_1_dsb, d_p_bk_iii_2_dsb, d_p_bk_iii_3_dsb, d_p_abs_1_dsb, d_p_abs_2_dsb, d_p_abs_3_dsb, d_p_abs_1_dsb_test, d_p_abs_2_dsb_test, d_p_abs_3_dsb_test

# wagons

s_w_Gblssy_2_gc = Train(
    id='s_w_Gblssy_2_gc',
    name='љњGC Gblss-y',
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
    name='љњSJ Hbis',
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

from code.narrow_gauge.Z4p import s_d_Z4p_1_srj, s_d_Z4p_2, s_d_Z4p_3_nklj, s_d_Z4p_4, s_d_Z4p_5_donj, s_d_Z4p_6_sl, s_d_Z4p_7_sl
from code.narrow_gauge.other import s_d_Tp_1_sj, s_p_Co_1
from code.narrow_gauge.MÖJ_2to5 import s_e_MÖJ_2to5_1_möj, s_e_MÖJ_2to5_2_möj
from code.narrow_gauge.NKlJ import s_e_NKlJ_AEG_1_nklj, s_e_NKlJ_AEG_2_nklj
from code.narrow_gauge.Xo6p import s_d_Xo6p_1_srj
from code.narrow_gauge.X10p import s_p_UBp_ii_1, s_e_X10p_1_sl, s_e_X10p_2_sl

'''

x15p = Train(
    id='x15p',
    name='љњX15p',
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

# end

purchase_icon = lambda fname: grf.FileSprite(grf.ImageFile(os.path.join(PURCHASE_ICONS_DIR, fname)), 0, 0, None, None)


COUNTRY_SPRITES = {
    'austria': purchase_icon('fat.png'),
    'belgium': purchase_icon('fbe.png'),
    'bulgaria': purchase_icon('fbg.png'),
    'switzerland': purchase_icon('fch.png'),
    'czechrepublic': purchase_icon('fcz.png'),
    'germany': purchase_icon('fde.png'),
    'denmark': purchase_icon('fdk.png'),
    'doggerland': purchase_icon('fdl.png'),
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
    'multi': purchase_icon('pelectricdv.png'), # replece these sprites
    'dc': purchase_icon('pelectricdc1500.png'),
    'dc3000': purchase_icon('pelectricdc3000.png'),
    '15kv': purchase_icon('pelectric15.png'),
    '15kv/25kv': purchase_icon('pelectric1525.png'),
    '25kv': purchase_icon('pelectric25.png'),
    'dc/15kv/25kv': purchase_icon('pelectric15001525.png'),
    'dc/dc3000/15kv/25kv': purchase_icon('pelectric150030001525.png'),
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
(g.add(lib.SetPurchaseOrder(
    # start
    # be
    # be diesel
    grf.VariantGroup('HLD 201', be_d_201_1_nmbs, be_d_201_5_nmbs, be_d_201_2_nmbs, be_d_201_3_nmbs, be_d_201_4_nmbs),
    grf.VariantGroup('HLD 202/203', be_d_202_1_nmbs, be_d_202_2_nmbs, be_d_202_3_nmbs, be_d_202_4_nmbs),
    grf.VariantGroup('HLD 204', be_d_202_5_nmbs, be_d_202_6_nmbs, be_d_202_7_nmbs, be_d_202_8_nmbs),
    # bg
    # bg electric 25
    grf.VariantGroup('EA', d_e_ea_4_bulmarket, d_e_ea_5_db),
    # de
    # de diesel
    grf.VariantGroup('V 170', d_d_my_ii_18_et, d_d_my_ii_22_et, d_d_my_ii_19_er, d_d_my_ii_20_strabag, d_d_my_ii_23_strabag, d_d_my_ii_25_strabag, d_d_my_ii_17_bsbs),
    # de electric 15
    de_e_dre93_1_dr,
    de_e_dre94_1_dr,
    grf.VariantGroup('њ103', de_e_db103_1_db, de_e_db103_2_db, de_e_db103_3_db, de_e_db103_4_radve),
    # dk
    # dk steam
    # dk diesel
    d_d_mx_i_1_dsb,
    grf.VariantGroup('љњFrichs 467-475 "Marcipanbrød"', dk_d_mbrød_467_1, dk_d_mbrød_467_2, dk_d_mbrød_467_3, dk_d_mbrød_468_1, dk_d_mbrød_469_1, dk_d_mbrød_469_2, dk_d_mbrød_471_1, dk_d_mbrød_471_2, dk_d_mbrød_471_3, dk_d_mbrød_472_2, dk_d_mbrød_472_3, dk_d_mbrød_472_4, dk_d_mbrød_473_1, dk_d_mbrød_473_2, dk_d_mbrød_474_1, dk_d_mbrød_474_2, dk_d_mbrød_474_3, dk_d_mbrød_475_1, dk_d_mbrød_475_2, dk_d_mbrød_475_3, dk_d_mbrød_475_4),
    grf.VariantGroup('SB M 6', d_d_sbm6_1_dsb, d_d_sbm6_2_dsb),
    d_d_mye_ii_1_dsb,
    grf.VariantGroup('MX II', d_d_mx_ii_1_dsb, d_d_mx_ii_2_dsb, d_d_mx_ii_8_ohj, d_d_mx_ii_13_lj, d_d_mx_ii_3_vltj, d_d_mx_ii_9_sb, d_d_mx_ii_10_cflcd, d_d_mx_ii_7_contec, d_d_mx_ii_5_lb, d_d_mx_ii_6_lt, d_d_mx_ii_11_vik),
    grf.VariantGroup('MY II', d_d_my_ii_1_dsb, d_d_my_ii_2_dsb, d_d_my_ii_7_dsb, d_d_my_ii_16_lj, d_d_my_ii_12_njj, d_d_my_ii_11_dsb, d_d_my_ii_10_dsb, d_d_my_ii_5_contec, d_d_my_ii_13_cflcd, d_d_my_ii_6_mjbad, d_d_my_ii_4_lt, d_d_my_ii_14_vik),
    grf.VariantGroup('MZ I/II', d_d_mz_i_1_dsb, d_d_mz_i_2_dsb, d_d_mz_i_3_dsb, d_d_mz_ii_6_stab),
    grf.VariantGroup('MZ III', d_d_mz_iii_1_dsb, d_d_mz_iii_2_dsb),
    grf.VariantGroup('MZ IV', d_d_mz_iv_1_dsb, d_d_mz_iv_2_dbcsc),
    grf.VariantGroup('ME II', d_d_me_ii_1_dsb, d_d_me_ii_2_dsb, d_d_me_ii_3_dsb, d_d_me_ii_4_dsb),
    # dk electric dc
    # dk electric dc 3000
    # dk electric 15
    # dk electric 25
    grf.VariantGroup('EA', d_e_ea_1_dsb, d_e_ea_2_dsb, d_e_ea_3_dsb),
    grf.VariantGroup('њ"EuroSprinter"', d_e_eg_1_dsb, d_e_eg_2_dsb, d_e_eg_3_dsb),
    grf.VariantGroup('њ"Vectron"', d_e_eb_1_dsb, d_e_eb_2_dsb),
    # dk electric 3rd
    # dk dmu
    grf.VariantGroup('ML', d_d_ml_1_dsb, d_d_ml_2_dsb),
    d_d_mq_1_dsb,
    d_d_mp_1_dsb,
    grf.VariantGroup('MO', d_d_mo_ii_1_dsb, d_d_mo_iv_1_dsb, d_d_mo_v_1_dsb),
    d_d_ms_1_dsb,
    d_d_mb_1_dsb,
    d_d_mki_1_dsb,
    grf.VariantGroup('њMA (Part 1)', d_d_ma_1_dsb, d_d_ma_2_dsb, d_d_ma_3_dsb),
    grf.VariantGroup('њMA (Part 2)', d_d_ma_4_dsb, d_d_ma_5_dsb, d_d_ma_6_dsb),
    grf.VariantGroup('њMA (Part 1 reversed)', d_d_ma_7_dsb, d_d_ma_8_dsb, d_d_ma_9_dsb),
    grf.VariantGroup('њMA (Part 2 reversed)', d_d_ma_10_dsb, d_d_ma_11_dsb, d_d_ma_12_dsb),
    grf.VariantGroup('Y-Tog "Lynette" "Grisen"', d_d_y1_1_dsb, d_d_y2_1_dsb, d_d_y2_2_dsb, d_d_y3_1_dsb, d_d_y4_1_dsb, d_d_y5_1_dsb, d_d_y6_1_dsb, d_d_y6_2_dsb, d_d_y6_3_dsb, d_d_y7_1_dsb, d_d_y7_2_dsb, d_d_y7_3_dsb, d_d_y8_1_dsb, d_d_y8_2_dsb, d_d_y8_3_dsb, d_d_y8_4_dsb, d_d_y9_1_dsb),
    grf.VariantGroup('MR', d_d_mr_1_dsb, d_d_mr_7_dsb, d_d_mr_2_dsb, d_d_mr_4_dsb, d_d_mr_3_dsb, d_d_mr_5_dsb, d_d_mr_6_dsb, d_d_mr_8_dsb, d_d_mr_9_dsb),
    grf.VariantGroup('њMF (IC3)', d_d_mf_1_dsb, d_d_mf_2_dsb, d_d_mf_3_dsb, d_d_mf_4_dsb),
    d_d_ic2_1_dsb,
    grf.VariantGroup('њ"Desiro Classic"', d_d_mq2_6_dsb, d_d_mq2_1_dsb, d_d_mq2_7_dsb, d_d_mq2_2_dsb, d_d_mq2_8_dsb, d_d_mq2_10_dsb, d_d_mq2_3_dsb, d_d_mq2_4_dsb, d_d_mq2_11_dsb, d_d_mq2_9_dsb, d_d_mq2_5_dsb),
    grf.VariantGroup('њMG (IC4)', d_d_mg_1_dsb, d_d_mg_2_dsb),
    grf.VariantGroup('њMP (IC2)', d_d_mp2_1_dsb, d_d_mp2_2_dsb),
    # dk emu dc
    grf.VariantGroup('S-Tog 1 "De Brune S-Tog"', d_e_stog1_1_dsb, d_e_stog1_2_dsb, d_e_stog1_3_dsb, d_e_stog1_4_dsb, d_e_stog1_5_dsb),
    grf.VariantGroup('њS-Tog 2 "De Røde S-Tog"', d_e_stog2_1_dsb, d_e_stog2_2_dsb, d_e_stog2_9_dsb, d_e_stog2_4_dsb, d_e_stog2_3_dsb, d_e_stog2_10_dsb, d_e_stog2_11_dsb, d_e_stog2_12_dsb, d_e_stog2_5_dsb, d_e_stog2_6_dsb, d_e_stog2_7_dsb, d_e_stog2_8_dsb),
    grf.VariantGroup('њS-Tog 3', d_e_stog3_1_dsb, d_e_stog3_2_dsb, d_e_stog3_3_dsb, d_e_stog3_4_dsb),
    grf.VariantGroup('њS-Tog 4 "Hamster" & "Hamsterunge"', d_e_stog4_5_dsb, d_e_stog4_1_dsb, d_e_stog4_3_dsb, d_e_stog4_4_dsb, d_e_stog4_2_dsb),
    # dk emu dc 3000
    # dk emu 15
    # dk emu 25
    grf.VariantGroup('њER (IR4)', d_e_er_1_dsb, d_e_er_2_dsb, d_e_er_3_dsb, d_e_er_4_dsb),
    # dk emu 3rd
    # dk carriages
    grf.VariantGroup('CR', d_p_cr_1_dsb, d_p_ca_1_dsb, d_p_car_1_dsb, d_p_cae_1_dsb),
    grf.VariantGroup('30s stock 1st class', d_p_ac_i_1_dsb, d_p_ac_ii_1_dsb, d_p_ag_1_dsb, d_p_ag_2_dsb),
    grf.VariantGroup('30s stock 1st & 2nd class', d_p_au_1_dsb, d_p_aul_1_dsb, d_p_av_1_dsb, d_p_abv_1_dsb, d_p_abg_1_dsb, d_p_bv_1_dsb),
    grf.VariantGroup('30s stock 2nd class', d_p_crl_1_dsb, d_p_cb_1_dsb, d_p_cc_1_dsb, d_p_bg_1_dsb, d_p_bg_2_dsb, d_p_b_1_lj, d_p_b_2_lj),
    grf.VariantGroup('њCL/CLE/CLS', d_p_cl_1_dsb, d_p_cl_9_dsb, d_p_cl_10_dsb, d_p_cl_11_dsb, d_p_cl_8_dsb, d_p_cl_7_dsb, d_p_cl_2_dsb, d_p_cl_3_dsb),
    grf.VariantGroup('AL/BL', d_p_al_1_dsb, d_p_al_2_dsb, d_p_al_3_dsb, d_p_al_4_dsb, d_p_bl_1_dsb, d_p_bl_2_dsb, d_p_bl_3_dsb),
    grf.VariantGroup('Excursion & dance carriages', d_p_bu_1_dsb, d_p_bu_2_dsb, d_p_bu_3_dsb),
    grf.VariantGroup('UIC-Y 1st class', d_p_a_1_dsb, d_p_a_2_dsb, d_p_a_3_dsb),
    grf.VariantGroup('UIC-Y 1st & 2nd class', d_p_ab_1_dsb, d_p_ab_2_dsb, d_p_ab_3_dsb),
    grf.VariantGroup('UIC-Y 2nd class', d_p_b_1_dsb, d_p_b_i_1_dsb),
    grf.VariantGroup('UIC-Y other', d_p_bd_1_dsb, d_p_bd_2_dsb, d_p_bk_i_1_dsb, d_p_bk_i_2_dsb, d_p_bd_3_dsb),
    d_p_cl_5_dsb,
    grf.VariantGroup('An', d_p_an_1_dsb, d_p_an_2_dsb, d_p_an_3_dsb),
    grf.VariantGroup('Bn', d_p_bn_1_dsb, d_p_bn_2_dsb, d_p_bn_5_dsb, d_p_bn_6_dsb, d_p_bn_4_dsb, d_p_bn_3_dsb),
    grf.VariantGroup('њBns', d_p_bns_1_dsb, d_p_bns_2_dsb, d_p_bns_3_dsb, d_p_bns_6_dsb, d_p_bns_4_dsb, d_p_bns_5_dsb,),
    d_p_bdg_1_dsb,
    grf.VariantGroup('њIC5/APO Lyntog Prototype', d_p_ic5_1_dsb, d_p_ic5_2_dsb,),
    grf.VariantGroup('B II', d_p_b_ii_1_dsb, d_p_b_ii_2_dsb, d_p_b_ii_3_dsb),
    grf.VariantGroup('Bk III', d_p_bk_iii_1_dsb, d_p_bk_iii_2_dsb, d_p_bk_iii_3_dsb),
    grf.VariantGroup('њABs', d_p_abs_1_dsb, d_p_abs_2_dsb, d_p_abs_3_dsb),
    # dk wagons
    # dl
    # dl dmu
    dl_d_mr_1_dlj,
    # fr
    # fr emu dc
    grf.VariantGroup('њTGV PSE', fr_e_pse_1_sncf, fr_e_pse_2_sncf, fr_e_pse_3_sncf),
    grf.VariantGroup('њTGV M', fr_e_m_1_sncf, fr_e_m_2_sncf, fr_e_m_3_sncf),
    # fr carriages
    grf.VariantGroup('UIC-Y 1st class', fr_p_a_1_sncf, fr_p_a_2_sncf, fr_p_a_3_sncf),
    grf.VariantGroup('UIC-Y 1st & 2nd class', fr_p_ab_1_sncf, fr_p_ab_2_sncf, fr_p_ab_3_sncf),
    grf.VariantGroup('UIC-Y 2nd class', fr_p_b_1_sncf, fr_p_b_2_sncf, fr_p_b_3_sncf),
    grf.VariantGroup('UIC-Y other', fr_p_ad_1_sncf, fr_p_ad_2_sncf, fr_p_ad_3_sncf, fr_p_bd_1_sncf, fr_p_bd_2_sncf),
    # hu
    # hu diesel
    grf.VariantGroup('M61', hu_d_m61_1_mav, hu_d_m61_2_mav, hu_d_m61_3_mav),
    d_d_my_ii_21_mav,
    d_d_me_ii_6_mav,
    # lu
    # lu diesel
    lu_d_1600_1_cfl,
    # no
    # no emu dc
    n_o_Wes_1_hkb,
    grf.VariantGroup('њOS T', n_o_T_1_os, n_o_T_2_os,),
    # no emu 15
    n_e_type64_1_nsb,
    grf.VariantGroup('Type 69A', n_o_BM69A_1_nsb, n_o_BM69A_2_nsb, n_o_BM69A_3_nsb,),
    # no carriages
    d_p_al_5_dsb,
    # pl
    # pl diesel
    d_d_me_ii_7_skpl,
    # se
    # se steam
    s_s_N_ii_1_sj,
    s_s_Sa_sj,
    # se diesel
    grf.VariantGroup('TMX II', d_d_mx_ii_14_bsx, d_d_mx_ii_15_bsx, d_d_mx_ii_16_bsm, d_d_mx_ii_12_bk, d_d_mx_ii_4_ttt, d_d_mx_ii_17_stab),
    grf.VariantGroup('TMY II', d_d_my_ii_8_taagab, d_d_my_ii_24_bsx, d_d_my_ii_9_taagab, d_d_my_ii_15_bk, d_d_my_ii_3_ttt),
    grf.VariantGroup('TMZ I/II', d_d_mz_i_4_ttt, d_d_mz_ii_4_taagab, d_d_mz_ii_5_ibab),
    d_d_me_ii_5_nrfab,
    # se electric 15
    grf.VariantGroup('њRa', s_e_ra_1_sj, s_e_ra_2_sj, s_e_ra_3_sj, s_e_ra_4_sj, s_e_ra_5_sj),
    grf.VariantGroup('њRc1/2/4/5', s_e_rc1245_1_sj, s_e_rc1245_6_sj, s_e_rc1245_7_sj, s_e_rc1245_2_sj, s_e_rc1245_3_sj, s_e_rc1245_4_sj, s_e_rc1245_5_sj, s_e_rc1245_8_sj, s_e_rc1245_10_sj, s_e_rc1245_9_sj),
    grf.VariantGroup('њRc3/6', s_e_rc36_1_sj, s_e_rc36_8_sj, s_e_rc36_2_sj, s_e_rc36_3_sj, s_e_rc36_4_sj, s_e_rc36_5_sj, s_e_rc36_6_sj, s_e_rc36_7_sj),
    grf.VariantGroup('њRm', s_e_rm_1_sj, s_e_rm_2_sj, s_e_rm_3_sj, s_e_rm_4_sj),
    s_e_rc7_1_sj,
    # se dmu
    grf.VariantGroup('њYd', s_d_Yd_1_sj, s_d_Yd_2_hnj, s_d_Yd_3_msj),
    grf.VariantGroup('њYo', s_d_Yo_1_sj, s_d_Yo_2_hnj),
    grf.VariantGroup('њYo1s', s_d_Yo1s_1_sj, s_d_Yo1s_2_bj, s_d_Yo1s_3_tgoj),
    grf.VariantGroup('њY2', s_d_mf_5_sj, s_d_mf_6_sj),
    # se emu 15
    grf.VariantGroup('њXoa3', s_e_Xoa3_1_bj, s_e_Xoa3_2_sj),
    grf.VariantGroup('њXoa4', s_e_Xoa4_1_sj, s_e_Xoa4_2_sj, s_e_Cox4_1_sj, s_e_Cox4_2_sj),
    grf.VariantGroup('X1', s_e_X1a_1_sj, s_e_X1a_2_sj, s_e_X1a_3_sj),
    grf.VariantGroup('њX10', s_e_x10_1_sj, s_e_x10_2_sj, s_e_x10_3_sj, s_e_x10_4_sj, s_e_x10_5_sj, s_e_x10_6_sj, s_e_x10_7_sj),
    grf.VariantGroup('њX11', s_e_x11_1_sj, s_e_x11_2_sj, s_e_x11_3_sj, s_e_x11_4_sj, s_e_x11_5_sj),
    grf.VariantGroup('њX12', s_e_x12_1_sj, s_e_x12_2_sj, s_e_x12_3_sj),
    grf.VariantGroup('њX14', s_e_x14_1_sj, s_e_x14_2_sj, s_e_x14_3_sj, s_e_x14_4_sj, s_e_x14_5_sj, s_e_x14_6_sj),
    grf.VariantGroup('њX31K/ET/X32K (Øresundståg)', d_e_et_1_dsb, d_e_et_2_dsb),
    s_e_x60_1_sj,
    grf.VariantGroup('њX61', s_e_x61_1_sj, s_e_x61_2_sj, s_e_x61_3_sj, s_e_x61_4_sj),
    s_e_x62_1_sj,
    # se emu 3rd
    grf.VariantGroup('Cx', s_e_C2_1_ss, s_e_C3_1_ss, s_e_C4_1_ss, s_e_C4_2_sl, s_e_C5_1_ss),
    # se wagons
    s_w_Hbis_sj,
    s_w_Gblssy_2_gc,
    # narrow gauge
    grf.VariantGroup('њZ4p', s_d_Z4p_1_srj, s_d_Z4p_2, s_d_Z4p_3_nklj, s_d_Z4p_4, s_d_Z4p_5_donj, s_d_Z4p_6_sl, s_d_Z4p_7_sl,),
    s_d_Tp_1_sj,
    grf.VariantGroup('MÖJ 2-5', s_e_MÖJ_2to5_1_möj, s_e_MÖJ_2to5_2_möj),
    grf.VariantGroup('NKlJ AEG', s_e_NKlJ_AEG_1_nklj, s_e_NKlJ_AEG_2_nklj),
    s_d_Xo6p_1_srj,
    grf.VariantGroup('њX10p', s_e_X10p_1_sl, s_e_X10p_2_sl),
    s_p_Co_1,
    s_p_UBp_ii_1,
    # junk
    grf.VariantGroup('њTEST VEHICLES', d_p_cl_4_dsb, d_p_cl_6_dsb, d_p_bns_1_dsb_test, d_p_ic5_3_dsb, d_p_ic5_4_dsb, d_p_bns_2_dsb_test, d_p_bns_3_dsb_test, d_p_bns_6_dsb_test, d_p_abs_1_dsb_test, d_p_bns_4_dsb_test, d_p_bns_5_dsb_test, d_p_abs_2_dsb_test, d_p_abs_3_dsb_test,),
    
).set_variant_callbacks(g)))

grf.main(g, 'KST_Kitchen_Sink_Trains.grf')
