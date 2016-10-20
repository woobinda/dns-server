# -*- coding: utf-8 -*-
import socket
from config import black_list, upstream_server, failed_answer


def request_to_upstream(upstream_server, data):
	upstream_server_ip, upstream_server_post = upstream_server[0], upstream_server[1]
	sock_to_upstream = socket.socket()
	sock_to_upstream.connect((upstream_server_ip, upstream_server_post))
	sock_to_upstream.send(data)
	data_from_upstream= sock_to_upstream.recv(1024)
	sock_to_upstream.close()
	return data_from_upstream


def run(black_list, upstream_server, failed_answer):
	sock = socket.socket()
	sock.bind(('', 2053))
	sock.listen(10)


	conn, addr = sock.accept()
	print('connected:', addr)

	while True:
		data_from_client = conn.recv(1024)
		if not data_from_client:
			break
		if data_from_client not in black_list:
			resolved_ip = request_to_upstream(upstream_server, data_from_client)
			conn.send(resolved_ip)
		else:
			conn.send(failed_answer)
	
	conn.close()


if __name__ == '__main__':
	import config
	run(config.black_list, config.upstream_server, config.failed_answer)
