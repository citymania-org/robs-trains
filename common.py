import grf, lib

g = grf.NewGRF(
    grfid=b'KSTA',
    name='The International Train Set - TITS',
    description='Mostly European trains made by Rob, dP, Brickblock1 and Meja. Licence: GPL v2',
    url='https://github.com/citymania-org/robs-trains',
    id_map_file='id_map.json',
)

Train = g.bind(lib.Train)

g.add(grf.SetGlobalTrainDepotYOffset(2))

g.add(grf.SetGlobalTrainMiscFlag(grf.GlobalTrainMiscFlag.DEPOT_FULL_TRAIN_WIDTH))

# railtype table
(
    standard_gauge,
    standard_gauge_1500v,  # Stog and Saltsjöbanan
    standard_guage_3kv,
    standard_gauge_15kv,  # Sweden and Norway
    standard_gauge_25kv,  # Denmark
    standard_gauge_25kv_15kv,  # border crossing trains
    standard_gauge_3kv_1500v,
    standard_gauge_25kv_3kv,
    standard_gauge_25kv_1500v,
    standard_gauge_15kv_3kv,
    standard_gauge_15kv_1500v,
    standard_gauge_25kv_15kv_3kv,
    standard_gauge_25kv_15kv_1500v,
    standard_gauge_25kv_3kv_1500v,
    standard_gauge_15kv_3kv_1500v,
    standard_gauge_all_voltages,
    metro,  # Metro
    extra_narrow_gauge,  # Swedish 3 foot gauge
    extra_narrow_gauge_1500v,  # SRJ
    extra_narrow_gauge_15kv,  # NKlJ
) = g.set_railtype_table([
    ('SAAN', 'RAIL'),  # Standard gauge track
    ('SAAd', 'SAAD', 'SAAE', 'ELRL'),  # Standard gauge 1,5kv and stog dc
    ('SAAD', 'SAAE', 'ELRL'),  # Standard gauge 3kv dc
    ('SAAa', 'SAAA', 'SAAE', 'ELRL'),  # Standard gauge 15kv ac
    ('SAAA', 'SAAE', 'ELRL'),  # Standard gauge 25kv ac
    ('SAA$', 'NORD', 'SAAE', 'ELRL'),  # Standard gauge 15kv and 25kv ac (will show up on all most of the time)
    ('SAA=', 'SAAE', 'ELRL'),  # Standard gauge 1500v and 3kv dc (will show up on all most of the time)
    ('SAA)', 'SAAE', 'ELRL'),  # Standard gauge 25kv and 3kv dc (will show up on all most of the time)
    ('SAA(', 'SAAE', 'ELRL'),  # Standard gauge 25kv and 1500kv ac/dc (will show up on all most of the time)
    ('SAA]', 'SAAE', 'ELRL'),  # Standard gauge 15kv and 3kv ac/dc (will show up on all most of the time)
    ('SAA[', 'SAAE', 'ELRL'),  # Standard gauge 15kv and 1500v ac/dc (will show up on all most of the time)
    ("SAA'", 'SAAE', 'ELRL'),  # Standard gauge 25kv, 15kv and 3kv ac/dc (will show up on all most of the time)
    ('SAA^', 'SAAE', 'ELRL'),  # Standard gauge 25kv, 15kv and 1500v ac/dc (will show up on all most of the time)
    ('SAA_', 'SAAE', 'ELRL'),  # Standard gauge 25kv, 3kv and 1500v ac/dc (will show up on all most of the time)
    ('SAA,', 'SAAE', 'ELRL'),  # Standard gauge 15kv, 3kv adn 1500v ac/dc (will show up on all most of the time)
    ('SAA*', 'SAAE', 'ELRL'),  # Standard gauge all voltages ac/dc
    ('MTRO', 'SAA4', 'SAA3'),  # Standard gauge Metro (MTRO is first be because it is better definded as metro)
    ('nAAN', 'NAAN', 'NGRL'),  # Narrow gauge track
    ('nAAd', 'nAAD', 'nAAE', 'NAAd', 'NAAD', 'NAAE', 'ELNG'),  # Narrow gauge 1.5kv dc
    ('nAAa', 'nAAA', 'nAAE', 'NAAa', 'NAAA', 'NAAE', 'ELNG'),  # Narrow gauge 15kv ac
])

# Add SAAZ? for Oslo metro won't be purfect (could work with sets)

# cargo table

(ct_mail, ct_goods, ct_food, ct_parcels, ct_wood) = g.set_cargo_table(["MAIL", "GOOD", "FOOD", "PCL_", "WOOD"])

# badge table

badges = lib.BadgeHandler(g)

# try to keep the order used here for now https://newgrf-specs.tt-wiki.net/wiki/CargoTypes

def tmpl_train(func):
    return [
        func(  0, 8, 10, 44, xofs=-4,  yofs=-21),
        func( 20, 8, 42, 44, xofs=-24, yofs=-30),
        func( 70, 8, 69, 44, xofs=-34, yofs=-38),
        func(150, 8, 42, 44, xofs=-16, yofs=-30),
        func(200, 8, 10, 44, xofs=-4,  yofs=-21),
        func(220, 8, 42, 44, xofs=-24, yofs=-30),
        func(270, 8, 69, 44, xofs=-34, yofs=-38),
        func(350, 8, 42, 44, xofs=-16, yofs=-30),
    ]
    
def tmpl_train_r(func):
    return [
        func(200, 8, 10, 44, xofs=-4,  yofs=-23),
        func(220, 8, 42, 44, xofs=-22, yofs=-31),
        func(270, 8, 69, 44, xofs=-30, yofs=-38),
        func(350, 8, 42, 44, xofs=-14, yofs=-29),
        func(  0, 8, 10, 44, xofs=-4,  yofs=-19),
        func( 20, 8, 42, 44, xofs=-26, yofs=-29),
        func( 70, 8, 69, 44, xofs=-38, yofs=-38),
        func(150, 8, 42, 44, xofs=-18, yofs=-31),
    ]

Livery = lib.LiveryFactory(tmpl_train, tmpl_train_r)
paint_palette = lib.read_palette_file('compal.png')
PSDLivery = lambda *args, **kw: lib.PSDLivery(tmpl_train, tmpl_train_r, paint_palette, *args, **kw)

# Using sound files from RUKTS: https://github.com/StarRaid/Representitive-UK-Trainset
modern_diesel_sound = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/modern_diesel_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/modern_diesel_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/modern_diesel_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/horn_4.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.BREAKDOWN_TRAIN_SHIP,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/horn_4.wav'),
}

dsb_my_sound = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/my_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/my_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/my_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/my_whistle.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.BREAKDOWN_TRAIN_SHIP,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/my_whistle.wav'),
}

dsb_mz_sound = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/mz_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/mz_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/mz_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/mz_horn.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.BREAKDOWN_TRAIN_SHIP,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/mz_horn.wav'),
}

dsb_me_sound = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/mz_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/mz_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/mz_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/me_horn.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.BREAKDOWN_TRAIN_SHIP,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/me_horn.wav'),
}

dsb_stog4_sound = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/electric4_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/electric4_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/electric4_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/stog4_start.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.BREAKDOWN_TRAIN_SHIP,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/stog4_horn.wav'),
}

palette = lib.read_palette_file('compal.png')
colours = {
    
"MAGENTA" : palette[16: 24],
"PINK" : palette[24: 32],
"RED" : palette[32: 40], # DSB
"MAROON" : palette[40: 48], # old DSB
"ORANGE" : palette[48: 56],
"BROWN" : palette[56: 64], # wood
"REDBROWN" : palette[64: 72],
"YELLOWBROWN" : palette[72: 80],
"DCREAM" : palette[80: 88],
"CREAM" : palette[88: 96],
"YELLOW" : palette[96: 104],
"LIME" : palette[104: 112],
"GREEN" : palette[112: 120],
"DGREEN" : palette[120: 128],
"TURQUOISE" : palette[128: 136],
"DTURQUOISE" : palette[136: 144],
"SKY" : palette[144: 152],
"BLUE" : palette[152: 160],
"DBLUE" : palette[160: 168],
"COLBALT" : palette[168: 176], # rc7 late DSB Bn
"MAUVE" : palette[176: 184],
"LAVENDER" : palette[184: 192],
"PURPLE" : palette[192: 200],
"DPURPLE" : palette[200: 208],
"GREY1" : palette[232: 240], # white
"GREY2" : palette[240: 248],
"GREY3" : palette[248: 256],
"GREY4" : palette[256: 264],
"GREY5" : palette[264: 272],
"GREY6" : palette[272: 280],
"GREY7" : palette[280: 288],
"GREY8" : palette[288: 296],
"GREY9" : palette[296: 304],
"GREY10" : palette[304: 312], # black
"SEBROWN" : palette[344: 352], # SJ D, SJ F
"SCARLET" : palette[352: 360], # lolland
"SLBLUE" : palette[360: 368],
"APPLE" : palette[368: 376], # green cargo
"MECONIUM" : palette[376: 384], # meja green
"SBB" : palette[384: 392], # sbb green
}

def make_psd_cc_liveries(psd_file, *, shading=None, paint=None, overlay=None, r_overlay=None, cc_replace, cc2_replace):
    return {
        'Default': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            r_overlay=r_overlay,
            cc_replace=cc_replace,
            cc2_replace=cc2_replace,
        ),
        '2CC': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            r_overlay=r_overlay,
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            r_overlay=r_overlay,
            auto_cc=lib.CC_SWAPPED,
        ),
    }
