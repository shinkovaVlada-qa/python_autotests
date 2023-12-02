import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'

def test_status_code(): 
    trainer_id = 3738
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id': str(trainer_id)}, timeout=5)

    # Проверка кода статуса
    assert response.status_code == 200, f'Unexpected status code for /trainers. Response: {response.text}'
    # Проверка кода статуса
    assert response.json()['trainer_name'] == 'Котик', ''