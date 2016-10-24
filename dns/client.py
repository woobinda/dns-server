# -*- coding: utf-8 -*-
from dnslib.dns import DNSRecord

def dns_request(domain, qtype, address, port, nodig=False):
	"""
	    Simple DNS Client - may be used to testing responses from DNS server,
	    					results are displayed in the console

	    domain		- domain to resolve
	    qtype		- DNS record type
	    address		- DNS server address
	    port		- DNS server port
	            
	"""
	request = DNSRecord.question(domain, qtype)
	paket = request.send(address, port)
	answer = DNSRecord.parse(paket)
	return answer

if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("--domain", default='google.com', type=str, help='Domain to resolve')
	parser.add_argument("--rtype", default='A', type=str, help='DNS record type')
	parser.add_argument("--address", default='127.0.0.1', type=str, help='DNS server ip address')
	parser.add_argument("--port", default=53, type=int, help='DNS server port')
	args = parser.parse_args()

	domain = args.domain
	rtype = args.rtype
	address = args.address
	port = args.port

	answer = dns_request(domain, rtype, address, port)
	print(answer)
