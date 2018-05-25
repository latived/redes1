
class Player:

    all_players = []

    def __init__(self, player_id, name, host, port):
        self.my_games = []
        self.actual_game = None   # No main yet
        self.playing_games = []
        self.player_id = player_id
        self.name = name
        self.host = host
        self.port = port

    def __str__(self):
        return "{}, {}".format(self.player_id, self.name)

