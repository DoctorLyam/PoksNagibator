from time import sleep
from create_pokemon import create_pokemon_func
from put_in_pockeball import put_in_pokeball_func
from find_weak_enemy import getting_weakest_enemy, getting_weakest_enemy_sleep
from get_over_here import get_over_here_func
from kill_all import kill_my_poks

pok_id1 = create_pokemon_func()
put_in_pokeball_func(pok_id1)
enemy_id1 = getting_weakest_enemy()
total1 = get_over_here_func(pok_id1, enemy_id1)

while True:
    while total1 == "Твой покемон победил":
        enemy_id1 = getting_weakest_enemy()
        total1 = get_over_here_func(pok_id1, enemy_id1)

    if  total1 == "Твой покемон проиграл":
        pok_id1 = create_pokemon_func()
        put_in_pokeball_func(pok_id1)
        enemy_id1 = getting_weakest_enemy()
        total1 = get_over_here_func(pok_id1, enemy_id1)

    if total1 == 'Отсутствует обороняющийся покемон(defending_pokemon)':
        kill_my_poks()
        enemy_id1 = getting_weakest_enemy_sleep()
        while not enemy_id1:
            enemy_id1 = getting_weakest_enemy_sleep()
        if enemy_id1:
            pok_id1 = create_pokemon_func()
            put_in_pokeball_func(pok_id1)
            enemy_id1 = getting_weakest_enemy()
            total1 = get_over_here_func(pok_id1, enemy_id1)