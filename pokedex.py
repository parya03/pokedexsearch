from requests import get
import json

class Pokedex:
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    
    def search_pokemon(self, pokemon_name):
        response = get(self.base_url + pokemon_name).json()
        return response