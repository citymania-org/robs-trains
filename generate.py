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

from code.standard_gauge.mxe import d_d_mx_i_1_dsb

from code.standard_gauge.be201 import be_d_201_1_nmbs, be_d_201_2_nmbs, be_d_201_3_nmbs, be_d_201_4_nmbs

# nohab

from code.standard_gauge.nohab import hu_d_m61_1_mav, hu_d_m61_2_mav, hu_d_m61_3_mav, hu_d_m61_4_mav

from code.standard_gauge.my import d_d_mye_ii_1_dsb, d_d_my_ii_1_dsb, d_d_my_ii_2_dsb, d_d_my_ii_8_taagab, d_d_my_ii_7_dsb, d_d_my_ii_9_taagab, d_d_my_ii_12_njj, d_d_my_ii_11_dsb, d_d_my_ii_10_dsb, d_d_my_ii_5_contec, d_d_my_ii_3_ttt, d_d_my_ii_13_cflcd, d_d_my_ii_6_mjbad, d_d_my_ii_4_lt, d_d_my_ii_14_vik
        
from code.standard_gauge.mx import d_d_mx_ii_1_dsb, d_d_mx_ii_2_dsb, d_d_mx_ii_8_ohj, d_d_mx_ii_3_vltj, d_d_mx_ii_9_sb, d_d_mx_ii_10_cflcd, d_d_mx_ii_7_contec, d_d_mx_ii_5_lb, d_d_mx_ii_4_ttt, d_d_mx_ii_6_lt, d_d_mx_ii_11_vik

# toaster

from code.standard_gauge.mz import d_d_mz_i_1_dsb, d_d_mz_i_2_dsb, d_d_mz_i_3_dsb, d_d_mz_i_4_ttt, d_d_mz_ii_4_taagab, d_d_mz_ii_5_ibab, d_d_mz_iii_1_dsb, d_d_mz_iii_2_dsb, d_d_mz_iv_1_dsb, d_d_mz_iv_2_dbcsc

from code.standard_gauge.me import d_d_me_ii_1_dsb, d_d_me_ii_2_dsb, d_d_me_ii_3_dsb, d_d_me_ii_4_dsb, d_d_me_ii_5_nrfab, d_d_me_ii_6_mav, d_d_me_ii_7_skpl

# electric 15

from code.standard_gauge.dre9394 import de_e_dre93_1_dr, de_e_dre94_1_dr

from code.standard_gauge.rc import s_e_rc36_1_sj, s_e_rc36_2_sj, s_e_rc36_3_sj, s_e_rc36_4_sj, s_e_rc36_5_sj, s_e_rc36_6_sj, s_e_rc7_1_sj, s_e_rm_1_sj, s_e_rm_2_sj, s_e_rm_3_sj, s_e_rm_4_sj, s_e_rc36_7_sj, s_e_rc1245_1_sj, s_e_rc1245_2_sj, s_e_rc1245_3_sj, s_e_rc1245_4_sj, s_e_rc1245_5_sj, s_e_rc1245_6_sj

from code.standard_gauge.db103 import de_e_db103_1_db, de_e_db103_2_db, de_e_db103_3_db, de_e_db103_4_radve

# electric 25

from code.standard_gauge.ea import d_e_ea_1_dsb, d_e_ea_2_dsb, d_e_ea_4_bulmarket, d_e_ea_5_db, d_e_ea_3_dsb

# electric dc

# electric 3rd

# dmu

from code.standard_gauge.mq import d_d_ml_1_dsb, d_d_ml_2_dsb, d_d_mq_1_dsb, d_d_mp_1_dsb, d_d_mo_ii_1_dsb, d_d_mo_iv_1_dsb, d_d_mo_v_1_dsb

from code.standard_gauge.Yd import s_d_Yd_1_sj, s_d_Yd_2_hnj, s_d_Yd_3_msj

from code.standard_gauge.Yo import s_d_Yo_1_sj, s_d_Yo_2_hnj

from code.standard_gauge.Yo1s import s_d_Yo1s_1_sj, s_d_Yo1s_2_bj, s_d_Yo1s_3_tgoj

from code.standard_gauge.mr import d_d_mr_1_dsb, d_d_mr_2_dsb, d_d_mr_3_dsb, d_d_mr_4_dsb, d_d_mr_5_dsb, d_d_mr_6_dsb

from code.standard_gauge.ic3 import d_d_mf_1_dsb, d_d_mf_2_dsb, d_d_mf_3_dsb, d_d_mf_4_dsb, s_d_mf_5_sj, s_d_mf_6_sj

# emu 15

from code.standard_gauge.Xoa4 import s_e_Xoa4_1_sj, s_e_Xoa4_2_sj, s_e_Cox4_1_sj, s_e_Cox4_2_sj

from code.standard_gauge.Xoa3 import s_e_Xoa3_1_bj, s_e_Xoa3_2_sj

from code.standard_gauge.X1 import s_e_X1_1_sj, s_e_X1_2_sl, s_e_X1_3_sl

from code.standard_gauge.type69 import n_o_BM69A_1_nsb, n_o_BM69A_2_nsb, n_o_BM69A_3_nsb

# emu 25

from code.standard_gauge.ir4 import d_e_er_1_dsb, d_e_er_2_dsb, d_e_er_3_dsb, d_e_er_4_dsb

from code.standard_gauge.øt import d_e_et_1_dsb, d_e_et_2_dsb

# emu dc

from code.standard_gauge.HKB_Wes_1 import n_o_Wes_1_hkb

from code.standard_gauge.stog1 import d_e_stog1_1_dsb, d_e_stog1_2_dsb, d_e_stog1_3_dsb, d_e_stog1_4_dsb, d_e_stog1_5_dsb

from code.standard_gauge.OS_T import n_o_T_1_os, n_o_T_2_os

from code.standard_gauge.stog2 import d_e_stog2_1_dsb, d_e_stog2_2_dsb, d_e_stog2_9_dsb, d_e_stog2_3_dsb, d_e_stog2_4_dsb, d_e_stog2_5_dsb, d_e_stog2_6_dsb, d_e_stog2_7_dsb, d_e_stog2_8_dsb

from code.standard_gauge.stog3 import d_e_stog3_1_dsb, d_e_stog3_2_dsb, d_e_stog3_3_dsb, d_e_stog3_4_dsb

from code.standard_gauge.stog4 import d_e_stog4_1_dsb, d_e_stog4_2_dsb, d_e_stog4_3_dsb, d_e_stog4_4_dsb

# emu 3rd

from code.standard_gauge.C1 import s_e_C1_1_ss

from code.standard_gauge.C4 import s_e_C4_1_ss, s_e_C4_2_sl

from code.standard_gauge.C5 import s_e_C5_1_ss

# carriages

from code.standard_gauge.dk30stock import d_p_cr_1_dsb, d_p_ca_1_dsb, d_p_car_1_dsb, d_p_cae_1_dsb, d_p_ac_i_1_dsb, d_p_ac_ii_1_dsb, d_p_ag_1_dsb, d_p_ag_2_dsb, d_p_au_1_dsb, d_p_aul_1_dsb, d_p_av_1_dsb, d_p_abv_1_dsb, d_p_abg_1_dsb, d_p_bv_1_dsb, d_p_cc_1_dsb, d_p_bg_1_dsb, d_p_bg_2_dsb, d_p_b_1_lj, d_p_b_2_lj

from code.standard_gauge.uicy import d_p_a_1_dsb, d_p_a_2_dsb, d_p_a_3_dsb, d_p_ab_1_dsb, d_p_ab_2_dsb, d_p_ab_3_dsb, d_p_b_1_dsb, d_p_b_i_1_dsb, d_p_bk_i_1_dsb, d_p_bk_i_2_dsb, d_p_bd_1_dsb, d_p_bd_2_dsb, d_p_an_1_dsb, d_p_an_2_dsb, d_p_an_3_dsb, d_p_bn_1_dsb, d_p_bn_2_dsb, d_p_bn_3_dsb, d_p_bn_4_dsb, d_p_bn_5_dsb, d_p_bn_6_dsb, fr_p_a_1_sncf, fr_p_a_2_sncf, fr_p_a_3_sncf, fr_p_ab_1_sncf, fr_p_ab_2_sncf, fr_p_ab_3_sncf, fr_p_b_1_sncf, fr_p_b_2_sncf, fr_p_b_3_sncf, fr_p_ad_1_sncf, fr_p_ad_2_sncf, fr_p_ad_3_sncf, fr_p_bd_1_sncf, fr_p_bd_2_sncf

d_p_b_ii_1_dsb = Train(
    id='d_p_b_ii_1_dsb',
    name='љњDSB B II',
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
    name='љњDSB B II',
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
    name='љњDSB Bk III',
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
    name='љњDSB Bk III',
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

from code.narrow_gauge.X10p import s_p_UBp_ii_1, s_e_X10p_1_sl, s_e_X10p_2_sl

from code.narrow_gauge.Z4p import s_d_Z4p_1_srj, s_d_Z4p_2, s_d_Z4p_3_nklj, s_d_Z4p_4, s_d_Z4p_5_donj, s_d_Z4p_6_sl, s_d_Z4p_7_sl

from code.narrow_gauge.other import s_d_Tp_1_sj, s_p_Co_1

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

# old sbb

from code.standard_gauge.sbb import ch_p_2pax_1_sbb, ch_p_2bag_1_sbb, ch_p_4pax_1_sbb, ch_p_4bag_1_sbb

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
    #grf.VariantGroup('љњFrichs 467-475 "Marcipanbrød"', d_d_frichs_467_1, d_d_frichs_467_2, d_d_frichs_467_3, d_d_frichs_467_4, d_d_frichs_467_5, d_d_frichs_468_1, d_d_frichs_468_2, d_d_frichs_468_3, d_d_frichs_469_1, d_d_frichs_469_2, d_d_frichs_469_3, d_d_frichs_469_4, d_d_frichs_469_8, d_d_frichs_469_5, d_d_frichs_469_6, d_d_frichs_469_7, d_d_frichs_471_1, d_d_frichs_471_2, d_d_frichs_471_3, d_d_frichs_471_4, d_d_frichs_471_5, d_d_frichs_471_6, d_d_frichs_472_1, d_d_frichs_472_2, d_d_frichs_472_3, d_d_frichs_472_4, d_d_frichs_472_5, d_d_frichs_473_1, d_d_frichs_473_2, d_d_frichs_473_3, d_d_frichs_474_1, d_d_frichs_474_2, d_d_frichs_474_3, d_d_frichs_474_4, d_d_frichs_474_5, d_d_frichs_475_1, d_d_frichs_475_2, d_d_frichs_475_3, d_d_frichs_475_4),
    d_d_mx_i_1_dsb,
    grf.VariantGroup('њHLD 201/HLD 59', be_d_201_1_nmbs, be_d_201_2_nmbs, be_d_201_3_nmbs, be_d_201_4_nmbs),
    d_d_mye_ii_1_dsb,
    grf.VariantGroup('MX II', d_d_mx_ii_1_dsb, d_d_mx_ii_2_dsb, d_d_mx_ii_8_ohj, d_d_mx_ii_3_vltj, d_d_mx_ii_9_sb, d_d_mx_ii_10_cflcd, d_d_mx_ii_7_contec, d_d_mx_ii_5_lb, d_d_mx_ii_4_ttt, d_d_mx_ii_6_lt, d_d_mx_ii_11_vik),
    grf.VariantGroup('M61', hu_d_m61_1_mav, hu_d_m61_2_mav, hu_d_m61_3_mav, hu_d_m61_4_mav),
    grf.VariantGroup('MY II', d_d_my_ii_1_dsb, d_d_my_ii_2_dsb, d_d_my_ii_8_taagab, d_d_my_ii_7_dsb, d_d_my_ii_9_taagab, d_d_my_ii_12_njj, d_d_my_ii_11_dsb, d_d_my_ii_10_dsb, d_d_my_ii_5_contec, d_d_my_ii_3_ttt, d_d_my_ii_13_cflcd, d_d_my_ii_6_mjbad, d_d_my_ii_4_lt, d_d_my_ii_14_vik),
    grf.VariantGroup('MZ I/II', d_d_mz_i_1_dsb, d_d_mz_i_2_dsb, d_d_mz_i_3_dsb, d_d_mz_i_4_ttt, d_d_mz_ii_4_taagab, d_d_mz_ii_5_ibab),
    grf.VariantGroup('MZ III', d_d_mz_iii_1_dsb, d_d_mz_iii_2_dsb),
    grf.VariantGroup('MZ IV', d_d_mz_iv_1_dsb, d_d_mz_iv_2_dbcsc),
    grf.VariantGroup('ME II', d_d_me_ii_1_dsb, d_d_me_ii_2_dsb, d_d_me_ii_3_dsb, d_d_me_ii_4_dsb, d_d_me_ii_5_nrfab, d_d_me_ii_7_skpl, d_d_me_ii_6_mav),
    # electric 15
    de_e_dre93_1_dr,
    de_e_dre94_1_dr,
    grf.VariantGroup('њRc1/2/4/5', s_e_rc1245_1_sj, s_e_rc1245_6_sj, s_e_rc1245_2_sj, s_e_rc1245_3_sj, s_e_rc1245_4_sj, s_e_rc1245_5_sj),
    grf.VariantGroup('њ103', de_e_db103_1_db, de_e_db103_2_db, de_e_db103_3_db, de_e_db103_4_radve),
    grf.VariantGroup('њRc3/6', s_e_rc36_1_sj, s_e_rc36_2_sj, s_e_rc36_3_sj, s_e_rc36_4_sj, s_e_rc36_5_sj, s_e_rc36_6_sj, s_e_rc36_7_sj),
    grf.VariantGroup('њRm', s_e_rm_1_sj, s_e_rm_2_sj, s_e_rm_3_sj, s_e_rm_4_sj),
    s_e_rc7_1_sj,
    # electric 25
    grf.VariantGroup('њEA', d_e_ea_1_dsb, d_e_ea_2_dsb, d_e_ea_4_bulmarket, d_e_ea_5_db, d_e_ea_3_dsb),
    # electric dc
    # electric 3rd
    # dmu
    grf.VariantGroup('њML', d_d_ml_1_dsb, d_d_ml_2_dsb),
    d_d_mq_1_dsb,
    d_d_mp_1_dsb,
    grf.VariantGroup('MO', d_d_mo_ii_1_dsb, d_d_mo_iv_1_dsb, d_d_mo_v_1_dsb),
    grf.VariantGroup('њYd', s_d_Yd_1_sj, s_d_Yd_2_hnj, s_d_Yd_3_msj),
    grf.VariantGroup('њYo', s_d_Yo_1_sj, s_d_Yo_2_hnj),
    grf.VariantGroup('њYo1s', s_d_Yo1s_1_sj, s_d_Yo1s_2_bj, s_d_Yo1s_3_tgoj),
    grf.VariantGroup('њMR', d_d_mr_1_dsb, d_d_mr_2_dsb, d_d_mr_4_dsb, d_d_mr_3_dsb, d_d_mr_5_dsb, d_d_mr_6_dsb),
    grf.VariantGroup('њMF (IC3)/Y2', d_d_mf_1_dsb, s_d_mf_5_sj, d_d_mf_2_dsb, s_d_mf_6_sj, d_d_mf_3_dsb, d_d_mf_4_dsb),
    # emu 15
    grf.VariantGroup('њXoa3', s_e_Xoa3_1_bj, s_e_Xoa3_2_sj,),
    grf.VariantGroup('њXoa4', s_e_Xoa4_1_sj, s_e_Xoa4_2_sj, s_e_Cox4_1_sj, s_e_Cox4_2_sj,),
    grf.VariantGroup('њX1', s_e_X1_1_sj, s_e_X1_2_sl, s_e_X1_3_sl,),
    grf.VariantGroup('њBM69A', n_o_BM69A_1_nsb, n_o_BM69A_2_nsb, n_o_BM69A_3_nsb,),
    # emu 25
    grf.VariantGroup('њER (IR4)', d_e_er_1_dsb, d_e_er_2_dsb, d_e_er_3_dsb, d_e_er_4_dsb),
    grf.VariantGroup('њET (Øresundstog)', d_e_et_1_dsb, d_e_et_2_dsb),
    # emu dc
    n_o_Wes_1_hkb,
    grf.VariantGroup('њS-Tog 1', d_e_stog1_1_dsb, d_e_stog1_2_dsb, d_e_stog1_3_dsb, d_e_stog1_4_dsb, d_e_stog1_5_dsb),
    grf.VariantGroup('њOS T', n_o_T_1_os, n_o_T_2_os,),
    grf.VariantGroup('њS-Tog 2', d_e_stog2_1_dsb, d_e_stog2_2_dsb, d_e_stog2_9_dsb, d_e_stog2_3_dsb, d_e_stog2_4_dsb, d_e_stog2_5_dsb, d_e_stog2_6_dsb, d_e_stog2_7_dsb, d_e_stog2_8_dsb),
    grf.VariantGroup('њS-Tog 3', d_e_stog3_1_dsb, d_e_stog3_2_dsb, d_e_stog3_3_dsb, d_e_stog3_4_dsb),
    grf.VariantGroup('њS-Tog 4', d_e_stog4_1_dsb, d_e_stog4_3_dsb, d_e_stog4_4_dsb, d_e_stog4_2_dsb),
    # emu 3rd
    s_e_C1_1_ss,
    s_e_C4_1_ss,
    s_e_C4_2_sl,
    s_e_C5_1_ss,
    # carriages
    ch_p_2pax_1_sbb,
    ch_p_4pax_1_sbb,
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
    grf.VariantGroup('љњB II', d_p_b_ii_1_dsb, d_p_bk_iii_1_dsb, d_p_b_ii_2_dsb, d_p_bk_iii_2_dsb),
    # wagons
    ch_p_2bag_1_sbb,
    ch_p_4bag_1_sbb,
    s_w_Hbis_sj,
    s_w_Gblssy_2_gc,
    # narrow gauge
    grf.VariantGroup('њZ4p', s_d_Z4p_1_srj, s_d_Z4p_2, s_d_Z4p_3_nklj, s_d_Z4p_4, s_d_Z4p_5_donj, s_d_Z4p_6_sl, s_d_Z4p_7_sl,),
    s_d_Tp_1_sj,
    grf.VariantGroup('њX10p', s_e_X10p_1_sl, s_e_X10p_2_sl),
    s_p_Co_1,
    s_p_UBp_ii_1,
).set_variant_callbacks(g)))

grf.main(g, 'KST_Kitchen_Sink_Trains.grf')
