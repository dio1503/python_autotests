import requests

# ОБЩИЕ ПЕРЕМЕННЫЕ
host = 'https://api.pokemonbattle.me:9104'
token = 'df554acce850ba2100c6b37c26dbcaef'

trainer_info = requests.get(f'{host}/trainers', 
                                params = {'trainer_id': 1475, 'trainer_name': 'khde15'})
print(trainer_info.status_code)
#print(trainer_info.trainer_name)

#params = {'trainer_id': 1475}