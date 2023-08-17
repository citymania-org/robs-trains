import os
from datetime import date

import grf

import lib


PURCHASE_ICONS_DIR = 'purchase list'
DEBUG_DIR = 'debug'

os.makedirs(DEBUG_DIR, exist_ok=True)

PALETTE = lib.read_palette_file('pal.png')
BLACK1 = PALETTE[0: 4] + PALETTE[8: 12]
MAGENTA = PALETTE[44: 52]
PINK = PALETTE[52: 60]
RED = PALETTE[60: 68]
MAROON = PALETTE[68: 76]
ORANGE = PALETTE[76: 84]
BROWN = PALETTE[84: 92]
REDBROWN = PALETTE[92: 100]
YELLOWBROWN = PALETTE[100: 108]
DCREAM = PALETTE[108: 116]
CREAM = PALETTE[116: 124]
YELLOW = PALETTE[124: 132]
LIME = PALETTE[132: 140]
GREEN = PALETTE[140: 148]
DGREEN = PALETTE[148: 156]
TURQUOISE = PALETTE[156: 164]
DTURQUOISE = PALETTE[164: 172]
SKY = PALETTE[172: 180]
BLUE = PALETTE[180: 188]
DBLUE = PALETTE[188: 196]
COLBALT = PALETTE[196: 204]
MAUVE = PALETTE[204: 212]
LAVENDER = PALETTE[212: 220]
PURPLE = PALETTE[220: 228]
DPURPLE = PALETTE[228: 236]

g = grf.NewGRF(
    grfid=b'KSTA',
    name='KST SNDTS (ScaNDinavian Train Set)',
    description='Scandinavian Trains made by Rob, dP and Brickblock1',
    url='https://github.com/citymania-org/ro.bs-trains',
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


def tmpl_train(func):
    return [
        func(  0, 8, 10, 44, xofs=-4,  yofs=-21),
        func( 20, 8, 42, 44, xofs=-24, yofs=-30),
        func( 70, 8, 69, 44, xofs=-35, yofs=-38),
        func(150, 8, 42, 44, xofs=-16, yofs=-30),
        func(200, 8, 10, 44, xofs=-4,  yofs=-21),
        func(220, 8, 42, 44, xofs=-24, yofs=-30),
        func(270, 8, 69, 44, xofs=-35, yofs=-38),
        func(350, 8, 42, 44, xofs=-16, yofs=-30),
    ]

Livery = lib.LiveryFactory(tmpl_train)

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
    liveries=make_liveries({
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
    liveries=make_liveries({
        '': 'template.png'
    }),
)

Train(
    id='alignment_narrow',
    name='alignment narrow',
    length=16,
    liveries=make_liveries({
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
    liveries=make_liveries(8, {
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
    liveries=make_liveries(8, {
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
    liveries=make_liveries(8, {
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
    liveries=make_liveries(8, {
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
    liveries=make_liveries(8, {
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
)'''


mzi1 = Train(
    id='mzi1',
    name='MZ I',
    length=10,
    liveries={
        'Maroon and Cream': Livery('cc1967_DK_MZ_I_1_1967.png', cc_replace=MAROON, cc2_replace=DCREAM),
        '2CC': Livery('cc1967_DK_MZ_I_1_1967.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(143),
    power=3300,
    introduction_date=date(1967, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=117,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

mzi2 = Train(
    id='mzi2',
    name='MZ I',
    length=10,
    liveries={
        'Black and Red': Livery('cc1967_DK_MZ_I_2_1972.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1967_DK_MZ_I_2_1972.png', auto_cc=True),
        '2CC alt': Livery('cc1967_DK_MZ_I_2alt_1972.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(143),
    power=3300,
    introduction_date=date(1972, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=117,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

mzi3 = Train(
    id='mzi3',
    name='MZ I',
    length=10,
    liveries={
        'Black and Red': Livery('cc1967_DK_MZ_I_3_1986.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1967_DK_MZ_I_3_1986.png', auto_cc=True),
        '2CC alt': Livery('cc1967_DK_MZ_I_3alt_1986.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(143),
    power=3300,
    introduction_date=date(1986, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=117,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

mzii1 = Train(
    id='mzii1',
    name='MZ II',
    length=10,
    liveries={
        'Maroon and Cream': Livery('cc1967_DK_MZ_I_1_1967.png', cc_replace=MAROON, cc2_replace=DCREAM),
        '2CC': Livery('cc1967_DK_MZ_I_1_1967.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(143),
    power=3300,
    introduction_date=date(1970, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=117,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

mzii2 = Train(
    id='mzii2',
    name='MZ II',
    length=10,
    liveries={
        'Black and Red': Livery('cc1967_DK_MZ_I_2_1972.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1967_DK_MZ_I_2_1972.png', auto_cc=True),
        '2CC alt': Livery('cc1967_DK_MZ_I_2alt_1972.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(143),
    power=3300,
    introduction_date=date(1972, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=117,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

mzii3 = Train(
    id='mzii3',
    name='MZ II',
    length=10,
    liveries={
        'Black and Red': Livery('cc1967_DK_MZ_I_3_1986.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1967_DK_MZ_I_3_1986.png', auto_cc=True),
        '2CC alt': Livery('cc1967_DK_MZ_I_3alt_1986.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(143),
    power=3300,
    introduction_date=date(1986, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=117,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

mziii1 = Train(
    id='mziii1',
    name='MZ III',
    length=10,
    liveries={
        'Black and Red': Livery('cc1972_DK_MZ_III_1_1972.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1972_DK_MZ_III_1_1972.png', auto_cc=True),
        '2CC alt': Livery('cc1972_DK_MZ_III_1alt_1972.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(165),
    power=3900,
    introduction_date=date(1972, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=125,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

mziii2 = Train(
    id='mziii2',
    name='MZ III',
    length=10,
    liveries={
        'Black and Red': Livery('cc1972_DK_MZ_III_2_1986.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1972_DK_MZ_III_2_1986.png', auto_cc=True),
        '2CC alt': Livery('cc1972_DK_MZ_III_2alt_1986.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(165),
    power=3900,
    introduction_date=date(1986, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=125,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

mziv1 = Train(
    id='mziv1',
    name='MZ IV',
    length=10,
    liveries={
        'Black and Red': Livery('cc1977_DK_MZ_IV_1_1977.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1977_DK_MZ_IV_1_1977.png', auto_cc=True),
        '2CC alt': Livery('cc1977_DK_MZ_IV_1alt_1977.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(165),
    power=3900,
    introduction_date=date(1977, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=123,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

meii1 = Train(
    id='meii1',
    name='ME II',
    length=10,
    liveries={
        'Black and Red': Livery('cc1981_DK_ME_II_1_1981.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1981_DK_ME_II_1_1981.png', auto_cc=True),
        '2CC alt': Livery('cc1981_DK_ME_II_1alt_1981.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(175),
    power=3300,
    introduction_date=date(1981, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=122,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's final diesel locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

meii2 = Train(
    id='meii2',
    name='ME II',
    length=10,
    liveries={
        'Red and Blue': Livery('cc1981_DK_ME_II_2_2000.png', cc_replace=RED, cc2_replace=COLBALT),
        '2CC': Livery('cc1981_DK_ME_II_2_2000.png', auto_cc=True),
        '2CC alt': Livery('cc1981_DK_ME_II_3_2006.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(175),
    power=3300,
    introduction_date=date(2000, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=122,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's final diesel locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

meii3 = Train(
    id='meii3',
    name='ME II',
    length=10,
    liveries={
        'Blue and Red': Livery('cc1981_DK_ME_II_3_2006.png', cc_replace=RED, cc2_replace=COLBALT),
        '2CC': Livery('cc1981_DK_ME_II_3_2006.png', auto_cc=True),
        '2CC alt': Livery('cc1981_DK_ME_II_2_2000.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(175),
    power=3300,
    introduction_date=date(2006, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=122,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's final diesel locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

meii4 = Train(
    id='meii4',
    name='ME II',
    length=10,
    liveries={
        'Red': Livery('cc1981_DK_ME_II_4_2016.png', cc_replace=RED, cc2_replace=RED),
        '2CC': Livery('cc1981_DK_ME_II_4_2016.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(175),
    power=3300,
    introduction_date=date(2016, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=122,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's final diesel locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

'''
rc1 = Train(
    id='rc1',
    name='Rc1',
    shorten_by=2,
    liveries=make_liveries(6, {
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
    liveries=make_liveries(6, {
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
    liveries=make_liveries(6, {
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
    liveries=make_liveries(6, {
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
    liveries=make_liveries(6, {
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
    liveries=make_liveries(6, {
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

ea1 = Train(
    id='ea1',
    name='EA',
    length=9,
    liveries={
        'Black and Red': Livery('cc1984_DK_EA_1_1984.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('cc1984_DK_EA_1_1984.png', auto_cc=True),
        '2CC alt': Livery('cc1984_DK_EA_1alt_1984.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='25kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_25kv,
    max_speed=Train.kmhish(175),
    power=4962,
    introduction_date=date(1984, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=84,
    tractive_effort_coefficient=150,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's first electric locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

ea2 = Train(
    id='ea2',
    name='EA',
    length=9,
    liveries={
        'Blue and Red': Livery('cc1984_DK_EA_2_2006.png', cc_replace=RED, cc2_replace=COLBALT),
        '2CC': Livery('cc1984_DK_EA_2_2006.png', auto_cc=True),
        '2CC alt': Livery('cc1984_DK_EA_2alt_2006.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='25kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_25kv,
    max_speed=Train.kmhish(175),
    power=4962,
    introduction_date=date(2006, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=84,
    tractive_effort_coefficient=150,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's first electric locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

ea3 = Train(
    id='ea3',
    name='EA',
    length=9,
    liveries={
        'Red': Livery('cc1984_DK_EA_3_2017.png', cc_replace=RED, cc2_replace=RED),
        '2CC': Livery('cc1984_DK_EA_3_2017.png', auto_cc=True),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='25kv',
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=standard_gauge_25kv,
    max_speed=Train.kmhish(175),
    power=4962,
    introduction_date=date(2017, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=84,
    tractive_effort_coefficient=150,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=30,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's first electric locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)
'''
mf_ic3 = Train(
    id='mf_ic3',
    name='MF IC3',
    liveries=make_liveries(8, {
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
    liveries=make_liveries(8, {
        'White and Red': '1989_DK_MF_IC3_FF_1_1989.png',
        'Grey, Blue and Green': '1989_DK_MF_IC3_FF_2_2005.png',
        'Grey, Blue and Red': '1989_DK_MF_IC3_FF_3_2012.png',
        'Red and Black': '1989_DK_MF_IC3_FF_4_2018.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='mf_ic3_car3',
    liveries=make_liveries(8, {
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
    liveries=make_liveries(8, {
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
    liveries=make_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_FR22_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_FR22_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_FR22_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_FR22_4_2021.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='er_ir4_car3',
    liveries=make_liveries(8, {
        'White and Red': '1993_DK_ER_IR4_FR23_1_1993.png',
        'Grey, Blue and Green': '1993_DK_ER_IR4_FR23_2_2005.png',
        'Grey, Blue and Red': '1993_DK_ER_IR4_FR23_3_2012.png',
        'Red and Black': '1993_DK_ER_IR4_FR23_4_2021.png',
    }),
    cargo_capacity=90,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='er_ir4_car4',
    liveries=make_liveries(8, {
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
        'Info': 'Can be combined with 2 and 4 car sets to make sets of 6 and 8',
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
        'Info': 'Can be combined with 2 and 4 car sets to make sets of 6 and 8',
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
)

abs1 = Train(
    id='abs1',
    name='ABs',
    liveries=make_liveries(11, {
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
    liveries=make_liveries(11, {
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
    liveries=make_liveries(10, {
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
    liveries=make_liveries(10, {
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
    liveries={
        'Brown': Livery('1964_DK_B_1_1964.png'),
        '2CC': Livery('1964_DK_B_1_1964.png', mask='mc1964_DK_B_1_1964.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='b1',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1964, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=80,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

b2 = Train(
    id='b2',
    name='B I',
    length=11,
    liveries={
        'Red': Livery('1964_DK_B_2_(B_I)_1967.png'),
        '2CC': Livery('1964_DK_B_2_(B_I)_1967.png', mask='mc1964_DK_B_2_(B_I)_1967.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1967, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=80,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': '2nd class',
    }),
)

b3 = Train(
    id='b3',
    name='Bk I',
    length=11,
    liveries={
        'Red': Livery('1964_DK_B_2_(B_I)_1967.png'),
        '2CC': Livery('1964_DK_B_2_(B_I)_1967.png', mask='mc1964_DK_B_2_(B_I)_1967.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1973, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=48,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'kiosk car',
    }),
)

b4 = Train(
    id='b4',
    name='Bk I mod 1983',
    length=11,
    liveries={
        'Red and White': Livery('1964_DK_B_4_(Bk_I)_1983.png'),
        '2CC': Livery('1964_DK_B_4_(Bk_I)_1983.png', mask='mc1964_DK_B_4_(Bk_I)_1983.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1983, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=48,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': 'kiosk car',
    }),
)

b5 = Train(
    id='b5',
    name='B I mod 1974',
    length=11,
    liveries={
        'Red': Livery('1964_DK_B_2_(B_I)_1967.png'),
        '2CC': Livery('1964_DK_B_2_(B_I)_1967.png', mask='mc1964_DK_B_2_(B_I)_1967.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1974, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=60,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

a1 = Train(
    id='a1',
    name='A',
    length=11,
    liveries={
        'Brown and Yellow': Livery('1966_DK_A_1_1966.png'),
        '2CC': Livery('1966_DK_A_1_1966.png', mask='mc1966_DK_A_1_1966.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='b1',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1966, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=48,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': '1st class',
    }),
)

a2 = Train(
    id='a2',
    name='A',
    length=11,
    liveries={
        'Red and Yellow': Livery('1966_DK_A_2_1967.png'),
        '2CC': Livery('1966_DK_A_2_1967.png', mask='mc1966_DK_A_2_1967.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1967, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=48,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st class',
    }),
)

a3 = Train(
    id='a3',
    name='Ba',
    length=11,
    liveries={
        'Red': Livery('1966_DK_A_3_(Ba)_1991.png'),
        '2CC': Livery('1966_DK_A_3_(Ba)_1991.png', mask='mc1966_DK_A_3_(Ba)_1991.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='b2',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1991, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=48,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': '2nd class',
    }),
)

bn1 = Train(
    id='bn1',
    name='Bn',
    length=11,
    liveries={
        'Red': Livery('1971_DK_Bn_1_1971.png'),
        '2CC': Livery('1971_DK_Bn_1_1971.png', mask='mc1971_DK_Bn_1_1971.png'),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='bn1',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1971, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=80,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=15,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local trains, 2nd class',
        'Trivia': '''Also used in Stockholm commuter trains when SL didn't have enough rolling stock''',
    }),
)

# 891mm narrow gauge

ubp_i = Train(
    id='ubp_i',
    name='UBp',
    length=9,
    liveries={
        'Original': Livery('xxxx_SE_X10p_UBp_1_xxxx.png'),
    },
    engine_class=Train.EngineClass.ELECTRIC,
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
        'Use': 'Passenger',
        'Trivia': 'The middle part of the new emus were ordered to arive first so that they could be used earlier replacing the oldest rolling stock',
        'Builder': 'ABB railcar',
    }),
)

x10p = Train( 
    id='x10p',
    name='X10p',
    length=9,
    liveries={
        'Original': Livery('xxxx_SE_X10p_X10p_1_xxxx.png'),
        'Overhauled': Livery('xxxx_SE_X10p_X10p_2_xxxx.png', intro_year=2011),
        'Upptåget (fictional)': Livery('SE_X10p_X10p_3.png', intro_year=2011),
    },
    country='sweden',
    company='na',
    power_type='dc',
    purchase_sprite_towed_id='x10p_car2',
    engine_class=Train.EngineClass.ELECTRIC, 
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
        'Use': 'Passenger emu', 
        'Trivia': 'Technically modular but always used in sets of one railcar with an unpowered trailer and a driving trailer in tow.',
        'Builder': 'ABB railcar',
    }),
).add_articulated_part(
    id='x10p_car2',
    length=9,
    liveries={
        'Original': Livery('xxxx_SE_X10p_UBp_1_xxxx.png'),
        'Overhauled': Livery('xxxx_SE_X10p_UBp_2_xxxx.png'),
        'Upptåget (fictional)': Livery('SE_X10p_UBp_3.png'),
    },
    cargo_capacity=80,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='x10p_car3',
    length=9,
    liveries={
        'Original': Livery('xxxx_SE_X10p_UBxp_1_xxxx.png'),
        'Overhauled': Livery('xxxx_SE_X10p_UBxp_2_xxxx.png'),
        'Upptåget (fictional)': Livery('SE_X10p_UBxp_3.png'),
    },
    cargo_capacity=76,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

Co_i = Train(
    id='co_i',
    name='Co "Grindvagn"',
    length=8,
    liveries={
        'Original': Livery('1914_SE_Co_68-71_1_1914.png'),
    },
    engine_class=Train.EngineClass.STEAM,
    track_type=p_gauge,
    country='sweden',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='co_i',
    max_speed=Train.kmhish(75),
    power=0,
    introduction_date=date(1914, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=Train.ton(int(18)),
    tractive_effort_coefficient=79,
    running_cost_factor=222,
    cargo_capacity=72,
    cost_factor=24,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Longer distance passenger',
        'Trivia': 'Class was originally Co at SRJ later becoming Bop at SJ and finally Bp at SLJ',
        'Builder': 'ASEA',
    }),
)
'''
Tp = Train( 
    id='tp',
    name='Tp',
    length=5,
    liveries=make_liveries({
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
    liveries=make_liveries({
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
    liveries=make_liveries({
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
    grf.VariantGroup(
        'MZ I',
        mzi1,
        mzi2,
        mzi3,
    ),
    grf.VariantGroup(
        'MZ II',
        mzii1,
        mzii2,
        mzii3,
    ),
    grf.VariantGroup(
        'MZ III',
        mziii1,
        mziii2,
    ),
    mziv1,
    grf.VariantGroup(
        'ME II',
        meii1,
        meii2,
        meii3,
        meii4,
    ),
    #grf.VariantGroup(
    #    'Rc',
        #rc1,
        #rc2,
        #rc3,
        #rc4,
        #rc5,
        #rc6,
    #),
    grf.VariantGroup(
        'EA',
        ea1,
        ea2,
        ea3,
    ),
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
        b5,
    ),
    b3,
    b4,
    grf.VariantGroup(
        'A',
        a1,
        a2,
    ),
    a3,
    bn1,
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

grf.main(g, 'kst_scandi_train.grf')
