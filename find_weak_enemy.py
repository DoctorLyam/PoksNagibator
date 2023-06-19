import pytest
from time import sleep
import requests
import json

def getting_weakest_enemy():
    response2 = requests.get("https://pokemonbattle.me:9104/pokemons?in_pokeball=1")
    a_list = json.loads(response2.content) #method to convert the JSON array to a Python list
    print(a_list)
    result = []
    #sleep(10)
    for p in a_list:
          if "1" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']
               return enemy_id
          elif "2" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']
               return enemy_id
          elif "3" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id
          elif "4" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id    
          elif "5" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id
          elif "6" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id
          elif "7" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id                             
          


def getting_weakest_enemy_sleep():
    response2 = requests.get("https://pokemonbattle.me:9104/pokemons?in_pokeball=1")
    a_list = json.loads(response2.content) #method to convert the JSON array to a Python list
    sleep(5)
    print("Все вражеские покемоны мертвы")
    print(a_list)
    result = []
    for p in a_list:
          if "1" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']
               return enemy_id
          elif "2" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']
               return enemy_id
          elif "3" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id
          elif "4" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id    
          elif "5" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id
          elif "6" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id
          elif "7" in p["attack"] and p['trainer_id'] != "3491":
               result.append(p)
               enemy_id = result[0]['id']  
               return enemy_id          