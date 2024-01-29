"""
Test API
"""

import requests

URL="https://api.pokemonbattle.me:9104"

header={"Content-Type": 'application/json', "trainer_token": "33b7d88547c9df5b65113c5daab9aec9"}

# body={
#    "name": "generate",
#    "photo": "generate"
#}

# response=requests.post(url=f"{URL}/pokemons", json=body, headers=header, timeout=5)
# print(f"Статус код:{response.status_code}. Сообщение: {response.text}")

# body1={
#    "pokemon_id": "20947",
#    "name": "QA-инженер",
#    "photo": "https://dolnikov.ru/pokemons/albums/003.png"
#}
#response=requests.put(url=f"{URL}/pokemons", json=body1, headers=header, timeout=5)
#print(f"Статус код:{response.status_code}. Сообщение: {response.text}")

body2={
    "pokemon_id": "20947"
}
response=requests.post(url=f"{URL}/trainers/add_pokeball", json=body2, headers=header, timeout=5)
print(f"Статус код:{response.status_code}. Сообщение: {response.text}")