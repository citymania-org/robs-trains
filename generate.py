import os
from datetime import date

import grf

import lib


PURCHASE_ICONS_DIR = 'ztemps/purchase list'


g = grf.NewGRF(
    grfid=b'ROBT',
    name='SCATS',
    description='Scandinavian Trains made by Rob, dP and Brickblock',
)

Train = g.bind(lib.Train)


g.add(lib.set_global_train_y_offset(2))

g.add(lib.set_global_train_depot_width_32())

def tmpl_vox_train_12(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def tmpl_vox_train_11(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def tmpl_vox_train_10(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def tmpl_vox_train_9(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def tmpl_vox_train_8(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 16, 44, xofs=- 7, yofs=-29),
        sprite( 24, 0, 34, 32, xofs=-12, yofs=-21),
        sprite( 66, 0, 47, 26, xofs=-24, yofs=-20),
        sprite(121, 0, 34, 32, xofs=-12, yofs=-21),
        sprite(163, 0, 16, 44, xofs=- 7, yofs=-29),
        sprite(187, 0, 34, 32, xofs=-12, yofs=-21),
        sprite(229, 0, 47, 26, xofs=-24, yofs=-20),
        sprite(284, 0, 34, 32, xofs=-12, yofs=-21),
    ]

def tmpl_vox_train_7(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 16, 42, xofs=- 7, yofs=-29),
        sprite( 24, 0, 32, 31, xofs=-19, yofs=-21),
        sprite( 64, 0, 47, 26, xofs=-24, yofs=-20),
        sprite(119, 0, 32, 31, xofs=-14, yofs=-21),
        sprite(159, 0, 16, 42, xofs=- 7, yofs=-19),
        sprite(183, 0, 32, 31, xofs=-19, yofs=-21),
        sprite(223, 0, 47, 26, xofs=-24, yofs=-20),
        sprite(278, 0, 32, 31, xofs=-14, yofs=-21),
    ]

def tmpl_vox_train_6(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 16, 42, xofs=- 7, yofs=-28),
        sprite( 24, 0, 32, 31, xofs=-17, yofs=-21),
        sprite( 64, 0, 47, 26, xofs=-20, yofs=-20),
        sprite(119, 0, 32, 31, xofs=- 9, yofs=-19),
        sprite(159, 0, 16, 42, xofs=- 7, yofs=-24),
        sprite(183, 0, 32, 31, xofs=-21, yofs=-19),
        sprite(223, 0, 47, 26, xofs=-28, yofs=-20),
        sprite(278, 0, 32, 31, xofs=-13, yofs=-21),
    ]

def tmpl_vox_train_5(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def tmpl_vox_train_4(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def tmpl_vox_train_3(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def tmpl_vox_train_2(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def tmpl_vox_train_1(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 15, 40, xofs=-7, yofs=-16),
        sprite( 28, 0, 29, 31, xofs=-15, yofs=-16),
        sprite( 70, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(123, 0, 29, 31, xofs=-10, yofs=-16),
        sprite(165, 0, 15, 40, xofs=-7, yofs=-16),
        sprite(193, 0, 29, 31, xofs=-15, yofs=-16),
        sprite(235, 0, 45, 26, xofs=-10, yofs=-16),
        sprite(288, 0, 29, 31, xofs=-10, yofs=-16),
    ]

def make_vox_liveries(length, liveries):
    TEMPLATES = {
        1: tmpl_vox_train_1,
        2: tmpl_vox_train_2,
        3: tmpl_vox_train_3,
        4: tmpl_vox_train_4,
        5: tmpl_vox_train_5,
        6: tmpl_vox_train_6,
        7: tmpl_vox_train_7,
        8: tmpl_vox_train_8,
        9: tmpl_vox_train_9,
        10: tmpl_vox_train_10,
        11: tmpl_vox_train_11,
        12: tmpl_vox_train_12,
    }
    tmpl = TEMPLATES[length]
    res = []
    for name, filename in liveries.items():
        if isinstance(filename, tuple):
            filename, intro_year = filename
            res.append({
                'name': f' ({name})',
                'intro_year': intro_year,
                'sprites': tmpl(filename),
            })
        else:
            res.append({
                'name': f' ({name})',
                'sprites': tmpl(filename),
            })
    return res
# Using sound files from RUKTS: https://github.com/StarRaid/Representitive-UK-Trainset
modern_diesel_sound = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/modern_diesel_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/modern_diesel_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/modern_diesel_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/horn_4.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.BREAKDOWN_TRAIN_SHIP,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/horn_4.wav'),
}


Train(
    id=1100,
    name='MY II',
    liveries=make_vox_liveries(8, {
        'Maroon': '1954_DK_MY_II_1_1954.png',
        'Black and Red': ('1954_DK_MY_II_2_1972.png', 1972),
        'Blue': ('1954_DK_MY_II_3_2004.png', 2004),
    }),
    country='danmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id=1100,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1954, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1110,
    name='MX II',
    liveries=make_vox_liveries(8, {
        'Maroon': '1960_DK_MX_II_1_1960.png',
        'Black and Red': '1960_DK_MX_II_2_1972.png',
    }),
    country='danmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id=1110,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1960, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1120,
    name='MZ I',
    liveries=make_vox_liveries(8, {
        'Maroon': '1967_DK_MZ_I_1_1967.png',
        'Black and Red': '1967_DK_MZ_I_2_1972.png',
    }),
    country='danmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id=1120,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1967, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1125,
    name='MZ II',
    liveries=make_vox_liveries(8, {
        'Maroon': '1967_DK_MZ_I_1_1967.png',
        'Black and Red': '1967_DK_MZ_I_2_1972.png',
    }),
    country='danmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id=1125,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1970, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1130,
    name='MZ III',
    liveries=make_vox_liveries(8, {
        'Black and Red': '1972_DK_MZ_III_1_1972.png',
    }),
    country='danmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id=1130,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1135,
    name=' MZ IV',
    liveries=make_vox_liveries(8, {
        'Black and Red': '1977_DK_MZ_IV_1_1977.png',
    }),
    country='danmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id=1135,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1977, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1600,
    name='Rc1',
    shorten_by=2,
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1967_SE_Rc1_2_1997.png',
    }),
    country='sverige',
    company='na',
    power_type='ohle',
    purchase_sprite_towed_id=1600,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1967, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1610,
    name='Rc2',
    shorten_by=2,
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red Old': '1967_SE_Rc1_2_1997.png',
        'Blue and Red New': '1969_SE_Rc2_3_1997.png',
    }),
    country='sverige',
    company='na',
    power_type='ohle',
    purchase_sprite_towed_id=1610,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1969, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1620,
    name='Rc3',
    shorten_by=2,
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1969_SE_Rc2_3_1997.png',
    }),
    country='sverige',
    company='na',
    power_type='ohle',
    purchase_sprite_towed_id=1620,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1970, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1630,
    name='Rc4',
    shorten_by=2,
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1969_SE_Rc2_3_1997.png',
    }),
    country='sverige',
    company='na',
    power_type='ohle',
    purchase_sprite_towed_id=1630,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1975, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1640,
    name='Rc5',
    shorten_by=2,
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1969_SE_Rc2_3_1997.png',
    }),
    country='sverige',
    company='na',
    power_type='ohle',
    purchase_sprite_towed_id=1640,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1982, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=1650,
    name='Rc6',
    shorten_by=2,
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1969_SE_Rc2_3_1997.png',
    }),
    country='sverige',
    company='na',
    power_type='ohle',
    purchase_sprite_towed_id=1650,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1984, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'A Cool train',
    }),
)

Train(
    id=3600,
    name='MF IC3',
    liveries=make_vox_liveries(8, {
        'White and Red': '1989_DK_MF_IC3_MFA_1_1989.png',
        'Grey, Blue and Green': '1989_DK_MF_IC3_MFA_2_2005.png',
        'Grey, Blue and Red': '1989_DK_MF_IC3_MFA_3_2012.png',
        'Red and Black': '1989_DK_MF_IC3_MFA_4_2018.png',
    }),
    country='danmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id=3601,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1989, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
).add_articulated_part(
    id=3601,
    liveries = make_vox_liveries(8, {
        'White and Red': '1989_DK_MF_IC3_FF_1_1989.png',
        'Grey, Blue and Green': '1989_DK_MF_IC3_FF_2_2005.png',
        'Grey, Blue and Red': '1989_DK_MF_IC3_FF_3_2012.png',
        'Red and Black': '1989_DK_MF_IC3_FF_4_2018.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=3602,
    liveries = make_vox_liveries(8, {
        'White and Red': '1989_DK_MF_IC3_MFB_1_1989.png',
        'Grey, Blue and Green': '1989_DK_MF_IC3_MFB_2_2005.png',
        'Grey, Blue and Red': '1989_DK_MF_IC3_MFB_3_2012.png',
        'Red and Black': '1989_DK_MF_IC3_MFB_4_2018.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
)

Train(
    id=4100,
    name='ER IR4',
    liveries=make_vox_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_ER20_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_ER20_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_ER20_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_ER20_4_2021.png',
    }),
    country='danmark',
    company='na',
    power_type='ohle',
    purchase_sprite_towed_id=4101,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1993, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
).add_articulated_part(
    id=4101,
    liveries = make_vox_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_FR22_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_FR22_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_FR22_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_FR22_4_2021.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=4102,
    liveries = make_vox_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_FR23_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_FR23_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_FR23_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_FR23_4_2021.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=4103,
    liveries = make_vox_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_ER21_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_ER21_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_ER21_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_ER21_4_2021.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
)

Train(
    id=5600,
    name='S-Tog 1 (2 Car)',
    liveries=make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_MM_1_1933.png',
    }),
    country='danmark',
    company='stog',
    power_type='ohle',
    purchase_sprite_towed_id=5603,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1933, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Can be combined with 2 and 4 car sets to make sets of 6 and 8',
    }),
).add_articulated_part(
    id=5603,
    liveries = make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FS_1_1933.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
)

Train(
    id=5601,
    name='S-Tog 1 (4 Car)',
    liveries=make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_MM_1_1933.png',
    }),
    country='danmark',
    company='stog',
    power_type='ohle',
    purchase_sprite_towed_id=5602,
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=9999,
    introduction_date=date(1933, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Can be combined with 2 and 4 car sets to make sets of 6 and 8',
    }),
).add_articulated_part(
    id=5602,
    liveries = make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FM_1_1933.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=5602,
    liveries = make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FM_1_1933.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=5603,
    liveries = make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FS_1_1933.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
)

Train(
    id=6600,
    name='ABs',
    liveries=make_vox_liveries(11, {
        'White, Blue and Green': '2002_DK_ABs_1_2002.png',
        'White, Blue and Red': '2002_DK_ABs_2_2012.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=0,
    introduction_date=date(2002, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=7100,
    name='B',
    liveries=make_vox_liveries(11, {
        'Brown': '1964_DK_B_1_1964.png',
        'Red (B I)': '1964_DK_B_2_(B_I)_1972.png',
        'Red (Bk I)': '1964_DK_B_3_(Bk_I)_1974.png',
        'Red and White (Bk I)': '1964_DK_B_4_(Bk_I)_1983.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=0,
    introduction_date=date(1964, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=7110,
    name='A',
    liveries=make_vox_liveries(10, {
        'Brown and Yellow': '1966_DK_A_1_1966.png',
        'Red and Yellow': '1966_DK_A_2_1972.png',
        'Red (Ba)': '1966_DK_A_3_(Ba)_1991.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=0,
    introduction_date=date(1966, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

Train(
    id=7120,
    name='B II',
    liveries=make_vox_liveries(10, {
        'White, Blue and Green': '2002_DK_B_II_1_2002.png',
        'White, Blue and Red': '2002_DK_B_II_2_2012.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=0,
    introduction_date=date(2002, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=90,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Leyland',
    }),
)

purchase_icon = lambda fname: grf.FileSprite(grf.ImageFile(os.path.join(PURCHASE_ICONS_DIR, fname)), 0, 0, None, None)


COUNTRY_SPRITES = {
    'switzerland': purchase_icon('fch.png'),
    'germany': purchase_icon('fde.png'),
    'danmark': purchase_icon('fdk.png'),
    'france': purchase_icon('ffr.png'),
    'hrvatska': purchase_icon('fhr.png'),
    'italy': purchase_icon('fit.png'),
    'norge': purchase_icon('fno.png'),
    'srbija': purchase_icon('frs.png'),
    'russia': purchase_icon('fru.png'),
    'sverige': purchase_icon('fse.png'),
    'sssr': purchase_icon('fsu.png'),
    'jugoslavija': purchase_icon('fyu.png'),
}


COMPANY_SPRITES = {
    'na': purchase_icon('lblank.png'),
    'cmetro': purchase_icon('lcmetro.png'),
    'øresundståg': purchase_icon('løresundståg.png'),
    'stog': purchase_icon('lstog.png'),
}


POWER_TYPE_SPRITES = {
    'diesel': purchase_icon('pdiesel.png'),
    '3rd': purchase_icon('pelectric3.png'),
    'dual': purchase_icon('pelectricdv.png'),
    'metro': purchase_icon('pelectricm.png'),
    'ohle': purchase_icon('pelectricw.png'),
    'steam': purchase_icon('psteam.png'),
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
        'checker': (-4, 4),
    },
    # debug_dir='debug_purchase',
)

g.write('robs_trains.grf')
