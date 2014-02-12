# coding: utf-8

from functools import wraps

from service_gen.jagare.ttypes import NoneResult


def check_none_result(f):
    @wraps(f)
    def _(*a, **kw):
        ret = f(*a, **kw)
        if ret is None:
            raise NoneResult
        else:
            return ret
    return _
