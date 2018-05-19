#!/usr/bin/env python

import socket
import traceback

# TODO: find a better name to module 'Command'
from command import Command, CommandBoard
from utils import PlayerResources

# Parse command and return a instance of the desired command
def parse_command(cmd_full, player_id):

    # Split by spaces to get COMMAND [, CMD] <option(s)>[,=<value>]
    cmd = cmd_full.split(' ')

    # Check length of command + options
    # All defined commands have at least one option,
    # except for QUIT and HELP (not implemented)
    # TODO: analyse QUIT flow control here
    if len(cmd) < 2: 
        raise SyntaxError("Incomplete or wrong command.")

    # Only command with two consecutives keywords 
    if cmd[0] == "CONF" and cmd[1] == "PLAY":
        if len(cmd[2:]):
            return getattr(Command, '_'.join([cmd[0].lower(), 
                cmd[1].lower()]))(cmd[2:], player_id)
        else:
            raise SyntaxError("Missing options to command '{}'."
                .format(cmd[:2]))
    elif cmd[0] not in Command.VALID_COMMANDS:
        msg = "Invalid command '{}'."
        raise SyntaxError(msg.format(cmd[0]))

    return getattr(Command, cmd[0].lower())(cmd[1:], player_id)

def parse_command_board(team, movement):
    CommandBoard.move()

def client_thread(conn, host, port, MAX_BUFFER_SIZE = 4096):
    
    player_id = PlayerResources.save_player(host, port)
    
    with conn:
        while True:
            command = conn.recv(MAX_BUFFER_SIZE)
            if not command: break # TODO: add useful msg
            cmd_string = command.decode("utf8").rstrip()
            
            # Parse command
            try:
                # encapsulate this conditionals below
                out_msg = 'ANSWER: {}\nSTATUS_COD: {}\nDATA: {}'
                status_cod = Command.STATUS_COD_NORMAL
                data = ''
                if not Command.board_ctx:
                    msg = parse_command(cmd_string, player_id)
                    out_msg = out_msg.format(msg, 
                                status_cod,
                                data) # empty
                else:
                    # HOW TO FIX cmd_string?
                    # HOW TO KNOW/DEFINE PLAYER'S TURN?
                    msg = parse_command_board(team, cmd_string)
                    game = PlayerResources.get_player(
                            player_id).actual_game
                        
                    # Could use a class Board,
                    # but to cut time I will use moves 
                    # to know which player can move

                    # len(moves) % 2 == 0 means that
                    #   turn: whites
                    # else, turn: black
                    moves_sz = len(actual_game.moves)
                    turn = 'white'
                    if (moves_sz % 2) != 0:
                        turn = 'black'
                    
                    if Command.board_greetings: # first move
                        status_cod = Command.STATUS_COD_BOARD_HELLO
                        data = '({},"white"):({},"black")'.format(
                                game.teams['white'][0].port,
                                game.teams['black'][0].port
                                )
                        out_msg = out_msg.format(msg,
                                    status_cod,
                                    data
                                    ) 
                        Command.board_greetings = False
                    elif Command.board_bye: # when True?? last move?
                        status_cod = Command.STATUS_COD_BOARD_BYE
                        out_msg = out_msg.format(msg,
                                    status_cod,
                                    data) # empty
                        Command.board_bye = False 
                        Command.board_ctx = False
                    else: # all moves
                        data = turn
                        status_cod = Command.STATUS_COD_BOARD
                        out_msg = out_msg.format(msg,
                                    Command.STATUS_COD_BOARD,
                                    data)
                
                conn.sendall(out_msg.encode())

            except Exception as e:
                if hasattr(e, 'msg'):
                    conn.sendall(e.msg.encode())
                else:
                    traceback.print_exc()
                    conn.sendall(b'unknown error.')

        # TODO: remove player from games
        print("Connection {}:{} ended".format(host, port))

