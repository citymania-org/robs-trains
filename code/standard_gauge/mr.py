import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_mr_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(130),
    power=636,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=70,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

COMMON_mrred_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=636,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=70,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_1_dsb = Train(
    id='d_d_mr_1_dsb',
    **COMMON_mrred_PROPS,
    name='DSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb1',),
        overlay=('mrlight'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    purchase_sprite_towed_id='d_d_mrd_1_dsb',
    country='denmark',
    introduction_date=date(1978, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 5 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mrd_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb1',
        overlay='mrdlight',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_2_dsb = Train(
    id='d_d_mr_2_dsb',
    **COMMON_mr_PROPS,
    name='DSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb2',),
        overlay=('mrlight'),
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    purchase_sprite_towed_id='d_d_mrd_2_dsb',
    country='denmark',
    introduction_date=date(1994, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 5 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mrd_2_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb2',
        overlay='mrdlight',
        cc_replace=colours['GREY1'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_3_dsb = Train(
    id='d_d_mr_3_dsb',
    **COMMON_mr_PROPS,
    name='DSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb3',),
        overlay=('mrlight'),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["COLBALT"]
    ),
    purchase_sprite_towed_id='d_d_mrd_3_dsb',
    country='denmark',
    introduction_date=date(2004, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 5 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mrd_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb3',
        overlay='mrdlight',
        cc_replace=colours['GREY3'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_4_dsb = Train(
    id='d_d_mr_4_dsb',
    **COMMON_mr_PROPS,
    name='Arriva MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrarriva1',),
        overlay=('mrlight'),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["RED"]
    ),
    purchase_sprite_towed_id='d_d_mrd_4_dsb',
    country='denmark',
    introduction_date=date(2003, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 5 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mrd_4_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrdarriva1',
        overlay='mrdlight',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_5_dsb = Train(
    id='d_d_mr_5_dsb',
    **COMMON_mr_PROPS,
    name='Arriva MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrarriva2',),
        overlay=('mrlight'),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["CREAM"]
    ),
    purchase_sprite_towed_id='d_d_mrd_5_dsb',
    country='denmark',
    introduction_date=date(2005, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 5 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mrd_5_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrdarriva2',
        overlay='mrdlight',
        cc_replace=colours['TURQUOISE'],
        cc2_replace=colours['CREAM'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_6_dsb = Train(
    id='d_d_mr_6_dsb',
    **COMMON_mr_PROPS,
    name='DSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb4',),
        overlay=('mrlight'),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["COLBALT"]
    ),
    purchase_sprite_towed_id='d_d_mrd_6_dsb',
    country='denmark',
    introduction_date=date(2012, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 5 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mrd_6_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb4',
        overlay='mrdlight',
        cc_replace=colours['GREY3'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_7_dsb = Train(
    id='d_d_mr_7_dsb',
    **COMMON_mrred_PROPS,
    name='DSB MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdsb5',),
        overlay=('mrlight'),
        cc_replace=colours["RED"],
        cc2_replace=colours["RED"]
    ),
    purchase_sprite_towed_id='d_d_mrd_7_dsb',
    country='denmark',
    introduction_date=date(1986, 1, 1),
    cargo_capacity=52,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers with 1st class carriage, up to 5 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mrd_7_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddsb1',
        overlay='mrdlight',
        cc_replace=colours['RED'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=52,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_8_dsb = Train(
    id='d_d_mr_8_dsb',
    **COMMON_mr_PROPS,
    name='CRSA MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrcrsa1',),
        overlay=('mrlight'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["COLBALT"]
    ),
    purchase_sprite_towed_id='d_d_mrd_8_dsb',
    country='denmark',
    introduction_date=date(2019, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Trivia': '''Used to service & maintain Denmark's railways''',
    }),
).add_articulated_part(
    id='d_d_mrd_8_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrdcrsa1',
        overlay='mrdlight',
        cc_replace=colours['COLBALT'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mr_9_dsb = Train(
    id='d_d_mr_9_dsb',
    **COMMON_mr_PROPS,
    name='Scandia Ekspressen MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrse1',),
        overlay=('mrlight'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='d_d_mrd_9_dsb',
    country='denmark',
    introduction_date=date(2019, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Trivia': 'A static restaurant train that can be found in Randers, Denmark',
    }),
).add_articulated_part(
    id='d_d_mrd_9_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrdse1',
        overlay='mrdlight',
        cc_replace=colours['COLBALT'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

dl_d_mr_1_dlj = Train(
    id='dl_d_mr_1_dlj',
    **COMMON_mrred_PROPS,
    name='DLJ MR',
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading=('mr',),
        paint=('mrdlj1',),
        overlay=('mrlight'),
        cc_replace=colours["BLUE"],
        cc2_replace=colours["RED"]
    ),
    purchase_sprite_towed_id='dl_d_mrd_1_dlj',
    country='doggerland',
    introduction_date=date(1986, 1, 1),
    cargo_capacity=56,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 5 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='dl_d_mrd_1_dlj',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/mr.psd',
        shading='mrd',
        paint='mrddlj1',
        overlay='mrdlight',
        cc_replace=colours['BLUE'],
        cc2_replace=colours['RED'],
    ),
    cargo_capacity=56,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
