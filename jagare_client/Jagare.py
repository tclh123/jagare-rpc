# from thrift import Thrift  # Thrift.TException
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from .service_gen.jagare import Jagare as genmod


class Client(object):
    def __init__(self):
        self.service_name = 'jagare'
        self.thrift_module = genmod
        self.host = '127.0.0.1'
        self.port = 7303
        self.connect_timeout = 1.2
        self.read_timeout = 2
        self.server_max_requests = 1000
        self.read_timeout = 60
        self.retries = 3
        self.connect_timeout = 10

        self.closed = True

    def __getattr__(self, method_name):
        if self.closed:
            self.connect()
        return getattr(self._client, method_name)

    def connect(self):
        transport = TSocket.TSocket(self.host, self.port)
        self.transport = TTransport.TBufferedTransport(transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)  # iport
        self._client = self.thrift_module.Client(self.protocol)

        self.transport.open()
        self.closed = False

    def disconnect(self):
        self.transport.close()
        self.closed = True

Jagare = Client()
