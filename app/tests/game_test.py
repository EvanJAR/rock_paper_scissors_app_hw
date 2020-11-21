import unittest
from app import app
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Evan", "rock")
        self.player_2 = Player("James", "Scissors")

#player class tests
    def test_player_has_name(self):
        self.assertEqual("Evan", self.player_1.name) 

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player_1.choice)

#game class tests
    