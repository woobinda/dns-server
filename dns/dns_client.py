# -*- coding: utf-8 -*-
from __future__ import print_function
from dnslib.dns import DNSRecord

def dns_request(domain, qtype, address="127.0.0.1", port=53, nodig=False):
    request = DNSRecord.question(domain, qtype)
    a_pkt = request.send(address,port)
    answer = DNSRecord.parse(a_pkt)
    return answer

answer = dns_request('facebook.com', 'A')
print(answer)
