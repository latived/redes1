#!/usr/bin/env python

import socket

def main(host='localhost', port=12345):
    HOST = host
    PORT = port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        cmd_input = ""
        while cmd_input != "QUIT":
            cmd_input = input("COMMAND?\n")
            soc.sendall(cmd_input.encode("utf8"))
            result_bytes = soc.recv(4096)
            result_string = result_bytes.decode("utf8")

            print("ANSWER: {}".format(result_string))

        print("Quiting game...\n")


if __name__ == '__main__':
    main()

