class Game:

    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player 
    
    def get_winner(self, first_player, second_player):
    #     # rock vs scissors
        if self.first_player.choice == "rock" and self.second_player.choice == "scissors":
            return self.first_player.name
        elif self.second_player.choice == "rock" and self.first_player.choice == "scissors":
            return self.second_player.name
        # rock vs paper
        if self.first_player.choice == "paper" and self.second_player.choice == "rock":
            return self.first_player.name
        elif self.second_player.choice == "paper" and self.first_player.choice == "rock":
            return self.second_player.name
        # paper vs scissors
        if self.first_player.choice == "scissors" and self.second_player.choice == "paper":
            return self.first_player.name
        elif self.second_player.choice == "scissors" and self.first_player.choice == "paper":
            return self.second_player.name