import json

class Pokemon:
    pokemon_dict = {}

    def store_json_as_dict(self, raw_json_input):
        global pokemon_dict
        pokemon_dict = raw_json_input
        return pokemon_dict