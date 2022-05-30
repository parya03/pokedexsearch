import unittest
import main
import pokedex
import pokemon

def run_tests():
    unittest.main()

class TestStringMethods(unittest.TestCase):
    def test_search_button_handle(self):
        self.assertNotEqual(main.search_button_handle(), None) #Check if function actually returned something

    def test_narrow_down_button_handle(self):
        self.assertNotEqual(main.narrow_down_button_handle(), None) #Check if function actually returned something

    def test_search_pokemon(self):
        self.assertNotEqual(pokedex.search_pokemon(), None) #Check if function actually returned something

    def test_store_json_as_dict(self):
        sample_json = {"1": 1, "2": 2}
        self.assertNotEqual(pokemon.store_json_as_dict(), None) #Check if function actually returned something