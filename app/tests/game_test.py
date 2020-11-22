import unittest
from app import app
from app.models.player import Player
from app.models.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Evan", "rock")
        self.player_2 = Player("Anna", "paper")
        self.player_3 = Player("Bobby", "scissors")
        self.player_4 = Player("Alex", "rock")
        self.player_5 = Player("Dan", "paper")
        self.player_6 = Player("Irene", "scissors")

        #rock vs scissors
        self.game1 = Game(self.player_1, self.player_3)
        self.game2 = Game(self.player_6, self.player_4)
        #rock vs paper
        self.game3 = Game( self.player_5, self.player_4)
        self.game4 = Game(self.player_1, self.player_2)
        #paper vs scissors
        self.game5 = Game(self.player_6, self.player_2)
        self.game6 = Game(self.player_5, self.player_3)
        #draw
        self.game7 = Game(self.player_1, self.player_4)


#player class tests
    def test_player_has_name(self):
        self.assertEqual("Evan", self.player_1.name) 

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player_1.choice)

#game class tests
    def test_game_has_player_1(self):
        self.assertEqual("rock", self.game1.first_player.choice)

    def test_game_has_player_2(self):
        self.assertEqual("scissors", self.game1.second_player.choice)

# #game class method tests

#     #rock vs scissors
    def test_get_winner__rock_vs_scissors_first_player_wins(self):
        first_player = self.player_1
        second_player = self.player_3
        result = self.game1.get_winner(first_player, second_player)
        self.assertEqual("Evan", result)
    
    def test_get_winner__rock_vs_scissors_second_player_wins(self):
        first_player = self.player_6
        second_player = self.player_4
        result = self.game2.get_winner(first_player, second_player)
        self.assertEqual("Alex", result)
 
#     #rock vs paper

    def test_get_winner__rock_vs_paper__first_player_wins(self):
        first_player = self.player_5
        second_player = self.player_4
        result = self.game3.get_winner(first_player, second_player)
        self.assertEqual("Dan", result) 
   
    def test_get_winner__rock_vs_paper__second_player_wins(self):
        first_player = self.player_1
        second_player = self.player_2
        result = self.game4.get_winner(first_player, second_player)
        self.assertEqual("Anna", result)

#     #paper vs scissors

    def test_get_winner__paper_vs_scissors__first_player_wins(self):
        first_player = self.player_6
        second_player = self.player_2
        result = self.game5.get_winner(first_player, second_player)
        self.assertEqual("Irene", result) 
   
    def test_get_winner__paper_vs_scissors__second_player_wins(self):
        first_player = self.player_5
        second_player = self.player_3
        result = self.game6.get_winner(first_player, second_player)
        self.assertEqual("Bobby", result)

        #draw
    def test_get_winner__rock_vs_rock(self):
        first_player = self.player_1
        second_player = self.player_4
        result = self.game7.get_winner(first_player, second_player)
        self.assertEqual(None, result)