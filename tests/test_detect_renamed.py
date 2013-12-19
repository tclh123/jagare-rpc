# coding: utf-8

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_detect_renamed(tmpdir):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)

    # FIXME: test case too weak

    new_to_old = t_repo.detect_renamed(ref='master')
    ret = Jagare.detect_renamed(path, ref='master')
    assert ret == new_to_old
