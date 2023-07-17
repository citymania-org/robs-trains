import os
from datetime import date

import grf

import lib


PURCHASE_ICONS_DIR = 'purchase list'
DEBUG_DIR = 'debug'

os.makedirs(DEBUG_DIR, exist_ok=True)

g = grf.NewGRF(
    grfid=b'ROB1',
    name='SNDTS (ScaNDinavian Train Set)',
    description='Scandinavian Trains made by Rob, dP and Brickblock1',
    url='https://github.com/citymania-org/robs-trains',
    id_map_file='id_map.json',
)

Train = g.bind(lib.Train)

g.add(grf.SetGlobalTrainDepotYOffset(2))

g.add(grf.SetGlobalTrainMiscFlag(grf.GlobalTrainMiscFlag.DEPOT_FULL_TRAIN_WIDTH))

# railtype table
(
    standard_gauge,
    standard_gauge_multi,  # border crossing trains
    standard_gauge_dc,  # stog and saltsjöbanan
    standard_gauge_15kv,  # Sweden and Norway
    standard_gauge_25kv,  # Denmark
    metro,  # Metro
    p_gauge,  # Swedish 3 foot gauge
    p_gauge_dc,  # SRJ
    p_gauge_15kv,  # NKIJ
) = g.set_railtype_table([
    ('SAAN', 'RAIL'),  # Standard gauge track
    ('NORD', 'SAAE', 'ELRL'),  # Standard gauge 15kv and 25kv ac (will show up on dc most of the time)
    ('SAAd', 'SAAD', 'SAAE', 'ELRL'),  # Standard gauge 1,5kv and stog  dc
    ('SAAa', 'SAAA', 'SAAE', 'ELRL'),  # Standard gauge 15kv ac
    ('SAAA', 'SAAE', 'ELRL'),  # Standard gauge 25kv ac
    ('MTRO', 'SAA4', 'SAA3'),  # Standard gauge Metro (MTRO is first be because it is better definded as metro)
    ('nAAN', 'NAAN', 'NGRL'),  # Narrow gauge track
    ('nAAd', 'nAAD', 'nAAE', 'NAAd', 'NAAD', 'NAAE', 'ELNG'),  # Narrow gauge 3kv dc
    ('nAAa', 'nAAA', 'nAAE', 'NAAa', 'NAAA', 'NAAE', 'ELNG'),  # Narrow gauge 15kv ac
])

# we might need more narrow gauge types if we add norwegian or danish trains but it isn't super important and might not be neccesary


def tmpl_vox_train(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 8, 10, 44, xofs=-4,  yofs=-21),
        sprite( 20, 8, 42, 44, xofs=-24, yofs=-30),
        sprite( 70, 8, 69, 44, xofs=-35, yofs=-38),
        sprite(150, 8, 42, 44, xofs=-16, yofs=-30),
        sprite(200, 8, 10, 44, xofs=-4,  yofs=-21),
        sprite(220, 8, 42, 44, xofs=-24, yofs=-30),
        sprite(270, 8, 69, 44, xofs=-35, yofs=-38),
        sprite(350, 8, 42, 44, xofs=-16, yofs=-30),
    ]

# old templates
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
        'new': tmpl_vox_train,
    }
    tmpl = TEMPLATES[length]
    res = []
    for name, filename in liveries.items():
        data = {}

        if isinstance(filename, tuple):
            filename, intro_year = filename
            data['intro_year'] = intro_year

        if filename.endswith('.vox'):
            sprites = lib.VoxTrainFile(filename).make_sprites()
            if DEBUG_DIR is not None:
                debug_fname = os.path.join(DEBUG_DIR, os.path.basename(filename)[:-4]) + '.png'
                lib.make_debug_sprite_sheet(debug_fname, sprites, scale=5)
        else:
            sprites = tmpl(filename)

        res.append({
            **data,
            'name': f' ({name})',
            'sprites': sprites,
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
'''
# special alignment train
alignment16 = Train(
    id='alignment16',
    name='alignment 16',
    length=16,
    liveries=make_vox_liveries('new', {
        '': 'template.png'
    }),
    #country='sweden',
    company='na',
    power_type='multi',
    purchase_sprite_towed_id='alignment16',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_multi,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1954, 1, 1),
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
        'Info': 'Test locomotive',
    }),
).add_articulated_part(
    id=19,
    length=16,
    liveries=make_vox_liveries('new', {
        '': 'template.png'
    }),
)

Train(
    id='alignment_narrow',
    name='alignment narrow',
    length=16,
    liveries=make_vox_liveries('new', {
        '': 'template_narrow_gauge.png'
    }),
    #country='sweden',
    company='na',
    power_type='multi',
    purchase_sprite_towed_id='x10p',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=p_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1954, 1, 1),
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
        'Info': 'Test locomotive',
    }),
)

# regular trains

my_ii1 = Train(
    id='my_ii1',
    name='MY II',
    liveries=make_vox_liveries(8, {
        'Maroon': '1954_DK_MY_II_1_1954.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b1',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1954, 1, 1),
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

my_ii2 = Train(
    id='my_ii2',
    name='MY II',
    liveries=make_vox_liveries(8, {
        'Black and Red': '1954_DK_MY_II_2_1972.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1972, 1, 1),
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

my_ii3 = Train(
    id='my_ii3',
    name='MY II',
    liveries=make_vox_liveries(8, {
        'Blue': '1954_DK_MY_II_3_2004.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(2004, 1, 1),
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

mx_ii1 = Train(
    id='mx_ii1',
    name='MX II',
    liveries=make_vox_liveries(8, {
        'Maroon': '1960_DK_MX_II_1_1960.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b1',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1960, 1, 1),
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

mx_ii2 = Train(
    id='mx_ii2',
    name='MX II',
    liveries=make_vox_liveries(8, {
        'Black and Red': '1960_DK_MX_II_2_1972.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1972, 1, 1),
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
    
mz_i1 = Train(
    id='mz_i1',
    name='MZ I',
    liveries=make_vox_liveries(8, {
        'Maroon': '1967_DK_MZ_I_1_1967.png',
    }),
    length=7,
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b1',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
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

mz_i2 = Train(
    id='mz_i2',
    name='MZ I',
    liveries=make_vox_liveries(8, {
        'Black and Red': '1967_DK_MZ_I_2_1972.png',
    }),
    length=7,
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1972, 1, 1),
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

mz_ii1 = Train(
    id='mz_ii1',
    name='MZ II',
    liveries=make_vox_liveries(8, {
        'Maroon': '1967_DK_MZ_I_1_1967.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b1',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
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

mz_ii2 = Train(
    id='mz_ii2',
    name='MZ II',
    liveries=make_vox_liveries(8, {
        'Black and Red': '1967_DK_MZ_I_2_1972.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1972, 1, 1),
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

mz_iii1 = Train(
    id='mz_iii1',
    name='MZ III',
    liveries=make_vox_liveries(8, {
        'Black and Red': '1972_DK_MZ_III_1_1972.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1972, 1, 1),
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

mz_iv1 = Train(
    id='mz_iv1',
    name=' MZ IV',
    liveries=make_vox_liveries(8, {
        'Black and Red': '1977_DK_MZ_IV_1_1977.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(104),
    power=9999,
    introduction_date=date(1977, 1, 1),
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

me = Train(
    id=1012,
    name='ME',
    length=10,
    liveries=make_vox_liveries('new', {
        'ME': 'me.png',
    }),
    country='denmark',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='a1',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(174),
    power=3255,
    introduction_date=date(1981, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=122,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=0,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
'''
rc1 = Train(
    id='rc1',
    name='Rc1',
    shorten_by=2,
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1967_SE_Rc1_2_1990.png',
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
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red Old': '1967_SE_Rc1_2_1990.png',
        'Blue and Red New': '1969_SE_Rc2_3_1990.png',
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
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1969_SE_Rc2_3_1990.png',
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
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1969_SE_Rc2_3_1990.png',
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
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1969_SE_Rc2_3_1990.png',
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
    liveries=make_vox_liveries(6, {
        'Orange and Turquoise': '1967_SE_Rc1_1_1967.png',
        'Blue and Red': '1969_SE_Rc2_3_1990.png',
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

ea = Train(
    id=1651,
    name='EA',
    length=9,
    liveries=make_vox_liveries('new', {
        'EA': 'ea.png',
    }),
    country='denmark',
    company='na',
    power_type='25kv',
    purchase_sprite_towed_id='a1',
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge_25kv,
    max_speed=Train.kmhish(174),
    power=4962,
    introduction_date=date(1984, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=84,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=0,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
'''
mf_ic3 = Train(
    id='mf_ic3',
    name='MF IC3',
    liveries=make_vox_liveries(8, {
        'White and Red': '1989_DK_MF_IC3_MFA_1_1989.png',
        'Grey, Blue and Green': '1989_DK_MF_IC3_MFA_2_2005.png',
        'Grey, Blue and Red': '1989_DK_MF_IC3_MFA_3_2012.png',
        'Red and Black': '1989_DK_MF_IC3_MFA_4_2018.png',
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
    liveries=make_vox_liveries(8, {
        'White and Red': '1989_DK_MF_IC3_FF_1_1989.png',
        'Grey, Blue and Green': '1989_DK_MF_IC3_FF_2_2005.png',
        'Grey, Blue and Red': '1989_DK_MF_IC3_FF_3_2012.png',
        'Red and Black': '1989_DK_MF_IC3_FF_4_2018.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='mf_ic3_car3',
    liveries=make_vox_liveries(8, {
        'White and Red': '1989_DK_MF_IC3_MFB_1_1989.png',
        'Grey, Blue and Green': '1989_DK_MF_IC3_MFB_2_2005.png',
        'Grey, Blue and Red': '1989_DK_MF_IC3_MFB_3_2012.png',
        'Red and Black': '1989_DK_MF_IC3_MFB_4_2018.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

er_ir4 = Train(
    id='er_ir4',
    name='ER IR4',
    liveries=make_vox_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_ER20_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_ER20_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_ER20_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_ER20_4_2021.png',
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
    liveries=make_vox_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_FR22_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_FR22_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_FR22_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_FR22_4_2021.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='er_ir4_car3',
    liveries=make_vox_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_FR23_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_FR23_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_FR23_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_FR23_4_2021.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='er_ir4_car4',
    liveries=make_vox_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_ER21_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_ER21_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_ER21_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_ER21_4_2021.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

stog_1_2 = Train(
    id='stog_1_2',
    name='S-Tog 1 (2 Car)',
    liveries=make_vox_liveries(8, {
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
        'Info': 'Can be combined with 2 and 4 car sets to make sets of 6 and 8',
    }),
).add_articulated_part(
    id='stog_1_2_car2',
    liveries=make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FS_1_1933.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

stog_1_4 = Train(
    id='stog_1_4',
    name='S-Tog 1 (4 Car)',
    liveries=make_vox_liveries(8, {
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
        'Info': 'Can be combined with 2 and 4 car sets to make sets of 6 and 8',
    }),
).add_articulated_part(
    id='stog_1_4_car2',
    liveries=make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FM_1_1933.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='stog_1_4_car3',
    liveries=make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FM_1_1933.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='stog_1_4_car4',
    liveries=make_vox_liveries(8, {
        'Maroon': '1933_DK_S-Tog_1_FS_1_1933.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

abs1 = Train(
    id='abs1',
    name='ABs',
    liveries=make_vox_liveries(11, {
        'White, Blue and Green': '2002_DK_ABs_1_2002.png',
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
    liveries=make_vox_liveries(11, {
        'White, Blue and Red': '2002_DK_ABs_2_2012.png',
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
    liveries=make_vox_liveries(10, {
        'White, Blue and Green': '2002_DK_B_II_1_2002.png',
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
    liveries=make_vox_liveries(10, {
        'White, Blue and Red': '2002_DK_B_II_2_2012.png',
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

b1 = Train(
    id='b1',
    name='B',
    length=11,
    liveries=make_vox_liveries('new', {
        'Brown': '1964_DK_B_1_1964.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1964, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=80,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

b2 = Train(
    id='b2',
    name='B I',
    length=11,
    liveries=make_vox_liveries('new', {
        'Red (B I)': '1964_DK_B_2_(B_I)_1972.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=60,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

b3 = Train(
    id='b3',
    name='Bk I',
    length=11,
    liveries=make_vox_liveries('new', {
        'Red (Bk I)': '1964_DK_B_2_(B_I)_1972.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=48,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

b4 = Train(
    id='b4',
    name='Bk I',
    length=11,
    liveries=make_vox_liveries('new', {
        'Red and White Stripe (Bk I)': '1964_DK_B_4_(Bk_I)_1983.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1983, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=48,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

a1 = Train(
    id='a1',
    name='A',
    length=11,
    liveries=make_vox_liveries('new', {
        'Brown and Yellow': '1966_DK_A_1_1966.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1966, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=48,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

a2 = Train(
    id='a2',
    name='A',
    length=11,
    liveries=make_vox_liveries('new', {
        'Red and Yellow': '1966_DK_A_2_1972.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=48,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

a3 = Train(
    id='a3',
    name='Ba',
    length=11,
    liveries=make_vox_liveries('new', {
        'Red (Ba)': '1966_DK_A_3_(Ba)_1991.png',
    }),
    country='denmark',
    company='na',
    power_type='na',
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1991, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=48,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

# 891mm narrow gauge

ubp_i = Train(
    id='ubp_i',
    name='UBp',
    length=9,
    liveries=make_vox_liveries('new', {
        'Original': 'xxxx_SE_X10p_UBp_1_xxxx.png',
    }),
    engine_class=Train.EngineClass.ELECTRIC,
    sound_effects=modern_diesel_sound,
    track_type=p_gauge,
    country='sweden',
    company='na',
    power_type='dc',
    purchase_sprite_towed_id='ubp_i',
    max_speed=Train.kmhish(80),
    power=0,
    introduction_date=date(1988, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(16.6)),
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=80,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Info': 'Built by ABB railcar. Part of a major refurbisment of Roslagsbanan',
    }),
)

x10p = Train( # todo make it work with the length for mus
    id='x10p',
    name='X10p',
    length=9,
    liveries=make_vox_liveries('new', {
        'Original': 'xxxx_SE_X10p_X10p_1_xxxx.png',
        'Overhauled': ('xxxx_SE_X10p_X10p_2_xxxx.png', 2011)
    }),
    country='sweden',
    company='na',
    power_type='dc',
    purchase_sprite_towed_id='x10p_car2',
    engine_class=Train.EngineClass.ELECTRIC, # unsure about how to enter stats due to units
    sound_effects=modern_diesel_sound,
    track_type=p_gauge_dc,
    max_speed=Train.kmhish(80),
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
        'Info': 'Built by ABB railcar. Part of a major refurbisment of Roslagsbanan',
    }),
    callbacks={'properties': {'cargo_capacity': 0},}
).add_articulated_part(
    id='x10p_car2',
    length=9,
    liveries=make_vox_liveries('new', {
        'Original': 'xxxx_SE_X10p_UBp_1_xxxx.png',
        'Overhauled': 'xxxx_SE_X10p_UBp_2_xxxx.png',
    }),
    cargo_capacity=80,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='x10p_car3',
    length=9,
    liveries=make_vox_liveries('new', {
        'Original': 'xxxx_SE_X10p_UBxp_1_xxxx.png',
        'Overhauled': 'xxxx_SE_X10p_UBxp_2_xxxx.png',
    }),
    cargo_capacity=76,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
'''
Tp = Train( 
    id='tp',
    name='Tp',
    length=5,
    liveries=make_vox_liveries('new', {
        'Original': 'xxxx_SE_Tp_1_xxxx.png',
    }),
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='tp',
    engine_class=Train.EngineClass.DIESEL, # unsure about how to enter stats due to units
    sound_effects=modern_diesel_sound,
    track_type=p_gauge,
    max_speed=Train.kmhish(80),
    power=778,
    introduction_date=date(1953, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=46,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=0,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS, # can't be NONE 
    additional_text=grf.fake_vehicle_info({
        'Info': "SJ's larger narrow gauge loco",
    }),
    callbacks={'properties': {'cargo_capacity': 0},}
)



Z4p = Train( # Sport model as variant?
    id='z4p',
    name='Z4p',
    length=3,
    liveries=make_vox_liveries('new', {
        'SRJ/SJ': '1947_SE_Z4p_1_1947.png',
        'NKIJ': '1947_SE_Z4p_2_xxxx.png',
        'DONJ': '1947_SE_Z4p_3_xxxx.png',
        'SL Grey and yellow': '1947_SE_Z4p_4_xxxx.png',
        'SL Red': '1947_SE_Z4p_5_xxxx.png',
    
    }),
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='z4p',
    engine_class=Train.EngineClass.DIESEL, # unsure about how to enter stats due to units
    sound_effects=modern_diesel_sound,
    track_type=p_gauge,
    max_speed=Train.kmhish(40),
    power=160,
    introduction_date=date(1947, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=1,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS, # can't be NONE
    additional_text=grf.fake_vehicle_info({
        'Info': 'The most common diesel locomotive on narrow gauge lines. The first ones were acquired by SRJ, with other private companies and SJ following suit',
    }),
    callbacks={'properties': {'cargo_capacity': 0},}
)

x15p = Train( # todo make it work with the length for mus
    id='x15p',
    name='X15p',
    length=9,
    liveries=make_vox_liveries('new', {
        'Original': 'xxxx_SE_X10p_X10p_1_xxxx.png',
    }),
    country='sweden', 
    company='sl',
    power_type='dc',
    purchase_sprite_towed_id='x15p_car2',
    engine_class=Train.EngineClass.ELECTRIC, # unsure about how to enter stats due to units
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
    liveries=make_vox_liveries('new', {
        'Original': 'xxxx_SE_X10p_UBp_1_xxxx.png',
    }),
    cargo_capacity=80,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='x15p_car3',
    length=9,
    liveries=make_vox_liveries('new', {
        'Original': 'xxxx_SE_X10p_UBxp_1_xxxx.png',
    }),
    cargo_capacity=76,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
'''
purchase_icon = lambda fname: grf.FileSprite(grf.ImageFile(os.path.join(PURCHASE_ICONS_DIR, fname)), 0, 0, None, None)


COUNTRY_SPRITES = {
    'switzerland': purchase_icon('fch.png'),
    'germany': purchase_icon('fde.png'),
    'denmark': purchase_icon('fdk.png'),
    'france': purchase_icon('ffr.png'),
    'hrvatska': purchase_icon('fhr.png'),
    'italy': purchase_icon('fit.png'),
    'norway': purchase_icon('fno.png'),
    'srbija': purchase_icon('frs.png'),
    'russia': purchase_icon('fru.png'),
    'sweden': purchase_icon('fse.png'),
    'ussr': purchase_icon('fsu.png'),
    'jugoslavija': purchase_icon('fyu.png'),
}


COMPANY_SPRITES = {
    'na': purchase_icon('lblank.png'),
    'cmetro': purchase_icon('lcmetro.png'),
    'øresundståg': purchase_icon('løresundståg.png'),
    'stog': purchase_icon('lstog.png'),
    'sl': purchase_icon('lsl.png')
}


POWER_TYPE_SPRITES = {
    'diesel': purchase_icon('pdiesel.png'),
    '3rd': purchase_icon('pelectric3.png'),
    'dual': purchase_icon('pelectricdv.png'),
    'metro': purchase_icon('pelectricm.png'),
    'steam': purchase_icon('psteam.png'),
    'multi': purchase_icon('pelectricw.png'),  # replece these sprites
    'dc': purchase_icon('pelectricw.png'),
    '15kv': purchase_icon('pelectricw.png'),
    '25kv': purchase_icon('pelectricw.png'),
    'na': purchase_icon('pblank.png')
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

(g.add(grf.SetPurchaseOrder(
    #grf.VariantGroup(
    #    'MY II',
        #my_ii1,
        #my_ii2,
        #my_ii3,
    #),
    #grf.VariantGroup(
    #    'MX II',
        #mx_ii1,
        #mx_ii2,
    #),
    #grf.VariantGroup(
    #    'MZ',
        #mz_iii1,
        #mz_iv1,
    #    grf.VariantGroup(
    #        'MZ I',
            #mz_i1,
            #mz_i2,
    #    ),
    #    grf.VariantGroup(
    #        'MZ II',
            #mz_ii1,
            #mz_ii2,
    #    ),
    #),
    me,
    #grf.VariantGroup(
    #    'Rc',
        #rc1,
        #rc2,
        #rc3,
        #rc4,
        #rc5,
        #rc6,
    #),
    ea,
    #mf_ic3,
    #er_ir4,
    #stog_1_2,
    #stog_1_4,
    #grf.VariantGroup(
    #    'ABs',
        #abs1,
        #abs2,
    #),
    grf.VariantGroup(
        'B',
        b1,
        b2,
        b3,
        b4,
    ),
    grf.VariantGroup(
        'A',
        a1,
        a2,
        a3,
    ),
    #grf.VariantGroup(
    #    'B II',
    #    b_ii1,
    #    b_ii2,
    #),
    #Z4p,
    #Tp,
    ubp_i,
    x10p,
).set_variant_callbacks(g)))

g.write('robs_trains.grf')
