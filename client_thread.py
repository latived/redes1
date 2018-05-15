#!/usr/bin/env python

import socket

# TODO: find a better name to module 'Command'
from Command import VALID_COMMANDS 
from Command import Command 

# Parse command and return a instance of the desired command
def parse_cmd(cmd_full):
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
                cmd[1].lower()]))(cmd[2:])
        else:
            raise SyntaxError("Missing options to command '{}'."
                .format(cmd[:2]))
    elif cmd[0] not in VALID_COMMANDS:
        msg = "Invalid command '{}'."
        raise SyntaxError(msg.format(cmd[0]))

    return getattr(Command, cmd[0].lower())(cmd[1:])

def client_thread(conn, host, port, MAX_BUFFER_SIZE = 4096):
    with conn:
        while True:
            command = conn.recv(MAX_BUFFER_SIZE)
            if not command: break # TODO: add useful msg
            command_clean = command.decode("utf8").rstrip()

            # Parse command
            try:
                out_msg = parse_cmd(command_clean)
                conn.sendall(out_msg.encode("utf8"))
            except SyntaxError as e:
                print(e.msg)
                out_msg = 'processing command... ' + e.msg
                conn.sendall(out_msg.encode("utf8"))
            except:
                out_msg = 'unknown error...'
                print(out_msg)
                conn.sendall(out_msg.encode("utf8"))

        print("Connection " + host + ":" + port + " ended")

