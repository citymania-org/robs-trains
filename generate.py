import os
from datetime import date

import grf

import lib


PURCHASE_ICONS_DIR = 'purchase list'
DEBUG_DIR = 'debug'

os.makedirs(DEBUG_DIR, exist_ok=True)

PALETTE = lib.read_palette_file('pal.png')
BLACK1 = PALETTE[0: 4] + PALETTE[8: 12]
SILVER = PALETTE[11: 12] + PALETTE[4: 8] + PALETTE[12: 15]
WHITE1 = PALETTE[5: 8] + PALETTE[12: 17]
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
    ('nAAd', 'nAAD', 'nAAE', 'NAAd', 'NAAD', 'NAAE', 'ELNG'),  # Narrow gauge 1.5kv dc
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
paint_palette = lib.read_palette_file('compal.png')
PSDLivery = lambda *args, **kw: lib.PSDLivery(tmpl_train, paint_palette, *args, **kw)

# Using sound files from RUKTS: https://github.com/StarRaid/Representitive-UK-Trainset
modern_diesel_sound = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/modern_diesel_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/modern_diesel_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/modern_diesel_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/horn_4.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.BREAKDOWN_TRAIN_SHIP,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/horn_4.wav'),
}


def make_psd_cc_liveries(psd_file, *, shading, paint, overlay, cc_replace, cc2_replace):
    return {
        'Default': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            cc_replace=cc_replace,
            cc2_replace=cc2_replace,
        ),
        '2CC': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            auto_cc=lib.CC_SWAPPED,
        ),
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
'''
Train(
    id='alignment_narrow',
    name='alignment narrow',
    length=8,
    liveries={
        '': Livery('alignment_narrow_gauge_short.png')
    },
    country='sweden',
    company='na',
    power_type='multi',
    purchase_sprite_towed_id='s_e_X10p_2_sl_car2',
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

# steam locos

s_s_N_ii_1_sj = Train(
    id='s_s_N_ii_1_sj',
    name='SJ N II',
    length=5,
    liveries={
        'Default': Livery('1900_SE_N_II_1.png', cc_replace=BLACK1, cc2_replace=BLACK1),
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
        'Builder': 'Multible',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

# diesel locos

# frichs marcipanbrød

COMMON_frichs_467to475_PROPS = dict(
    length=6,
    misc_flags=Train.Flags.USE_2CC,
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=61,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_d_frichs_467_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_1',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_1_1952.png', cc_replace=RED, cc2_replace=RED),
        '2CC': Livery('1952_DK_Frichs_467_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_467_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_2',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_2_1958.png', cc_replace=RED, cc2_replace=RED),
        '2CC': Livery('1952_DK_Frichs_467_2_1958.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1958, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_467_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_3',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_3_1960.png', cc_replace=RED, cc2_replace=CREAM),
        '2CC': Livery('1952_DK_Frichs_467_3_1960.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_467_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_4',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_4_1981.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_467_4_1981.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1981, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_467_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_467_5',
    name='HFHJ Frichs 467',
    liveries={
        'Default': Livery('1952_DK_Frichs_467_5_1997.png', cc_replace=RED, cc2_replace=CREAM),
        '2CC': Livery('1952_DK_Frichs_467_5_1997.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_468_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_468_1',
    name='OHJ Frichs 468',
    liveries={
        'Default': Livery('1952_DK_Frichs_468_1_1952.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_468_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_468_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_468_2',
    name='OHJ Frichs 468',
    liveries={
        'Default': Livery('1952_DK_Frichs_468_2_1984.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_468_2_1984.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1984, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_468_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_468_3',
    name='OHJ Frichs 468',
    liveries={
        'Default': Livery('1952_DK_Frichs_468_3_2017.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_468_3_2017.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(2017, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_1',
    name='LJ Frichs 469/470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_1_1952.png', cc_replace=MAROON, cc2_replace=MAROON),
        '2CC': Livery('1952_DK_Frichs_469_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_2',
    name='LJ Frichs 469/470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_2_1960.png', cc_replace=MAROON, cc2_replace=MAROON),
        '2CC': Livery('1952_DK_Frichs_469_2_1960.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_3',
    name='LJ Frichs 469/470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_3_1974.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_469_3_1974.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1974, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_4',
    name='LJ Frichs 469/470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_4_1976.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_469_4_1976.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1976, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_8 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_8',
    name='SB Frichs 469',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_8_1992.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_469_8_1992.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1992, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_5',
    name='LJ Frichs 470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_5_1994.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_469_5_1994.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(1994, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_6 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_6',
    name='LJ Frichs 470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_6_2007.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_469_6_2007.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(2007, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_469_7 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_469_7',
    name='Contec Frichs 470',
    liveries={
        'Default': Livery('1952_DK_Frichs_469_7_2008.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_469_7_2008.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(90),
    power=750,
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_1',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_1_1952.png', cc_replace=MAROON, cc2_replace=DCREAM),
        '2CC': Livery('1952_DK_Frichs_471_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_2',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_2_1977.png', cc_replace=RED, cc2_replace=CREAM),
        '2CC': Livery('1952_DK_Frichs_471_2_1977.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_3',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_3_1988.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_471_3_1988.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(1988, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_4',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_4_1995.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_471_4_1995.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(1995, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_5',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_5_2000.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_471_5_2000.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(2000, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_471_6 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_471_6',
    name='HHJ Frichs 471',
    liveries={
        'Default': Livery('1952_DK_Frichs_471_6_2014.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_471_6_2014.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=500,
    introduction_date=date(2014, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_1',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_1_1952.png', cc_replace=MAROON, cc2_replace=MAROON),
        '2CC': Livery('1952_DK_Frichs_472_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_2',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_2_1968.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_472_2_1968.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(1968, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_3',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_3_1980.png', cc_replace=ORANGE, cc2_replace=CREAM),
        '2CC': Livery('1952_DK_Frichs_472_3_1980.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(1980, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_4',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_4_1997.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_472_4_1997.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(1997, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_472_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_472_5',
    name='VLTJ Frichs 472',
    liveries={
        'Default': Livery('1952_DK_Frichs_472_5_2009.png', cc_replace=MAROON, cc2_replace=MAROON),
        '2CC': Livery('1952_DK_Frichs_472_5_2009.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=700,
    introduction_date=date(2009, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_473_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_473_1',
    name='GDS Frichs 473',
    liveries={
        'Default': Livery('1952_DK_Frichs_473_1_1952.png', cc_replace=MAROON, cc2_replace=DCREAM),
        '2CC': Livery('1952_DK_Frichs_473_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_473_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_473_2',
    name='GDS Frichs 473',
    liveries={
        'Default': Livery('1952_DK_Frichs_473_2_1963.png', cc_replace=MAROON, cc2_replace=DCREAM),
        '2CC': Livery('1952_DK_Frichs_473_2_1963.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1963, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_473_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_473_3',
    name='GDS Frichs 473',
    liveries={
        'Default': Livery('1952_DK_Frichs_473_3_2006.png', cc_replace=MAROON, cc2_replace=DCREAM),
        '2CC': Livery('1952_DK_Frichs_473_3_2006.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(2006, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_1',
    name='FFJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_1_1952.png', cc_replace=MAROON, cc2_replace=BLACK1),
        '2CC': Livery('1952_DK_Frichs_474_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_2',
    name='OHJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_2_1969.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_474_2_1969.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1969, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_3',
    name='OHJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_3_1986.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_474_3_1986.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1986, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_4',
    name='OHJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_4_1990.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_474_4_1990.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1990, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_474_5 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_474_5',
    name='OHJ Frichs 474',
    liveries={
        'Default': Livery('1952_DK_Frichs_474_5_1993.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_474_5_1993.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1993, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_475_1 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_475_1',
    name='AHJ Frichs 475',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_1_1952.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('1952_DK_Frichs_475_1_1952.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1952, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_475_2 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_475_2',
    name='SB Frichs 475',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_2_1976.png', cc_replace=MAROON, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_475_2_1976.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1976, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_475_3 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_475_3',
    name='SB Frichs 475',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_3_1977.png', cc_replace=RED, cc2_replace=WHITE1),
        '2CC': Livery('1952_DK_Frichs_475_3_1977.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(1977, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

d_d_frichs_475_4 = Train(
    **COMMON_frichs_467to475_PROPS,
    id='d_d_frichs_475_4',
    name='AHJ Frichs 475',
    liveries={
        'Default': Livery('1952_DK_Frichs_475_4_2008.png', cc_replace=MAROON, cc2_replace=BLACK1),
        '2CC': Livery('1952_DK_Frichs_475_4_2008.png', auto_cc=lib.CC_DEFAULT),
    },
    country='denmark',
    company='na',
    max_speed=Train.kmhish(75),
    power=750,
    introduction_date=date(2008, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
    }),
)

# nohab

d_d_mye_ii_1_dsb = Train(
    id='d_d_mye_ii_1_dsb',
    name='DSB MY II (early)',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsbmy1',),
        overlay=('light'),
        cc_replace=MAROON,
        cc2_replace=DCREAM
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(133),
    power=1700,
    introduction_date=date(1954, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=102,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''Denmark's first mass-produced modern diesel locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

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
)

d_d_mx_ii_1_dsb = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_1_dsb',
    name='DSB MX II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('mx',),
        paint=('dsbmx1',),
        overlay=('light'),
        cc_replace=MAROON,
        cc2_replace=DCREAM
    ),
    country='denmark',
    company='na',
    introduction_date=date(1960, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''designed to be used on branch lines where a lighter locomotive is needed''',
    }),
)

d_d_mx_ii_2_dsb = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_2_dsb',
    name='DSB MX II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('mx',),
        paint=('dsbmx2',),
        overlay=('light'),
        cc_replace=RED,
        cc2_replace=BLACK1
    ),
    country='denmark',
    company='na',
    introduction_date=date(1972, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''designed to be used on branch lines where a lighter locomotive is needed''',
    }),
)

d_d_mx_ii_3_vltj = Train(
    **COMMON_mx_ii_PROPS,
    id='d_d_mx_ii_3_vltj',
    name='VLTJ MX II',
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('mx',),
        paint=('vltjmx1',),
        overlay=('light'),
        cc_replace=ORANGE,
        cc2_replace=RED
    ),
    country='denmark',
    company='na',
    introduction_date=date(1993, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''designed to be used on branch lines where a lighter locomotive is needed''',
    }),
)

d_d_my_ii_1_dsb = Train(
    id='d_d_my_ii_1_dsb',
    name='DSB MY II',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsbmy1',),
        overlay=('light'),
        cc_replace=MAROON,
        cc2_replace=DCREAM
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(133),
    power=1950,
    introduction_date=date(1964, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=102,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''a more powerful version of the famous MY locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_d_my_ii_2_dsb = Train(
    id='d_d_my_ii_2_dsb',
    name='DSB MY II',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/my.psd',
        shading=('my',),
        paint=('dsbmy2',),
        overlay=('light'),
        cc_replace=RED,
        cc2_replace=BLACK1
    ),
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(133),
    power=1950,
    introduction_date=date(1972, 1, 1),
    vehicle_life=30,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=102,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=1,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Universal',
        'Trivia': '''a more powerful version of the famous MY locomotive''',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

# toaster

d_d_mz_i_1_dsb = Train(
    id='d_d_mz_i_1_dsb',
    name='DSB MZ I',
    length=10,
    liveries={
        'Default': Livery('1967_DK_MZ_I_1_1967.png', cc_replace=MAROON, cc2_replace=DCREAM),
        '2CC': Livery('1967_DK_MZ_I_1_1967.png', auto_cc=lib.CC_DEFAULT),
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

d_d_mz_i_2_dsb = Train(
    id='d_d_mz_i_2_dsb',
    name='DSB MZ I',
    length=10,
    liveries={
        'Default': Livery('1967_DK_MZ_I_2_1972.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('1967_DK_MZ_I_2_1972.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1967_DK_MZ_I_2_1972.png', auto_cc=lib.CC_SWAPPED),
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

d_d_mz_i_3_dsb = Train(
    id='d_d_mz_i_3_dsb',
    name='DSB MZ I',
    length=10,
    liveries={
        'Default': Livery('1967_DK_MZ_I_3_1986.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('1967_DK_MZ_I_3_1986.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1967_DK_MZ_I_3_1986.png', auto_cc=lib.CC_SWAPPED),
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

d_d_mz_ii_1_dsb = Train(
    id='d_d_mz_ii_1_dsb',
    name='DSB MZ II',
    length=10,
    liveries={
        'Default': Livery('1967_DK_MZ_I_1_1967.png', cc_replace=MAROON, cc2_replace=DCREAM),
        '2CC': Livery('1967_DK_MZ_I_1_1967.png', auto_cc=lib.CC_DEFAULT),
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

d_d_mz_ii_2_dsb = Train(
    id='d_d_mz_ii_2_dsb',
    name='DSB MZ II',
    length=10,
    liveries={
        'Default': Livery('1967_DK_MZ_I_2_1972.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('1967_DK_MZ_I_2_1972.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1967_DK_MZ_I_2_1972.png', auto_cc=lib.CC_SWAPPED),
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

d_d_mz_ii_3_dsb = Train(
    id='d_d_mz_ii_3_dsb',
    name='DSB MZ II',
    length=10,
    liveries={
        'Default': Livery('1967_DK_MZ_I_3_1986.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('1967_DK_MZ_I_3_1986.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1967_DK_MZ_I_3_1986.png', auto_cc=lib.CC_SWAPPED),
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

d_d_mz_ii_4_taagab = Train(
    id='d_d_mz_ii_4_taagab',
    name='TÅGAB TMZ II',
    length=10,
    liveries={
        'Default': Livery('1970_DK_MZ_II_1_2004.png', cc_replace=SILVER, cc2_replace=RED),
        '2CC': Livery('1970_DK_MZ_II_1_2004.png', auto_cc=lib.CC_DEFAULT),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='taagab',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(143),
    power=3300,
    introduction_date=date(2004, 1, 1),
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
        'Trivia': 'Two locomotives bought from DSB in 2004 and 2006',
    }),
    callbacks={'properties': {'cargo_capacity': 0},},
)

d_d_mz_iii_1_dsb = Train(
    id='d_d_mz_iii_1_dsb',
    name='DSB MZ III',
    length=10,
    liveries={
        'Default': Livery('1972_DK_MZ_III_1_1972.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('1972_DK_MZ_III_1_1972.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1972_DK_MZ_III_1_1972.png', auto_cc=lib.CC_SWAPPED),
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

d_d_mz_iii_2_dsb = Train(
    id='d_d_mz_iii_2_dsb',
    name='DSB MZ III',
    length=10,
    liveries={
        'Default': Livery('1972_DK_MZ_III_2_1986.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('1972_DK_MZ_III_2_1986.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1972_DK_MZ_III_2_1986.png', auto_cc=lib.CC_SWAPPED),
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

d_d_mz_iv_1_dsb = Train(
    id='d_d_mz_iv_1_dsb',
    name='DSB MZ IV',
    length=10,
    liveries={
        'Default': Livery('1977_DK_MZ_IV_1_1977.png', cc_replace=RED, cc2_replace=BLACK1),
        '2CC': Livery('1977_DK_MZ_IV_1_1977.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1977_DK_MZ_IV_1_1977.png', auto_cc=lib.CC_SWAPPED),
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

d_d_me_ii_1_dsb = Train(
    id='d_d_me_ii_1_dsb',
    name='DSB ME II',
    length=10,
    liveries={
        'Default': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb1',),
            overlay=('light'),
            cc_replace=RED,
            cc2_replace=BLACK1
        ),
        '2CC': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb1',),
            overlay=('light'),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb1',),
            overlay=('light'),
            auto_cc=lib.CC_SWAPPED,
        ),
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

d_d_me_ii_2_dsb = Train(
    id='d_d_me_ii_2_dsb',
    name='DSB ME II',
    length=10,
    liveries={
        'Default': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb2/3',),
            overlay=('light'),
            cc_replace=RED,
            cc2_replace=COLBALT
        ),
        '2CC': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb2/3',),
            overlay=('light'),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb2/3',),
            overlay=('light'),
            auto_cc=lib.CC_SWAPPED,
        ),
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

d_d_me_ii_3_dsb = Train(
    id='d_d_me_ii_3_dsb',
    name='DSB ME II',
    length=10,
    liveries={
        'Default': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb2/3',),
            overlay=('light'),
            cc_replace=COLBALT,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb2/3',),
            overlay=('light'),
            auto_cc=lib.CC_SWAPPED,
        ),
        '2CC alt': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb2/3',),
            overlay=('light'),
            auto_cc=lib.CC_DEFAULT,
        ),
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

d_d_me_ii_4_dsb = Train(
    id='d_d_me_ii_4_dsb',
    name='DSB ME II',
    length=10,
    liveries={
        'Default': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb4',),
            overlay=('light'),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb4',),
            overlay=('light'),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/me.psd',
            shading=('me',),
            paint=('dsb4',),
            overlay=('light'),
            auto_cc=lib.CC_SWAPPED,
        ),
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

# electric locos leccy
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

d_e_ea_1_dsb = Train(
    id='d_e_ea_1_dsb',
    name='DSB EA',
    length=9,
    liveries=make_psd_cc_liveries(
        'pp/ea.psd',
        shading=('ea',),
        paint=('dsb1',),
        overlay=('light'),
        cc_replace=RED,
        cc2_replace=BLACK1
    ),
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

d_e_ea_2_dsb = Train(
    id='d_e_ea_2_dsb',
    name='DSB EA',
    length=9,
    liveries={
        'Default': PSDLivery(
            'pp/ea.psd',
            shading=('ea',),
            paint=('dsb2',),
            overlay=('light'),
            cc_replace=RED,
            cc2_replace=COLBALT
        ),
        '2CC': PSDLivery(
            'pp/ea.psd',
            shading=('ea',),
            paint=('dsb2',),
            overlay=('light'),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ea.psd',
            shading=('ea',),
            paint=('dsb2',),
            overlay=('light'),
            auto_cc=lib.CC_SWAPPED,
        ),
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

d_e_ea_3_dsb = Train(
    id='d_e_ea_3_dsb',
    name='DSB EA',
    length=9,
    liveries={
        'Default': PSDLivery(
            'pp/ea.psd',
            shading=('ea',),
            paint=('dsb3',),
            overlay=('light'),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ea.psd',
            shading=('ea',),
            paint=('dsb3',),
            overlay=('light'),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ea.psd',
            shading=('ea',),
            paint=('dsb3',),
            overlay=('light'),
            auto_cc=lib.CC_SWAPPED,
        ),
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

# carriages

# dsb b

d_p_b_1_dsb = Train(
    id='d_p_b_1_dsb',
    name='DSB B',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b1_bd1_bn1',),
            cc_replace=MAROON,
            cc2_replace=MAROON
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b1_bd1_bn1',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b1_bd1_bn1',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_1_dsb',
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

d_p_b_i_1_dsb = Train(
    id='d_p_b_i_1_dsb',
    name='DSB B I',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_i_1_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
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

d_p_bk_i_1_dsb = Train(
    id='d_p_bk_i_1_dsb',
    name='DSB Bk I',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_i_1_dsb',
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

d_p_bk_i_2_dsb = Train(
    id='d_p_bk_i_2_dsb',
    name='DSB Bk I',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('bk2',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('bk2',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('b',),
            paint=('bk2',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_i_1_dsb',
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

d_p_ab_1_dsb = Train(
    id='d_p_ab_1_dsb',
    name='DSB AB',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('ab1',),
            cc_replace=MAROON,
            cc2_replace=MAROON
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('ab1',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('ab1',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_ab_1_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1969, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=64,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st and 2nd class',
    }),
)

d_p_ab_2_dsb = Train(
    id='d_p_ab_2_dsb',
    name='DSB AB',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('ab2',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('ab2',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('ab2',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_ab_2_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=64,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st and 2nd class',
    }),
)

d_p_ab_3_dsb = Train(
    id='d_p_ab_3_dsb',
    name='DSB Bab',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('ab',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_ab_3_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1991, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=54,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

d_p_a_1_dsb = Train(
    id='d_p_a_1_dsb',
    name='DSB A',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('a1',),
            cc_replace=MAROON,
            cc2_replace=MAROON
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('a1',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('a1',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_1_dsb',
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

d_p_a_2_dsb = Train(
    id='d_p_a_2_dsb',
    name='DSB A',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('a2_an1',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('a2_an1',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('a2_an1',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_i_1_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
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

d_p_a_3_dsb = Train(
    id='d_p_a_3_dsb',
    name='DSB Ba',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('a',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_a_3_dsb',
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

d_p_bd_1_dsb = Train(
    id='d_p_bd_1_dsb',
    name='DSB BD',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('bd',),
            paint=('b1_bd1_bn1',),
            cc_replace=MAROON,
            cc2_replace=MAROON
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('bd',),
            paint=('b1_bd1_bn1',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('bd',),
            paint=('b1_bd1_bn1',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_bd_1_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1968, 1, 1),
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
    'Use': 'luggage carriage',
    }),
)

d_p_bd_2_dsb = Train(
    id='d_p_bd_2_dsb',
    name='DSB BD',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('bd',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('bd',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('bd',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_bd_2_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=37,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=36,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=10,
    additional_text=grf.fake_vehicle_info({
    'Use': 'luggage carriage',
    }),
)

d_p_bn_1_dsb = Train(
    id='d_p_bn_1_dsb',
    name='DSB Bn',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('b1_bd1_bn1',),
            cc_replace=MAROON,
            cc2_replace=MAROON
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('b1_bd1_bn1',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('b1_bd1_bn1',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_bn_1_dsb',
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
        'Use': 'local trains, 2nd class',
        'Trivia': '''also used in Stockholm commuter trains when SL didn't have enough rolling stock''',
    }),
)

d_p_bn_2_dsb = Train(
    id='d_p_bn_2_dsb',
    name='DSB Bn',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('b2_ba1_bab1_bd2_bk1_bn2',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_bn_2_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
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
        'Use': 'local trains, 2nd class',
        'Trivia': '''also used in Stockholm commuter trains when SL didn't have enough rolling stock''',
    }),
)

d_p_bn_3_dsb = Train(
    id='d_p_bn_3_dsb',
    name='DSB Bn',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('bn3',),
            cc_replace=COLBALT,
            cc2_replace=COLBALT
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('bn3',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('bn',),
            paint=('bn3',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_bn_3_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(2006, 1, 1),
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
        'Use': 'local trains, 2nd class',
        'Trivia': '''also used in Stockholm commuter trains when SL didn't have enough rolling stock''',
    }),
)

d_p_an_1_dsb = Train(
    id='d_p_an_1_dsb',
    name='DSB An',
    length=11,
    liveries={
        'Default': PSDLivery(
            'pp/ab.psd',
            shading=('an',),
            paint=('a2_an1',),
            cc_replace=RED,
            cc2_replace=RED
        ),
        '2CC': PSDLivery(
            'pp/ab.psd',
            shading=('an',),
            paint=('a2_an1',),
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            'pp/ab.psd',
            shading=('an',),
            paint=('a2_an1',),
            auto_cc=lib.CC_SWAPPED,
        ),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_an_1_dsb',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(160),
    power=0,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    weight=40,
    tractive_effort_coefficient=79,
    running_cost_factor=200,
    cargo_capacity=64,
    cost_factor=200,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    loading_speed=15,
    additional_text=grf.fake_vehicle_info({
        'Use': 'local trains, 1st class',
    }),
)

# dsb double decker dd

d_p_b_ii_1_dsb = Train(
    id='d_p_b_ii_1_dsb',
    name='DSB B II',
    length=12,
    liveries={
        'Default': Livery('2002_DK_B_II_1_2002.png', cc_replace=COLBALT, cc2_replace=WHITE1),
        '2CC': Livery('2002_DK_B_II_1_2002.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('2002_DK_B_II_1_2002.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_ii_1_dsb',
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
        'Default': Livery('2002_DK_B_II_2_2012.png', cc_replace=COLBALT, cc2_replace=WHITE1),
        '2CC': Livery('2002_DK_B_II_2_2012.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('2002_DK_B_II_2_2012.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_ii_2_dsb',
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
        'Default': Livery('2002_DK_Bk_III_1_2002.png', cc_replace=COLBALT, cc2_replace=WHITE1),
        '2CC': Livery('2002_DK_Bk_III_1_2002.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('2002_DK_Bk_III_1_2002.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_ii_1_dsb',
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
        'Default': Livery('2002_DK_Bk_III_2_2012.png', cc_replace=COLBALT, cc2_replace=WHITE1),
        '2CC': Livery('2002_DK_Bk_III_2_2012.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('2002_DK_Bk_III_2_2012.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='denmark',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='d_p_b_ii_2_dsb',
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
    purchase_sprite_towed_id='s_w_Gblssy_2_gc',
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

s_w_Gblssy_2_gc = Train(
    id='s_w_Hbis_sj',
    name='SJ Hbis',
    length=7,
    liveries={
        'Default': Livery('1972_SE_Hbis_1972.png', cc_replace=REDBROWN, cc2_replace=REDBROWN),
        '2CC': Livery('1972_SE_Hbis_1972.png', auto_cc=lib.CC_DEFAULT),
        '2CC alt': Livery('1972_SE_Hbis_1972.png', auto_cc=lib.CC_SWAPPED),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='s_w_Hbis_sj',
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

s_p_UBp_ii_1 = Train(
    id='s_p_UBp_ii_1',
    name='SL UBp II',
    length=9,
    liveries={
        'SL': Livery('xxxx_SE_X10p_UBp_1_xxxx.png'),
    },
    engine_class=Train.EngineClass.ELECTRIC,
    track_type=p_gauge,
    country='sweden',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='s_p_UBp_ii_1',
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

COMMON_X10p_PROPS = dict(
    length=9,
    country='sweden',
    company='na',
    power_type='dc',
    engine_class=Train.EngineClass.ELECTRIC, 
    track_type=p_gauge_dc,
    max_speed=Train.kmhish(80),
    power=536,
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
)

s_e_X10p_1_sl = Train(
    **COMMON_X10p_PROPS, 
    id='s_e_X10p_1_sl,',
    name='SL X10p',
    liveries={
        'Default': Livery('xxxx_SE_X10p_X10p_1_xxxx.png'),
    },
    purchase_sprite_towed_id='s_e_X10p_1_sl_car2',
    introduction_date=date(1990, 1, 1),
).add_articulated_part(
    id='s_e_X10p_1_sl_car2',
    length=9,
    liveries={
        'Default': Livery('xxxx_SE_X10p_UBp_1_xxxx.png'),
    },
    cargo_capacity=80,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='s_e_X10p_1_sl_car3',
    length=9,
    liveries={
        'Default': Livery('xxxx_SE_X10p_UBxp_1_xxxx.png'),
    },
    cargo_capacity=76,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_e_X10p_2_sl = Train(
    **COMMON_X10p_PROPS, 
    id='s_e_X10p_2_sl,',
    name='SL X10p mod 2011',
    liveries={
        'Default': Livery('xxxx_SE_X10p_X10p_2_xxxx.png'),
        '2CC': Livery('xxxx_SE_X10p_X10p_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
        'Upptåget (Fictional)': Livery('SE_X10p_X10p_3.png'),
        'Upptåget 2CC': Livery('SE_X10p_X10p_3.png', auto_cc=lib.CC_DEFAULT),
    },
    purchase_sprite_towed_id='s_e_X10p_2_sl_car2',
    introduction_date=date(2011, 1, 1),
).add_articulated_part(
    id='s_e_X10p_2_sl_car2',
    length=9,
    liveries={
        'Default': Livery('xxxx_SE_X10p_UBp_2_xxxx.png'),
        '2CC': Livery('xxxx_SE_X10p_UBp_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
        'Upptåget (Fictional)': Livery('SE_X10p_UBp_3.png'),
        'Upptåget 2CC': Livery('SE_X10p_UBp_3.png', auto_cc=lib.CC_DEFAULT),
    },
    cargo_capacity=80,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
).add_articulated_part(
    id='s_e_X10p_2_sl_car3',
    length=9,
    liveries={
        'Default': Livery('xxxx_SE_X10p_UBxp_2_xxxx.png'),
        '2CC': Livery('xxxx_SE_X10p_UBxp_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
        'Upptåget (Fictional)': Livery('SE_X10p_UBxp_3.png'),
        'Upptåget 2CC': Livery('SE_X10p_UBxp_3.png', auto_cc=lib.CC_DEFAULT),
    },
    cargo_capacity=76,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

s_p_Co_1 = Train(
    id='s_p_Co_1',
    name='SRJ Co "Grindvagn"',
    length=8,
    liveries={
        'Default': Livery('1914_SE_Co_68-71_1_1914.png'),
    },
    engine_class=Train.EngineClass.STEAM,
    track_type=p_gauge,
    country='sweden',
    company='na',
    power_type='na',
    purchase_sprite_towed_id='s_p_Co_1',
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

s_d_Tp_1_sj = Train( 
    id='s_d_Tp_1_sj',
    name='SJ Tp',
    length=5,
    liveries={
        'Default': Livery('SE_Tp_1.png'),
    },
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='s_d_Tp_1_sj',
    engine_class=Train.EngineClass.DIESEL,
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
        'Use': 'Universal',
        'Trivia': "SJ's larger narrow gauge loco",
        'Builder': 'Maschinenbau GmbH and ASJ Falun',
    }),
    callbacks={'properties': {'cargo_capacity': 0},}
)

s_d_Z4p_1_srj = Train(
    id='s_d_Z4p_1_srj',
    name='SRJ Z4p',
    length=3,
    liveries={
        'Default': Livery('1947_SE_Z4p_1_1947.png', cc_replace=REDBROWN),
        '2CC': Livery('1947_SE_Z4p_1_1947.png', auto_cc=lib.CC_DEFAULT),
    #    'SL Grey and yellow': '1947_SE_Z4p_4_xxxx.png',
    #    'SL Red': '1947_SE_Z4p_5_xxxx.png',
    },
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='s_p_Co_1',
    engine_class=Train.EngineClass.DIESEL, 
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

s_d_Z4p_2_nklj = Train(
    id='s_d_Z4p_2_NKLJ',
    name='NKlJ Z4p',
    length=3,
    liveries={
        'Default': Livery('1947_SE_Z4p_2_xxxx.png', cc_replace=MAROON, cc2_replace=CREAM),
        '2CC': Livery('1947_SE_Z4p_2_xxxx.png', auto_cc=lib.CC_DEFAULT),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='s_p_Co_1',
    engine_class=Train.EngineClass.DIESEL, 
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


s_d_Z4p_3_donj = Train(
    id='s_d_Z4p_3_DONJ',
    name='DONJ Z4p',
    length=3,
    liveries={
        'Default': Livery('1947_SE_Z4p_3_xxxx.png', cc_replace=ORANGE, cc2_replace=DTURQUOISE),
        '2CC': Livery('1947_SE_Z4p_3_xxxx.png', auto_cc=lib.CC_DEFAULT),
    },
    misc_flags=Train.Flags.USE_2CC,
    country='sweden',
    company='na',
    power_type='diesel',
    purchase_sprite_towed_id='s_p_Co_1',
    engine_class=Train.EngineClass.DIESEL, 
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

'''

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
    'sl': purchase_icon('lsl.png'),
    'taagab': purchase_icon('ltågab.png'),
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
    grf.VariantGroup(
        'Frichs 467-475 "Marcipanbrød"',
        d_d_frichs_467_1,
        d_d_frichs_467_2,
        d_d_frichs_467_3,
        d_d_frichs_467_4,
        d_d_frichs_467_5,
        d_d_frichs_468_1,
        d_d_frichs_468_2,
        d_d_frichs_468_3,
        d_d_frichs_469_1,
        d_d_frichs_469_2,
        d_d_frichs_469_3,
        d_d_frichs_469_4,
        d_d_frichs_469_8,
        d_d_frichs_469_5,
        d_d_frichs_469_6,
        d_d_frichs_469_7,
        d_d_frichs_471_1,
        d_d_frichs_471_2,
        d_d_frichs_471_3,
        d_d_frichs_471_4,
        d_d_frichs_471_5,
        d_d_frichs_471_6,
        d_d_frichs_472_1,
        d_d_frichs_472_2,
        d_d_frichs_472_3,
        d_d_frichs_472_4,
        d_d_frichs_472_5,
        d_d_frichs_473_1,
        d_d_frichs_473_2,
        d_d_frichs_473_3,
        d_d_frichs_474_1,
        d_d_frichs_474_2,
        d_d_frichs_474_3,
        d_d_frichs_474_4,
        d_d_frichs_474_5,
        d_d_frichs_475_1,
        d_d_frichs_475_2,
        d_d_frichs_475_3,
        d_d_frichs_475_4,
    ),
    d_d_mye_ii_1_dsb,
    grf.VariantGroup(
        'MX II',
        d_d_mx_ii_1_dsb,
        d_d_mx_ii_2_dsb,
        d_d_mx_ii_3_vltj,
    ),
    grf.VariantGroup(
        'MY II',
        d_d_my_ii_1_dsb,
        d_d_my_ii_2_dsb,
    ),
    grf.VariantGroup(
        'MZ I',
        d_d_mz_i_1_dsb,
        d_d_mz_i_2_dsb,
        d_d_mz_i_3_dsb,
    ),
    grf.VariantGroup(
        'MZ II',
        d_d_mz_ii_1_dsb,
        d_d_mz_ii_2_dsb,
        d_d_mz_ii_3_dsb,
        d_d_mz_ii_4_taagab,
    ),
    grf.VariantGroup(
        'MZ III',
        d_d_mz_iii_1_dsb,
        d_d_mz_iii_2_dsb,
    ),
    d_d_mz_iv_1_dsb,
    grf.VariantGroup(
        'ME II',
        d_d_me_ii_1_dsb,
        d_d_me_ii_2_dsb,
        d_d_me_ii_3_dsb,
        d_d_me_ii_4_dsb,
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
        d_e_ea_1_dsb,
        d_e_ea_2_dsb,
        d_e_ea_3_dsb,
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
        'A',
        d_p_a_1_dsb,
        d_p_a_2_dsb,
        d_p_a_3_dsb,
    ),
    grf.VariantGroup(
        'AB',
        d_p_ab_1_dsb,
        d_p_ab_2_dsb,
        d_p_ab_3_dsb,
    ),
    grf.VariantGroup(
        'B',
        d_p_b_1_dsb,
        d_p_b_i_1_dsb,
    ),
    grf.VariantGroup(
        'Bk I',
        d_p_bk_i_1_dsb,
        d_p_bk_i_2_dsb,
    ),
    grf.VariantGroup(
        'BD',
        d_p_bd_1_dsb,
        d_p_bd_2_dsb,
    ),
    d_p_an_1_dsb,
    grf.VariantGroup(
        'Bn',
        d_p_bn_1_dsb,
        d_p_bn_2_dsb,
        d_p_bn_3_dsb,
    ),
    grf.VariantGroup(
        'B II',
        d_p_b_ii_1_dsb,
        d_p_bk_iii_1_dsb,
        d_p_b_ii_2_dsb,
        d_p_bk_iii_2_dsb,
    ),
    #grf.VariantGroup(
    #    'B II',
    #    b_ii1,
    #    b_ii2,
    #),
    grf.VariantGroup(
        'Z4p',
        s_d_Z4p_1_srj,
        s_d_Z4p_2_nklj,
        s_d_Z4p_3_donj, 
    ),
    s_d_Tp_1_sj,
    s_p_Co_1,
    s_p_UBp_ii_1,
    grf.VariantGroup(
        'X10p',
        s_e_X10p_1_sl,
        s_e_X10p_2_sl,
    ),
).set_variant_callbacks(g)))

grf.main(g, 'kst_scandi_train.grf')
