# coding: utf-8

import os
import shutil
import tempfile
from functools import wraps
from contextlib import contextmanager

from service_gen.jagare.ttypes import NoneResult

from dae.api.util import get_tmpdir as get_dae_tmpdir


def check_none_result(f):
    @wraps(f)
    def _(*a, **kw):
        ret = f(*a, **kw)
        if ret is None:
            raise NoneResult
        else:
            return ret
    return _


@contextmanager
def get_tmpdir():
    """return tmpdir, e.g. xxx/jagare-rpc/tmpdir/pulltmp/tmpRSpeEi """

    tmpdir_root = get_dae_tmpdir()
    pulltmp = os.path.join(tmpdir_root, 'pulltmp')
    if not os.path.exists(pulltmp):
        os.makedirs(pulltmp)
    path = tempfile.mkdtemp(dir=pulltmp)

    yield path

    shutil.rmtree(path)
