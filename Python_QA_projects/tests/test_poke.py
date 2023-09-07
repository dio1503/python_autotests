import requests
import pytest

# ОБЩИЕ ПЕРЕМЕННЫЕ
host = 'https://api.pokemonbattle.me:9104'
token = 'df554acce850ba2100c6b37c26dbcaef'

def test_trainer_status():
    trainer_info = requests.get(f'{host}/trainers', 
                                params = {'trainer_id': 1475})
    assert trainer_info.status_code == 200

def test_trainer_name():
    answer_body = requests.get(f'{host}/trainers', 
                                params = {'trainer_id': 1475})
    assert answer_body.json()['trainer_name'] == 'khde15'

