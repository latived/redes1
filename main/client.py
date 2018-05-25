#!/usr/bin/env python

import socket
# TODO: many things, first is CLEAN THE CODE
def main(host='localhost', port=12345):
    HOST = host
    PORT = port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        
        console_text = 'COMMAND?\n'
        cmd_input = input(console_text)

        _, local_port = soc.getsockname()

        my_team = None
        my_turn = None

        while cmd_input != "QUIT":
            soc.sendall(cmd_input.encode("utf8"))
            msg_in = soc.recv(4096).decode()
            answer, status_cod, data = msg_in.split('\n')
                
            cod = status_cod[-1]

            if cod == '1':
                console_text = 'COMMAND?\n'
            elif cod == '2':
                my_turn = my_team == data
            elif cod == '3':
                console_text = 'GAME STARTED!\n\n{}"s turn{}'
                pairs = [eval(p) for p in data.split(':')]
                if (local_port, 'white') in pairs:
                    my_team = 'white'
                else:
                    my_team = 'black'
                    my_turn = False 
            elif cod == '4':
                console_text = 'GAME ENDED!\n'

            if my_turn: # False or None
                if my_team: # white/black or None
                    cmd_input = input(console_text
                            .format(my_team, ': '))
                else:
                    cmd_input = input(console_text)
            else:
                if my_team == 'white':
                    input(console_text
                            .format('black', '.'))
                else:
                    input(console_text
                            .format('white', '.'))


        print("Quiting main...\n")


if __name__ == '__main__':
    main()

