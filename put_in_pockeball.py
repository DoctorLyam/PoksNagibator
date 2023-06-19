import pytest
import requests
import json
#from create_pokemon import create_pokemon_func, pok_id1

def put_in_pokeball_func(pok_id0):
    body = {"pokemon_id": pok_id0}
    response1 = requests.post("https://pokemonbattle.me:9104/trainers/add_pokeball",
                            data=json.dumps(body), 
                            headers={"trainer_token": "",
                                     'content-type': 'application/json'})
    print(response1.json())
