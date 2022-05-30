import unittest
import main
import pokedex
import pokemon

pokedex_instance = pokedex.Pokedex()
pokemon_instance = pokemon.Pokemon()

class TestStringMethods(unittest.TestCase):
    def test_ui_start(self):
        self.assertEqual(main.ui_start(), 1) #Check if nested functions returned something

    def test_search_pokemon(self):
        self.assertNotEqual(pokedex_instance.search_pokemon(""), None) #Check if function actually returned something, should still return something with blank string

    def test_store_json_as_dict(self):
        sample_json = {"1": 1, "2": 2}
        self.assertNotEqual(pokemon_instance.store_json_as_dict({"1": 1, "2": 2}), None) #Check if function actually returned something

if __name__ == "__main__":
    unittest.main()