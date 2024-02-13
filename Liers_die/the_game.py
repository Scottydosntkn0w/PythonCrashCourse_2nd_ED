from player import Player

"""
each player starts with 6 die






"""
class liersDie:
    def __init__(self) -> None:
        self.get_players()
        self.begin_round()

    def get_players(self):

        number_of_players = input("How many players?")
        number_of_players = int(number_of_players)
        self.players = [Player() for i in range(number_of_players)]
        x=0
        for player in self.players:
            x+=1
            name = input(f"what is player {x} name? ")
            player.Name = name

        print('Hello: ')
        for player in self.players:
            print(player.Name)

    def begin_round(self):

        for player in self.players:
            player.roll_dice()
            

if __name__ == '__main__':
    # Make a game instance, and run the game.
    LiersDie = liersDie()
    #LiersDie.run_game()
