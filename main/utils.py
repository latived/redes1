import os

from .game import Game
from .player import Player

GAMES_PATH = 'games/'
PLAYERS_PATH = 'players/'


class GameResources:

    @classmethod
    def get_new_id(cls):
        return len(Game.all_games) + 1

    @classmethod
    def create_game(cls, owner_id, game_type):
        game = Game(cls.get_new_id(),
                    owner_id,
                    game_type)
        Game.all_games.append(game)
        cls.add_player(game.game_id, owner_id, 'white')
        PlayerResources.add_game(owner_id, game.game_id, True)
        
        return game.game_id 

    @classmethod
    def get_game(cls, game_id):
        for game in Game.all_games:
            if game_id == game.game_id:
                return game

        return None

    @classmethod
    def add_player(cls, game_id, player_id, player_team):
        # TODO: see: if main is not created, what to do?
        game = cls.get_game(game_id)
        if not game:
            raise ValueError("Game '{}' not exists."
                    .format(game_id))

        # Check if there are already enough players in main
        if ((len(game.players) < 4 and game.game_type == '2x2')
                or (len(game.players) < 2 and game.game_type == '1x1')):
            player = PlayerResources.get_player(player_id)

            # Check if player_id is valid
            if not player: 
                raise ValueError("Player {} not exists."
                        .format(player_id))
            elif player in game.players:
                raise ValueError("Player {} already in main."
                        .format(player_id))
            else:
                game.players.append(player)

            print(Game.all_games)
            print([game.teams for game in Game.all_games])
    
            # Check if player_team is valid
            if player_team in game.teams.keys():
                # Check if team is full 
                if ((len(game.teams[player_team]) < 2 and game.game_type ==
                    '2x2') or (len(game.teams[player_team]) == 0 and
                        game.game_type == '1x1')):
                    game.teams[player_team].append(player)
                else:
                    raise ValueError("Team '{}' is already full."
                            .format(player_team))
            else:
                raise ValueError("Team '{}' doesn't exists."
                        .format(player_team))
        else:
            raise ValueError("Can't add more players: main {} already full."
                    .format(game.game_id))



    @classmethod
    def save_game_to_file(cls, game):

        game_name = "game_" + str(game_id)
        game_path = GAMES_PATH + game_name 

        with open(game_path, mode='w') as game_file:
            print(game, file=game_file)

        return game.game_id 


    @classmethod
    def get_game_from_file(cls, game_id):
        games = os.listdir(PLAYERS_PATH)
        # TODO: check file name "player_<id>"
        game = 'game_' + str(game_id)
        game_path = GAMES_PATH + game 
        if game in games:
            
            def get_attr_value(g, attr_name):
                return g.readline().split("["+attr_name)[1][2:-2]

            def get_games_move(moves_line):
                import re
                return re.split('\s\d+\.\s',
                        ' ' + moves_line[:-1] # gambiarrazinha
                        )[1:]

            def get_player_from_team_line(line):
                p_id, _ = line.split(', ')
                player = PlayerResources.get_player(p_id)
                return player

            with open(game_path) as g:
                # [<attribute> "<attr_value>"]
                game_owner = get_attr_value(g, "OwnerID") # New.
                game_event = get_attr_value(g, "Event")
                game_site  = get_attr_value(g, "Site")
                game_date  = get_attr_value(g, "Date")
                # TODO: Round to be added
                white_player_line = get_attr_value(g, "White")
                black_player_line = get_attr_value(g, "Black")
                game_teams['white'].append(get_player_from_team_line(
                    white_player_line))
                game_teams['black'].append(get_player_from_team_line(
                    black_player_line))
                # TODO: Result to be added

                game_moves = get_games_move(g.readline()) 

                return Game(game_id,
                        game_owner,
                        '1x1', # TODO: support to 2x2
                        [game_teams['white'][0], game_teams['black'][0]],
                        game_teams,
                        game_event,
                        game_site,
                        game_date,
                        game_moves
                        )

        return None

class PlayerResources:
    
    @classmethod         
    def get_new_id(cls):
        return len(Player.all_players) + 1
    
    @classmethod 
    def save_player(cls, host, port):
        
#        player_id = PlayerResources.get_new_id()
#        player_name = "player_" + str(player_id)
#        player_path = PLAYERS_PATH + player_name
#
#        with open(player_path, mode='w') as player:
#            print(':'.join([player_name, host, port]), file=player)
#            # TODO: add more things? date? games?

        player_id = cls.get_new_id()
        player_name = "player_" + str(player_id)
        
        player = Player(player_id,
                    player_name, 
                    host, 
                    port)
               
        Player.all_players.append(player)

        return player_id

    @classmethod
    def get_player(cls, player_id):
#        players = os.listdir(PLAYERS_PATH)
#        # TODO: check file name "player_<id>"
#        player = 'player_' + str(player_id)
#        player_path = PLAYERS_PATH + player 
#        if player in players:
#            with open(player_path) as p:
#                name, host, port = p.readline().split(':')
#                return Player(name, host, port)
        for player in Player.all_players:
            if player_id == player.player_id:
                return player

        return None


    # FIXME: add needed exceptions
    @classmethod
    def add_game(cls, player_id, game_id, is_owner):
        player = cls.get_player(player_id)
        game = GameResources.get_game(game_id)

        if is_owner:
            player.my_games.append(game)

        player.actual_game = game
        player.playing_games.append(game)

