import json

try:
    with open("pokemons.json", "r") as file:
        pokemons_list = json.load(file)
except FileNotFoundError:
    pokemons_list = []  

name = input("Enter the Pokémon's English name: ")
poke_type = input("Enter the Pokémon's type: ")
hp = int(input("Enter HP: "))
attack = int(input("Enter Attack: "))
defense = int(input("Enter Defense: "))
sp_attack = int(input("Enter Sp. Attack: "))
sp_defense = int(input("Enter Sp. Defense: "))
speed = int(input("Enter Speed: "))

new_pokemon = {
    "name": {
        "english": name
    },
    "type": [poke_type],
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}

pokemons_list.append(new_pokemon)

with open("pokemons.json", "w") as file:
    json.dump(pokemons_list, file, indent=4)

print("\n✅ New Pokémon added successfully!")

import json

with open("pokemons.json", "r") as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))  
