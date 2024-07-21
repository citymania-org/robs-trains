import grf, lib

from datetime import date

from common import Train, Livery, p_gauge, modern_diesel_sound

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
    loading_speed=5,
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