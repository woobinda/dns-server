# DNS-Proxy server.

DNS server with blacklist support, based on Python dnslib 0.9.6 library.

config.py - startup config for DNS server. The default server listens to 0.0.0.0 port 53.
client.py - is a simple dns client, and may be used for testing responses from DNS server.

To install dependencie you can use the console command to Makefile:

$make start

To run application you can use the console command for Makefile:

$make start
