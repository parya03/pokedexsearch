from requests import get
import json

class Pokedex:
    def search_pokemon(self, pokemon_name):
        response = get("https://pokeapi.co/api/v2/pokemon/" + pokemon_name).json()
        return response