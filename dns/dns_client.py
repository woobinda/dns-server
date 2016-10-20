# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 2053))
sock.send('google.com')

data = sock.recv(1024)
sock.close()

print(data)