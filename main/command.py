
from .utils import GameResources, PlayerResources

class Command:

    STATUS_COD_NORMAL      = 1
    STATUS_COD_BOARD       = 2
    STATUS_COD_BOARD_HELLO = 3
    STATUS_COD_BOARD_BYE   = 4

    # Implemented: 
    #   - CREATE
    #   - PLAY
    #   - START

    VALID_COMMANDS = ["CREATE", "ADD", "REMOVE", 
            "START", "FOCUS", "CONF", 
            "PLAY", "SHOW", "LIST", 
            "HELP", "EXIT", "QUIT"]

    board_ctx = False
    board_greetings = False
    board_bye = False
    
    def create(options, owner_id):
        print("You are inside CREATE main function!")
        print("Options given: {}".format(options))
        
        if len(options) != 1:
            raise SyntaxError("Missing options to command 'CREATE'.")

        game_type = options[0]  

        if game_type not in ['1', '2', '1x1', '2x2']:
            raise SyntaxError("Malformed option '{}'."
                    .format(game_type))
        elif game_type[0] == '1': 
            game_type = '1x1'
        else:
            game_type = '2x2'

        game_id = GameResources.create_game(owner_id, game_type) 

        # TODO: check options
        return "created game_{} sucessfuly.".format(game_id)

    def play(options, player_id):
        print("You, player_{}, are inside PLAY main function!"
                .format(player_id))
        print("Options given: {}".format(options))
        # TODO: add needed exceptions
        game_id = int(options[0])
        # TODO: add player to main
        GameResources.add_player(game_id, player_id, 'black')
        PlayerResources.add_game(player_id, game_id, False)

        return "connected to game_{} sucessfuly.".format(game_id)


    def start(options, player_id):
        print("You, player_{}, are inside START main function!"
                .format(player_id))
        print("Options given: {}".format(options))
        # TODO: add needed exceptions
        game_id = int(options[0])
        # TODO: init main's board
        # TODO: test print board
        # TODO: change input command context

        # ALL OKAY, THEREFORE 
        board_ctx = True
        board_greetings = True
        return "started game_{} sucessfuly.".format(game_id)

    # NOT IMPLEMENTED
    def conf_play(options, owner_id):
        print("You, player_{}, are inside CONF PLAY main function!"
                .format(owner_id))
        print("Options given: {}".format(options))
        # TODO: check options
        # TODO: add play in return
        # return "configured play {} with option {} sucessfuly.".format(
        return "COMMAND NOT IMPLEMENTED"

class CommandBoard:

    def move(self, team, movement):
        pass

    def check(self):
        pass

    def checkmate(self):
        pass


