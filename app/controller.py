from flask import render_template, request, redirect, url_for
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/<choice_1>/<choice_2>')
def play_the_game(choice_1, choice_2):
    draw = "It's a draw"
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    current_game = Game(player_1, player_2)
    winner = current_game.get_winner(player_1, player_2)
    return render_template('result.html', choice_1=choice_1, choice_2=choice_2, winner=winner)