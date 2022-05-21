from datetime import date

import grf

import lib

g = grf.NewGRF(
    grfid=b'ROBT',
    name='Robs Trains',
    description='Robs Trains',
)
Train = g.bind(lib.Train)


def tmpl_vox_train(filename):
    png = grf.ImageFile('sprites/' + filename)
    sprite = lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=32)
    return [
        sprite(  0, 0, 10, 33, xofs=-3, yofs=-16),
        sprite( 18, 0, 24, 24, xofs=-15, yofs=-16),
        sprite( 50, 0, 35, 19, xofs=-10, yofs=-16),
        sprite( 93, 0, 24, 24, xofs=-10, yofs=-16),
        sprite(125, 0, 10, 32, xofs=-3, yofs=-16),
        sprite(143, 0, 24, 24, xofs=-15, yofs=-16),
        sprite(175, 0, 35, 19, xofs=-10, yofs=-16),
        sprite(218, 0, 24, 24, xofs=-10, yofs=-16),
    ]


def make_vox_liveries(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train(filename),
    } for name, filename in liveries.items()]


# Using sound files from RUKTS: https://github.com/StarRaid/Representitive-UK-Trainset
modern_diesel_sound = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/modern_diesel_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/modern_diesel_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/modern_diesel_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/horn_4.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.TRAIN_BREAKDOWN,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/horn_4.wav'),  # sounds are cached by filename so horn_4 will only be added once
}


Train(
    id=501,
    name='Leyland National',
    liveries=make_vox_liveries({
        'A': 'z1989_DSB_MF_IC3_MFA_1_32bpp.png',
        'B': 'z1989_DSB_MF_IC3_MFA_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    sound_effects=modern_diesel_sound,
    max_speed=Train.kmhishph(104),
    power=255,
    introduction_date=date(1972, 1, 1),
    weight=20,
    tractive_effort_coefficient=79,
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=24,
    refittable_cargo_types=1,
    additional_text=grf.fake_info_text({
        'Info': 'Leyland',
    }),
).add_articulated_part(
    id=502,
    liveries = make_vox_liveries({
        'A': 'z1989_DSB_MF_IC3_FF_1_32bpp.png',
        'B': 'z1989_DSB_MF_IC3_FF_2_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
).add_articulated_part(
    id=503,
    liveries = make_vox_liveries({
        'A': 'z1989_DSB_MF_IC3_MFB_1_32bpp.png',
        'B': 'z1989_DSB_MF_IC3_MFB_2_32bpp.png',
    }),
    cargo_capacity=90,
    default_cargo_type=0,
    refittable_cargo_types=1,
)

g.write('robs_trains.grf')
