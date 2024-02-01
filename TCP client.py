#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# or you can specify "host = '192.168.1.104'"
host = socket.gethostname()

port = 444

clientsocket.connect(('192.168.100.14', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))