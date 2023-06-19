import pytest
import requests
import json
#from create_pokemon import *
#from find_weak_enemy import *

def get_over_here_func(pok_id0, enemy_id0):
    try:
        body = {"attacking_pokemon": pok_id0,
            "defending_pokemon": enemy_id0}
        response4 = requests.post("https://pokemonbattle.me:9104/battle",
                                data=json.dumps(body), 
                                headers={"trainer_token": "",
                                        'content-type': 'application/json'})
        print(response4.json())
    
        resvs = json.loads(response4.content)
        total = resvs["result"]

        print(total)
        return total
    except KeyError:
        total0 = resvs["message"]
        return total0
    
#get_over_here_func("8177", "")