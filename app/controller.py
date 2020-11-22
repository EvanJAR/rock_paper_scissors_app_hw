from flask import render_template
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route('/<player_one_choice>/<player_two_choice>')
def play_the_game():
    player_1 = Player("Player 1", player_one_choice)
    player_2 = Player("Player 2", player_two_choice)
    game = Game(player_1, player_2)
    winner = game.get_winner()
    return render_template('result.html', winner=winner)