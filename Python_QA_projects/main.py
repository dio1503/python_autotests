import requests

# ОБЩИЕ ПЕРЕМЕННЫЕ
host = 'https://api.pokemonbattle.me:9104'
token = 'df554acce850ba2100c6b37c26dbcaef'


# - Создание покемона (**POST /pokemons** (*не забудь про нужный хэдер*))
#В ответе (терминале) должен прийти объект json

create_pok = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers= {"trainer_token": token, "Content-Type": "application/json"})

# print(create_pok.status_code)
print(create_pok.text)
new_pok_id = create_pok.text[7:11]   # Здесь берем из текста ответа номер покемона 
print('Here it is:', new_pok_id)  


# - Смена имени покемона (**PUT /pokemons** (*не забудь про нужный хэдер*))
# В ответе (терминале) должен прийти объект json
new_name_pok = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": new_pok_id,
    "name": "generate",
    "photo": "generate"
}, headers= {"trainer_token": token, "Content-Type": "application/json"})
print(new_name_pok.text)


# - Поймать покемона в покебол (**POST /trainers/add_pokeball** (*не забудь про нужный хэдер*))
# В ответе (терминале) должен прийти объект json

catch_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": new_pok_id
}, headers= {"trainer_token": token, "Content-Type": "application/json"})
print(catch_pokeball.text)

