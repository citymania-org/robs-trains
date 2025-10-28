d_d_y6_1_dsb = Train(
    id='d_d_y6_1_dsb',
    **COMMON_y6_PROPS,
    name='OHJ YM-YS',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'X',
    }),
).add_articulated_part(
    id='d_d_y62_1_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y6_2_dsb = Train(
    id='d_d_y6_2_dsb',
    **COMMON_y6_PROPS,
    name='VLTJ YM-YS',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    introduction_date=date(1983, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'Three locomotives bought in 1983 #12, #13, #14, named Storåen, Vigen and Tangen',
    }),
).add_articulated_part(
    id='d_d_y62_2_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y6_3_dsb = Train(
    id='d_d_y6_3_dsb',
    **COMMON_y6_PROPS,
    name='VLTJ YM-YS',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'One more locomotive was bought from NJ in 2005 #16, named Heden',
    }),
).add_articulated_part(
    id='d_d_y62_3_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y7_1_dsb = Train(
    id='d_d_y7_1_dsb',
    **COMMON_y7_PROPS,
    name='OHJ YM-YM',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='denmark',
    introduction_date=date(1975, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Owners': 'X',
    }),
).add_articulated_part(
    id='d_d_y72_1_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y7_2_dsb = Train(
    id='d_d_y7_2_dsb',
    **COMMON_y7_PROPS,
    name='VLTJ YM-YM',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    country='denmark',
    introduction_date=date(1983, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'Three locomotives bought in 1983 #12, #13, #14, named Storåen, Vigen and Tangen',
    }),
).add_articulated_part(
    id='d_d_y72_2_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["CREAM"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

d_d_y7_3_dsb = Train(
    id='d_d_y7_3_dsb',
    **COMMON_y7_PROPS,
    name='VLTJ YM-YM',
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    country='denmark',
    introduction_date=date(1999, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Use': 'Local passengers',
        'Trivia': 'One more locomotive was bought from NJ in 2005 #16, named Heden',
    }),
).add_articulated_part(
    id='d_d_y72_3_dsb',
    length=8,
    liveries=make_psd_cc_liveries(
        'pp/8Template.psd',
        shading=('1',),
        paint=('2',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["RED"]
    ),
    cargo_capacity=1,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)
