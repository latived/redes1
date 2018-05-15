#!/usr/bin/env python

import socket

valid_commands = ["CREATE", "ADD", "REMOVE", "START", "FOCUS", "CONF", 
        "PLAY", "SHOW", "LIST", "HELP", "EXIT", "QUIT"]

# Parse command and return a instance of the desired command
def parse_cmd(cmd_full):
    # Split by spaces to get COMMAND <option(s)>=<value>
    cmd = cmd_full.split(' ')

    if cmd[0] not in valid_commands:
        msg = "Invalid command!"
        raise SyntaxError(msg)
    
    return getattr(Command, cmd[0], cmd[1:])

def client_thread(conn, host, port, MAX_BUFFER_SIZE = 4096):
    with conn:
        while True:
            command = conn.recv(MAX_BUFFER_SIZE)
            if not command: break # TODO: add useful msg
            command_clean = command.decode("utf8").rstrip()

            # Parse command
            msg_return = parse_cmd(command_clean).encode("utf8")
            conn.sendall(msg_return)
        
        print("Connection " + host + ":" + port + " ended")

