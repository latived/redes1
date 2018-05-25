#!/usr/bin/env python

from threading import Thread
from .client_thread import client_thread

import socket
import sys
import traceback


def start_server(host='localhost', port=12345):

    HOST = host
    PORT = port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Socket created")

        try:
            soc.bind((HOST, PORT))
            print('Socket bind complete')
        except socket.error as msg:
            print('Bind failed. Error: ' + str(sys.exc_info()))
            sys.exit()

        soc.listen(2)
        print('Socket now listening')

        while True:
            conn, addr = soc.accept()
            host, port = str(addr[0]), str(addr[1])
            print('Accepting connection from ' + host + ':' + port)

            try:
                Thread(target=client_thread, 
                        args=(conn, host, port)).start()
            except:
                print("Terrible error!")
                traceback.print_exc()


if __name__ == '__main__':
    start_server()