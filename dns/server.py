# -*- coding: utf-8 -*-
from __future__ import print_function
from dnslib import DNSRecord, RR, A
from dnslib.server import DNSServer, DNSHandler, BaseResolver, DNSLogger


class InterceptResolver(BaseResolver):
    """
        InterceptResolver - proxy requests to upstream server
                            (optionally intercepting)

    """

    def __init__(self, upstream, upstream_port,
                 address, blacklist, block_answer):
        """
            upstream/upstream_port      - upstream server ip and port
            address                     - listen address
            blacklist                   - list of blocked domain names
            block_answer                - default blacklist response
        """
        self.upstream = upstream
        self.upstream_port = upstream_port
        self.address = address
        self.blacklist = blacklist
        self.block_answer = block_answer

    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname

        if qname in self.blacklist:
            answer = RR(self.block_answer, rdata=A(self.address))
            reply.add_answer(answer)
            return reply

        if handler.protocol == 'udp':
            proxy_r = request.send(self.upstream, self.upstream_port)
        else:
            proxy_r = request.send(self.upstream, self.upstream_port, tcp=True)
        reply = DNSRecord.parse(proxy_r)
        return reply


if __name__ == '__main__':
    
    import time
    import config

    port = 53
    address = '127.0.0.1'
    tcp = True

    upstream, upstream_port = config.upstream[0], config.upstream[1]

    resolver = InterceptResolver(upstream,
                                 upstream_port,
                                 address,
                                 blacklist=config.blacklist,
                                 block_answer=config.block_answer)

    print("Starting Intercept Proxy (%s:%d -> %s:%d) [%s]" % (
        address or "*", port,
        upstream, upstream_port,
        "UDP/TCP" if tcp else "UDP"))

    logger = DNSLogger("request, reply, truncated, error", False)

    DNSHandler.log = {
        'log_request',      # DNS Request
        'log_reply',        # DNS Response
        'log_truncated',    # Truncated
        'log_error',        # Decoding error
    }

    udp_server = DNSServer(resolver,
                           port=port,
                           address=address,
                           logger=logger)
    udp_server.start_thread()

    if tcp:
        tcp_server = DNSServer(resolver,
                               port=port,
                               address=address,
                               tcp=True,
                               logger=logger)
        tcp_server.start_thread()

    while udp_server.isAlive():
        time.sleep(1)
