#!/usr/bin/env python

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from service_gen.jagare import Jagare as genmod
from services.jagare_handler import Handler

# set host, port
host = '127.0.0.1'
port = 7303

# set handler to our implementation
handler = Handler()

processor = genmod.Processor(handler)
transport = TSocket.TServerSocket(host, port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print 'Starting server'
server.serve()
