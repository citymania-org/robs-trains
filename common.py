import grf, lib

g = grf.NewGRF(
    grfid=b'KSTA',
    name='KST - Kitchen Sink Trains',
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

palette = lib.read_palette_file('compal.png')
colours = {
    
"MAGENTA" : palette[16: 24],
"PINK" : palette[24: 32],
"RED" : palette[32: 40],
"MAROON" : palette[40: 48],
"ORANGE" : palette[48: 56],
"BROWN" : palette[56: 64],
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
"COLBALT" : palette[168: 176],
"MAUVE" : palette[176: 184],
"LAVENDER" : palette[184: 192],
"PURPLE" : palette[192: 200],
"DPURPLE" : palette[200: 208],
"GREY1" : palette[232: 240],
"GREY2" : palette[240: 248],
"GREY3" : palette[248: 256],
"GREY4" : palette[256: 264],
"GREY5" : palette[264: 272],
"GREY6" : palette[272: 280],
"GREY7" : palette[280: 288],
"GREY8" : palette[288: 296],
"GREY9" : palette[296: 304],
"GREY10" : palette[304: 312],
"SEBROWN" : palette[344: 352],
"SCARLET" : palette[352: 360],
"SLBLUE" : palette[360: 368],
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
