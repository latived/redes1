#!/usr/bin/env python

import socket

def do_some_stuff(input_string):
    print("Processing that input!")
    return input_string[::-1]

def client_thread(conn, host, port, MAX_BUFFER_SIZE = 4096):
    with conn:
        input_bytes = conn.recv(MAX_BUFFER_SIZE)

        input_fc = input_bytes.decode("utf8").rstrip()
        res = do_some_stuff(input_fc)
        print("Result of processing {} is: {}".format(input_fc, res))

        vysl = res.encode("utf8")
        conn.sendall(vysl)
        print("Connection " + host + ":" + port + " ended")

