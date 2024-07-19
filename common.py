import grf, lib

g = grf.NewGRF(
    grfid=b'KSTA',
    name='KST SNDTS (ScaNDinavian Train Set)',
    description='Scandinavian Trains made by Rob, dP and Brickblock1. Licence: GPL v2',
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
    p_gauge_15kv,  # NKlJ
) = g.set_railtype_table([
    ('SAAN', 'RAIL'),  # Standard gauge track
    ('SAA$', 'NORD', 'SAAE', 'ELRL'),  # Standard gauge 15kv and 25kv ac (will show up on dc most of the time)
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

palette = lib.read_palette_file('pal.png')
colours = {
"BLACK1" : palette[0: 4] + palette[8: 12],
"SILVER" : palette[11: 12] + palette[4: 8] + palette[12: 15],
"WHITE1" : palette[5: 8] + palette[12: 17],
"MAGENTA" : palette[44: 52],
"PINK" : palette[52: 60],
"RED" : palette[60: 68],
"MAROON" : palette[68: 76],
"ORANGE" : palette[76: 84],
"BROWN" : palette[84: 92],
"REDBROWN" : palette[92: 100],
"YELLOWBROWN" : palette[100: 108],
"DCREAM" : palette[108: 116],
"CREAM" : palette[116: 124],
"YELLOW" : palette[124: 132],
"LIME" : palette[132: 140],
"GREEN" : palette[140: 148],
"DGREEN" : palette[148: 156],
"TURQUOISE" : palette[156: 164],
"DTURQUOISE" : palette[164: 172],
"SKY" : palette[172: 180],
"BLUE" : palette[180: 188],
"DBLUE" : palette[188: 196],
"COLBALT" : palette[196: 204],
"MAUVE" : palette[204: 212],
"LAVENDER" : palette[212: 220],
"PURPLE" : palette[220: 228],
"DPURPLE" : palette[228: 236],
}

def make_psd_cc_liveries(psd_file, *, shading=None, paint=None, overlay=None, cc_replace, cc2_replace):
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