from datetime import date

class Game:

    # my_games to be added
    all_games = []
    open_games = []
    closed_games = []

    def __init__(self, game_id, owner_id, game_type, players=[],
            teams = {'white': [], 'black': []},
            event = 'Local match at IC - UFAL',
            site = 'Maceió, AL - Brazil',
            date_match = date.today().isoformat(),
            moves = []
            ):
        self.game_id = game_id
        self.owner_id = owner_id
        self.players = players # NOT USEFUL; REMOVE SOON; LEAVE TEAMS
        self.teams = teams 
        #self.teams_names = {} to be added
        self.game_type = game_type # NOT SAVED FOR NOW
        # useful info below?
        self.event = event
        self.site = site
        self.date = date_match
        # self.round to be added?
        # self.result to be added?

        # Each move is a string in algebraic notation
        # denotating each player move separated by a space
        self.moves = moves

    # TODO: adapt info return to accomodate changes made in Game
    # above
    # TODO: see if returned string can be made PGN-like output
    def __str__(self):
        def get_moves_string(moves_list):
            moves_list_new = []
            index = 1
            for move_pair in moves_list:
                moves_list_new.append(("{}. " + move_pair + " ")
                        .format(index))
                index += 1
            return ''.join(moves_list_new)

        out = """[OwnerID '{}']\n[Event '{}']\n[Site '{}']\n[Date '{}']\n[White '{}']\n[Black '{}']\n{}"""

        # TODO: add method to check game integrity (fields with OK
        # values)
        if (len(self.teams['white']) == 0 or
                len(self.teams['black']) == 0):
            print('missing player?')
            return out.format(
                    self.owner_id,
                    self.event,
                    self.site,
                    self.date,
                    'Missing?',
                    'Missing?',
                    get_moves_string(self.moves)
                    )

        return out.format(
                self.owner_id, 
                self.event,
                self.site,
                self.date,
                self.teams['white'][0],
                self.teams['black'][0],
                get_moves_string(self.moves)
                )
