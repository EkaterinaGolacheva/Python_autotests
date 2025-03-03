import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '11111111111111111111111111111'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

BODY_REG = {
    "trainer_token": TOKEN,
    "email": "ekaterina2034@gmail.com",
    "password": "Iloveqa123"
}

BODY_CONFIRMATION = {
    "trainer_token": TOKEN  
}

BODY_CREATE = {"name": "generate",
    "photo_id": -1}

BODY_CATCHE = {
    "pokemon_id": "247386"
}

BODY_BATTLE = {"attacking_pokemon": "247386",
    "defending_pokemon": "248420"}

BODY_NAME = {
    "pokemon_id": "248431",
    "name": "Lakky",
    "photo_id": 45
}

BODY_KNOCKOUT = {
    "pokemon_id": "247385"
}



response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(response_create.text)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_NAME)
print(response_name.text)

response_catche = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_CATCHE)
print(response_catche.text)




'''response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = BODY_KNOCKOUT)
print(response_knockout.text)

response_battle = requests.post(url = f'{URL}/battle', headers = HEADER, json = BODY_BATTLE)
print(response_battle.text)
MESSAGE = response_battle.json()['message']
print(MESSAGE)

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = BODY_REG)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = BODY_CONFIRMATION)
print(response_confirmation.text)'''
