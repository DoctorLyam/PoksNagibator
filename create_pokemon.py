import pytest
import requests
import json
import random

def create_pokemon_func():
    with open('names.txt', 'r', encoding='utf-8') as file:
        words = file.readlines()
        rname = random.choice(words)
    
    sotnya = random.randint(0,9)
    desyatka = random.randint(0,9)
    edinica = random.randint(0,9)
    phurl = f"https://dolnikov.ru/pokemons/albums/{sotnya}{desyatka}{edinica}.png"

    body = {"name":rname, 
        "photo":phurl}
    response = requests.post("https://pokemonbattle.me:9104/pokemons",
                            data=json.dumps(body), 
                            headers={"trainer_token": "",
                                     'content-type': 'application/json'})
    
    b_list = json.loads(response.content)
    pok_id = b_list["id"]
    print(pok_id)
    print(response.json())
    return pok_id

#create_pokemon_func()