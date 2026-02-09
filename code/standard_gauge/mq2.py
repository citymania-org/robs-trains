import grf, lib

from datetime import date

from common import Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_mq_PROPS = dict(
    length=10,
    misc_flags=Train.Flags.USE_2CC,
    company='na',
    power_type='diesel',
    engine_class=Train.EngineClass.DIESEL,
    track_type=standard_gauge,
    max_speed=Train.kmhish(120),
    power=845,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=68,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_1_dsb = Train(
    id='d_d_mq2_1_dsb',
    **COMMON_mq_PROPS,
    name='њDSB MQ',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('adsb1',),
        overlay=('mqalight'),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["COLBALT"]
    ),
    purchase_sprite_towed_id='d_d_mq22_1_dsb',
    country='denmark',
    introduction_date=date(2002, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mq22_1_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY3'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_2_dsb = Train(
    id='d_d_mq2_2_dsb',
    **COMMON_mq_PROPS,
    name='њDSB MQ',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('adsb1',),
        overlay=('mqalight'),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["COLBALT"]
    ),
    purchase_sprite_towed_id='d_d_mq22_2_dsb',
    country='denmark',
    introduction_date=date(2012, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mq22_2_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY3'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_3_dsb = Train(
    id='d_d_mq2_3_dsb',
    **COMMON_mq_PROPS,
    name='њMjbaD MQ',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='d_d_mq22_3_dsb',
    country='denmark',
    introduction_date=date(2020, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
        'Trivia': 'Four sets bought from DSB in 2020 #4111, #4112, #4113 & #4114',
    }),
).add_articulated_part(
    id='d_d_mq22_3_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_4_dsb = Train(
    id='d_d_mq2_4_dsb',
    **COMMON_mq_PROPS,
    name='њArriva AR 3065-4090',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["COLBALT"]
    ),
    purchase_sprite_towed_id='d_d_mq22_4_dsb',
    country='denmark',
    introduction_date=date(2020, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
        'Trivia': 'Sixteen sets bought from DSB in 2020 #4115 - #4130',
    }),
).add_articulated_part(
    id='d_d_mq22_4_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_5_dsb = Train(
    id='d_d_mq2_5_dsb',
    **COMMON_mq_PROPS,
    name='њGCR 3065-4090',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["GREY7"],
        cc2_replace=colours["COLBALT"]
    ),
    purchase_sprite_towed_id='d_d_mq22_5_dsb',
    country='denmark',
    introduction_date=date(2024, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
        'Trivia': 'Sixteen sets bought from Arriva in 2024',
    }),
).add_articulated_part(
    id='d_d_mq22_5_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY7'],
        cc2_replace=colours['COLBALT'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_6_dsb = Train(
    id='d_d_mq2_6_dsb',
    **COMMON_mq_PROPS,
    name='њHHGB DM',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='d_d_mq22_6_dsb',
    country='denmark',
    introduction_date=date(2000, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mq22_6_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['RED'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_7_dsb = Train(
    id='d_d_mq2_7_dsb',
    **COMMON_mq_PROPS,
    name='њNJJ DM',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["YELLOW"]
    ),
    purchase_sprite_towed_id='d_d_mq22_7_dsb',
    country='denmark',
    introduction_date=date(2004, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mq22_7_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['COLBALT'],
        cc2_replace=colours['YELLOW'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_8_dsb = Train(
    id='d_d_mq2_8_dsb',
    **COMMON_mq_PROPS,
    name='њNJJ DM',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["GREY1"]
    ),
    purchase_sprite_towed_id='d_d_mq22_8_dsb',
    country='denmark',
    introduction_date=date(2016, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mq22_8_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['COLBALT'],
        cc2_replace=colours['GREY1'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_9_dsb = Train(
    id='d_d_mq2_9_dsb',
    **COMMON_mq_PROPS,
    name='њNJJ DM',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["COLBALT"],
        cc2_replace=colours["SKY"]
    ),
    purchase_sprite_towed_id='d_d_mq22_9_dsb',
    country='denmark',
    introduction_date=date(2023, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
    }),
).add_articulated_part(
    id='d_d_mq22_9_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['COLBALT'],
        cc2_replace=colours['SKY'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_10_dsb = Train(
    id='d_d_mq2_10_dsb',
    **COMMON_mq_PROPS,
    name='њNJJ DM',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["GREY10"],
        cc2_replace=colours["GREY7"]
    ),
    purchase_sprite_towed_id='d_d_mq22_10_dsb',
    country='denmark',
    introduction_date=date(2017, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
        'Trivia': 'One painted in this livery',
    }),
).add_articulated_part(
    id='d_d_mq22_10_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['GREY10'],
        cc2_replace=colours['GREY7'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_mq2_11_dsb = Train(
    id='d_d_mq2_11_dsb',
    **COMMON_mq_PROPS,
    name='њLT DM',
    liveries=make_psd_cc_liveries(
        'pp/mq2.psd',
        shading=('mqa',),
        paint=('2',),
        overlay=('mqalight'),
        cc_replace=colours["YELLOW"],
        cc2_replace=colours["GREY7"]
    ),
    purchase_sprite_towed_id='d_d_mq22_11_dsb',
    country='denmark',
    introduction_date=date(2021, 1, 1),
    cargo_capacity=64,
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers, up to 3 can be coupled together into a train set',
        'Trivia': 'Three sets rented from NJJ in 2021 #503, #504 & #507',
    }),
).add_articulated_part(
    id='d_d_mq22_11_dsb',
    length=10,
    liveries=make_psd_cc_liveries(
        'pp/10Template.psd',
        shading='1',
        paint='2',
        cc_replace=colours['YELLOW'],
        cc2_replace=colours['GREY7'],
    ),
    cargo_capacity=64,
    loading_speed=10,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
