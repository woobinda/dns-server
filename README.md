# DNS-Proxy server.

DNS server with blacklist support, based on Python dnslib 0.9.6 library.

config.py - startup config for DNS server. The default server listens to 127.0.0.1 port 53.

client.py - is a simple dns client, and may be used for testing responses from DNS server.

To install all dependencies and run the application, you can use the console command to Makefile:

$make start
