from datetime import date

import grf

import lib

g = grf.NewGRF(
    grfid=b'ROBT',
    name='SCATS',
    description='Scandinavian Trains made by Rob, dP and Brickblock',
)

Train = g.bind(lib.Train)


g.add(lib.set_global_train_y_offset(2))

g.add(lib.set_global_is_32(1))

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

def make_vox_liveries_12(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_12(filename),
    } for name, filename in liveries.items()]


def make_vox_liveries_11(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_11(filename),
    } for name, filename in liveries.items()]


def make_vox_liveries_10(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_10(filename),
    } for name, filename in liveries.items()]


def make_vox_liveries_9(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_9(filename),
    } for name, filename in liveries.items()]


    #use this for lenght 8 (0.5 tiles)
def make_vox_liveries_8(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_8(filename),
    } for name, filename in liveries.items()]
  
  #lenght 7
def make_vox_liveries_7(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_7(filename),
    } for name, filename in liveries.items()]

def make_vox_liveries_6(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_6(filename),
    } for name, filename in liveries.items()]

def make_vox_liveries_5(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_5(filename),
    } for name, filename in liveries.items()]

def make_vox_liveries_4(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_4(filename),
    } for name, filename in liveries.items()]

def make_vox_liveries_3(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_3(filename),
    } for name, filename in liveries.items()]

def make_vox_liveries_2(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_2(filename),
    } for name, filename in liveries.items()]

def make_vox_liveries_1(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train_1(filename),
    } for name, filename in liveries.items()]


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
    liveries=make_vox_liveries_8({
        'Maroon': 'z1954_DSB_MY_II_1_32bpp.png',
        'Black and Red': 'z1954_DSB_MY_II_2_32bpp.png',
        'Blue': 'z1954_DSB_MY_II_3_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_8({
        'Maroon': 'z1960_DSB_MX_II_1_32bpp.png',
        'Black and Red': 'z1960_DSB_MX_II_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_8({
        'Maroon': 'z1967_DSB_MZ_I_1_32bpp.png',
        'Black and Red': 'z1967_DSB_MZ_I_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_8({
        'Maroon': 'z1970_DSB_MZ_II_1_32bpp.png',
        'Black and Red': 'z1970_DSB_MZ_II_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_8({
        'Black and Red': 'z1972_DSB_MZ_III_1_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_8({
        'Black and Red': 'z1977_DSB_MZ_IV_1_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_6({
        'Orange and Turquoise': 'z1967_SJ_Rc1_1_32bpp.png',
        'Blue and Red': 'z1967_SJ_Rc1_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_6({
        'Orange and Turquoise': 'z1969_SJ_Rc2_1_32bpp.png',
        'Blue and Red Old': 'z1969_SJ_Rc2_2_32bpp.png',
        'Blue and Red New': 'z1969_SJ_Rc2_3_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_6({
        'Orange and Turquoise': 'z1970_SJ_Rc3_1_32bpp.png',
        'Blue and Red': 'z1970_SJ_Rc3_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_6({
        'Orange and Turquoise': 'z1975_SJ_Rc4_1_32bpp.png',
        'Blue and Red': 'z1975_SJ_Rc4_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_6({
        'Orange and Turquoise': 'z1982_SJ_Rc5_1_32bpp.png',
        'Blue and Red': 'z1982_SJ_Rc5_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_6({
        'Orange and Turquoise': 'z1984_SJ_Rc6_1_32bpp.png',
        'Blue and Red': 'z1984_SJ_Rc6_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_8({
        'White and Red': 'z1989_DSB_MF_IC3_MFA_1_32bpp.png',
        'Grey, Blue and Green': 'z1989_DSB_MF_IC3_MFA_2_32bpp.png',
        'Grey, Blue and Red': 'z1989_DSB_MF_IC3_MFA_3_32bpp.png',
        'Red and Black': 'z1989_DSB_MF_IC3_MFA_4_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries = make_vox_liveries_8({
        'White and Red': 'z1989_DSB_MF_IC3_FF_1_32bpp.png',
        'Grey, Blue and Green': 'z1989_DSB_MF_IC3_FF_2_32bpp.png',
        'Grey, Blue and Red': 'z1989_DSB_MF_IC3_FF_3_32bpp.png',
        'Red and Black': 'z1989_DSB_MF_IC3_FF_4_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=3602,
    liveries = make_vox_liveries_8({
        'White and Red': 'z1989_DSB_MF_IC3_MFB_1_32bpp.png',
        'Grey, Blue and Green': 'z1989_DSB_MF_IC3_MFB_2_32bpp.png',
        'Grey, Blue and Red': 'z1989_DSB_MF_IC3_MFB_3_32bpp.png',
        'Red and Black': 'z1989_DSB_MF_IC3_MFB_4_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
)

Train(
    id=4100,
    name='ER IR4',
    liveries=make_vox_liveries_8({
        'White and Red': 'z1993_DSB_ER_IR4_ER20_1_32bpp.png',
        'Grey, Blue and Green': 'z1993_DSB_ER_IR4_ER20_2_32bpp.png',
        'Grey, Blue and Red': 'z1993_DSB_ER_IR4_ER20_3_32bpp.png',
        'Red and Black': 'z1993_DSB_ER_IR4_ER20_4_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries = make_vox_liveries_8({
        'White and Red': 'z1993_DSB_ER_IR4_FR22_1_32bpp.png',
        'Grey, Blue and Green': 'z1993_DSB_ER_IR4_FR22_2_32bpp.png',
        'Grey, Blue and Red': 'z1993_DSB_ER_IR4_FR22_3_32bpp.png',
        'Red and Black': 'z1993_DSB_ER_IR4_FR22_4_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=4102,
    liveries = make_vox_liveries_8({
        'White and Red': 'z1993_DSB_ER_IR4_FR23_1_32bpp.png',
        'Grey, Blue and Green': 'z1993_DSB_ER_IR4_FR23_2_32bpp.png',
        'Grey, Blue and Red': 'z1993_DSB_ER_IR4_FR23_3_32bpp.png',
        'Red and Black': 'z1993_DSB_ER_IR4_FR23_4_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=4103,
    liveries = make_vox_liveries_8({
        'White and Red': 'z1993_DSB_ER_IR4_ER21_1_32bpp.png',
        'Grey, Blue and Green': 'z1993_DSB_ER_IR4_ER21_2_32bpp.png',
        'Grey, Blue and Red': 'z1993_DSB_ER_IR4_ER21_3_32bpp.png',
        'Red and Black': 'z1993_DSB_ER_IR4_ER21_4_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
)

Train(
    id=5600,
    name='S-Tog 1',
    liveries=make_vox_liveries_8({
        'Maroon': 'z1933_DSB_S-Tog_1_MM_1_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
        'Info': 'Leyland',
    }),
).add_articulated_part(
    id=5601,
    liveries = make_vox_liveries_8({
        'Maroon': 'z1933_DSB_S-Tog_1_FM_1_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=5602,
    liveries = make_vox_liveries_8({
        'Maroon': 'z1933_DSB_S-Tog_1_FS_1_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
)

Train(
    id=6600,
    name='ABs',
    liveries=make_vox_liveries_11({
        'White, Blue and Green': 'z2002_DSB_ABs_1_32bpp.png',
        'White, Blue and Red': 'z2002_DSB_ABs_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_11({
        'Brown': 'z1965_DSB_B_1_32bpp.png',
        'Red': 'z1967_DSB_B_1_32bpp.png',
        'Red and White': 'z1983_DSB_Bk_1_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
    introduction_date=date(1965, 1, 1),
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
    liveries=make_vox_liveries_10({
        'Brown and Yellow': 'z1966_DSB_A_1_32bpp.png',
        'Red and Yellow': 'z1967_DSB_A_1_32bpp.png',
        'Red': 'z1995_DSB_Ba_1_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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
    liveries=make_vox_liveries_10({
        'White, Blue and Green': 'z2002_DSB_B_II_1_32bpp.png',
        'White, Blue and Red': 'z2002_DSB_B_II_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
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

g.write('robs_trains.grf')
