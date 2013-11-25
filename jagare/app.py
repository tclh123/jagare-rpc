# coding: utf-8


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return 'Hello Jagare Service!'
