import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/reg',
              json={
              "trainer_token": "d5c99c256659f7373527a94539d27693",
              "email": "vlada-zv@mail.ru",
              "password": "Гавгав7"
              },
              headers={'Content-Type': 'application/json'})
print(response)

import requests

url = 'https://api.pokemonbattle.me:9104/pokemons'
data = {
    "name": "базавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

headers = {'Content-Type': 'application/json','trainer_token': 'd5c99c256659f7373527a94539d27693'}

response = requests.post(url=url, json=data, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    print("Запрос успешно выполнен.")
    print(response.json())  # Если сервер возвращает JSON, можно распечатать его содержимое
else:
    print(f"Ошибка при выполнении запроса. Код статуса: {response.status_code}")
    print(response.text)  # Вывести текст ответа для дополнительной диагностики

import requests

url = 'https://api.pokemonbattle.me:9104/pokemons'
data = {
    "pokemon_id": "19908",
    "name": "котиковый",
}

headers = {'Content-Type': 'application/json','trainer_token': 'd5c99c256659f7373527a94539d27693'}

response = requests.put(url=url, json=data, headers=headers)
print(response.json())

import requests

url = 'https://api.pokemonbattle.me:9104/trainers/add_pokeball'
data = {
    "pokemon_id": "19908",
}

headers = {'Content-Type': 'application/json','trainer_token': 'd5c99c256659f7373527a94539d27693'}

response = requests.post(url=url, json=data, headers=headers)
print(response.json())
