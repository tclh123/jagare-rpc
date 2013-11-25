
import os
from doubanservice.client import BaseClient, ClientMetaClass, DAEMixedTransport
from .service_gen.jagare import Jagare as genmod

class Client(BaseClient):
    __metaclass__ = ClientMetaClass
    service_name = 'Jagare.jagare'.lower()
    thrift_module = genmod
    host = 'Jagare.jagare.daesvc.douban.com'.lower() if os.environ.get('DOUBAN_PRODUCTION') else '127.0.0.1'
    port = 7303
    connect_timeout = 1.2
    read_timeout = 2
    server_max_requests = 1000
    transport = DAEMixedTransport('jagare', 'Jagare')
    read_timeout = 60
    retries = 3
    connect_timeout = 10

Jagare = Client()
