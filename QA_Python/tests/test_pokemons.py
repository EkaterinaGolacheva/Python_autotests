import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '11111111111111111111111111'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '32911'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_name_of_trainer():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'Koko'

def test_city():
    response_city = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_city.json()["data"][0]["city"] == 'Kokoville'

'''def test_premium():
    response_premium = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_premium.json()["data"][0]["is_premium"] == 'false' ПОЧЕМУ ЭТОТ ТЕСТ НЕ РАБОТАЕТ?'''


@pytest.mark.parametrize('key, value', [('trainer_name', 'Koko'), ('id', TRAINER_ID), ('city', 'Kokoville')])
def test_parametrize(key, value): 
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
