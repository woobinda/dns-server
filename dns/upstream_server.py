# -*- coding: utf-8 -*-
import socket

dns_records = {'google.com':'172.217.17.46', 'mail.ru':'52.203.219.137'}

sock = socket.socket()
sock.bind(('', 3053))
sock.listen(10)
conn, addr = sock.accept()

print('connected:', addr)

while True:
	data = conn.recv(1024)
	if not data:
		break
	if data in dns_records:
		conn.send(dns_records[data])

conn.close()