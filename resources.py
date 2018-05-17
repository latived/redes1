import os

from game import Player

GAMES_PATH = 'games/'
PLAYERS_PATH = 'players/'

class GameResources:
    def get_new_id():
        games = os.listdir(GAMES_PATH)
        # TODO: check file names "game_<id>"
        return len(games) + 1

class PlayerResources:
    def get_new_id():
        players = os.listdir(PLAYERS_PATH)
        # TODO: check file names "player_<id>"
        return len(players) + 1

    def get_player(player_id):
        players = os.listdir(PLAYERS_PATH)
        # TODO: check file name "player_<id>"
        # TODO: construct player info (name, etc)
        return Player(name='lativ')


class Command:
    VALID_COMMANDS = ["CREATE", "ADD", "REMOVE", 
            "START", "FOCUS", "CONF", 
            "PLAY", "SHOW", "LIST", 
            "HELP", "EXIT", "QUIT"]

    def create(options):
        print("You are inside CREATE game function!")
        print("Options given: {}".format(options))
        
        if len(options) != 1:
            raise SyntaxError("Missing options to command 'CREATE'.")

        game_type = options[0]  

        if game_type not in ['1', '2', '1x1', '2x2']:
            raise SyntaxError("Malformed option '{}'."
                    .format(game_type))
        
        # TODO: create game, bind owner to this game, return game_id
        # TODO: pass owner_id someway (socket port?)
        # TODO: create player by the time he connects with server
        game = Game(owner_id, game_type) # TODO: all above
       

        # TODO: check options
        return "created {} sucessfuly.".format(options[0])

    def conf_play(options):
        print("You are inside CONF PLAY game function!")
        print("Options given: {}".format(options))
        # TODO: check options
        return "configured play {} with option {} sucessfuly.".format(
                options[0], options[1])


