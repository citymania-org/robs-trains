from datetime import date

import grf

import lib

g = grf.NewGRF(
    b'ROBT',
    8,
    'Robs Trains',
    'Robs Trains',
)
g.strings = lib.StringManager()
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
        sprite(175, 0, 27, 19, xofs=-10, yofs=-16),
        sprite(218, 0, 24, 24, xofs=-10, yofs=-16),
    ]


def make_vox_liveries(liveries):
    return [{
        'name': f' ({name})',
        'sprites': tmpl_vox_train(filename),
    } for name, filename in liveries.items()]


Train(
    id=501,
    name='Leyland National',
    liveries=make_vox_liveries({
        'A': 'z1989_DSB_MF_IC3_MFA_1_32bpp.png',
        'B': 'z1989_DSB_MF_IC3_MFA_2_32bpp.png',
    }),
    engine_class=Train.EngineClass.DIESEL,
    max_speed=lib.kmhishph(104),
    power=255,
    introduction_date=date(1972, 1, 1),
    vehicle_life=8,
    model_life=144,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=222,
    cargo_capacity=90,
    default_cargo_type=0,
    cost_factor=246,
    refittable_cargo_types=1,
    additional_text=lib.fake_info_text({
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

g.add(g.strings)
g.write('robs_trains.grf')
