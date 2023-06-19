import json
import requests


def kill_my_poks():
    find_resp = requests.get("https://pokemonbattle.me:9104/pokemons?trainer_id=3491&status=1")
    found = json.loads(find_resp.content)

    #print(len(found))
    for p in range(len(found)):
        body = {"pokemon_id": found[p]["id"]}
        kill_resp = requests.post("https://pokemonbattle.me:9104/pokemons/kill", data=json.dumps(body),
                                  headers={"trainer_token": "",
                                     'content-type': 'application/json'})
        break

kill_my_poks()
        