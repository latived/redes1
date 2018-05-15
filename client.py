#!/usr/bin/env python

import socket

def main(host='localhost', port=12345):
    HOST = host
    PORT = port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))

        clients_input = input("Tell me what \n")
        soc.sendall(clients_input.encode("utf8"))
        result_bytes = soc.recv(4096)
        result_string = result_bytes.decode("utf8")

        print("Result from server is {}".format(result_string))

if __name__ == '__main__':
    main()

