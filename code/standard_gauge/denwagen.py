import grf, lib

from datetime import date

from common import g, Train, colours, make_psd_cc_liveries, standard_gauge

COMMON_nwagen_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=35,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    max_speed=Train.kmhish(140),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

de_p_nwagen_a1 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_a1',
    name='DB AB4n-59',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1959, 1, 1),
    cargo_capacity=78,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

de_p_nwagen_a2 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_a2',
    name='DB ABn 703',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["COBALT"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1975, 1, 1),
    cargo_capacity=78,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

de_p_nwagen_a3 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_a3',
    name='DB ABn 703',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1978, 1, 1),
    cargo_capacity=78,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

de_p_nwagen_a4 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_a4',
    name='DB ABnrzb 772', #café
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1984, 1, 1),
    cargo_capacity=78,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class with café',
    }),
)

de_p_nwagen_a5 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_a5',
    name='DB ABnrzb 772', #no café
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1984, 1, 1),
    cargo_capacity=78,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

de_p_nwagen_a6 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_a6',
    name='DB ABn 402',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1987, 1, 1),
    cargo_capacity=78,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

de_p_nwagen_a7 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_a7',
    name='DB ABn 402',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1996, 1, 1),
    cargo_capacity=78,
    additional_text=grf.fake_vehicle_info({
        'Use': '1st & 2nd class',
    }),
)

de_p_nwagen_b1 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_b1',
    name='DB B4n-59',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1959, 1, 1),
    cargo_capacity=96,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

de_p_nwagen_b2 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_b2',
    name='DB Bn 720',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["COBALT"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1975, 1, 1),
    cargo_capacity=96,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

de_p_nwagen_b3 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_b3',
    name='DB Bnrzb 728', #different roof
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1978, 1, 1),
    cargo_capacity=96,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

de_p_nwagen_b4 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_b4',
    name='DB Bnrzb 778',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1984, 1, 1),
    cargo_capacity=96,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

de_p_nwagen_b5 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_b5',
    name='DB Bn 432',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1987, 1, 1),
    cargo_capacity=96,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

de_p_nwagen_b6 = Train(
    **COMMON_nwagen_PROPS,
    id='de_p_nwagen_b6',
    name='DB Bn 432',
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1996, 1, 1),
    cargo_capacity=96,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class',
    }),
)

COMMON_nwagens_PROPS = dict(
    length=12,
    misc_flags=Train.Flags.USE_2CC,
    power_type='na',
    engine_class=Train.EngineClass.DIESEL, 
    track_type=standard_gauge,
    power=0,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=36,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cost_factor=25,
    loading_speed=20,
    max_speed=Train.kmhish(140),
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
)

de_p_nwagen_s1 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s1',
    name='DB BPw4nf-59', #black frame
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1959, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s2 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s2',
    name='DB BDnf 738', #blue frame
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["COBALT"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1975, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s3 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s3',
    name='DB BDnrzf 740 "Karlsruher Kopf"', #plain cab
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1971, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s4 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s4',
    name='DB BDnrzf 740 "Karlsruher Kopf"', #cab with orange stripes
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["GREY3"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1971, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s5 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s5',
    name='DB BDnrzf 740 "Karlsruher Kopf"', #cab with orange stripes and blue frame
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["GREY3"],
        cc2_replace=colours["COBALT"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1975, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s6 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s6',
    name='DB BDnrzf 784 "Karlsruher Kopf"', #citybahn
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["ORANGE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1984, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s7 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s7',
    name='DB BDnrzf 461 "Karlsruher Kopf"', #big doors
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1987, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s8 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s8',
    name='DB BDnrzf 477.2 "Karlsruher Kopf"', #windows
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1987, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s9 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s9',
    name='DB Bndzf 479 "Wittenberger Kopf"', #pinhead
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["TURQUOISE"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1994, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s10 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s10',
    name='DB BDnrzf 460 "Karlsruher Kopf"', #big doors
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1996, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s11 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s11',
    name='DB BDnrzf 477.2 "Karlsruher Kopf"', #windows
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1996, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)

de_p_nwagen_s12 = Train(
    **COMMON_nwagens_PROPS,
    id='de_p_nwagen_s12',
    name='DB Bndzf 479 "Wittenberger Kopf"', #pinhead
    liveries=make_psd_cc_liveries(
        'pp/Template.psd',
        shading=('12a',),
        paint=('12b',),
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    country='germany',
    company='na',
    introduction_date=date(1996, 1, 1),
    cargo_capacity=66,
    additional_text=grf.fake_vehicle_info({
        'Use': '2nd class DVT',
    }),
)
