# coding: utf-8

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_ls_tree(tmpdir):
    path = tmpdir.strpath
    temp_repo.create_temp_repo(path, is_bare=True)
    ret = Jagare.ls_tree(path, ref='master', req_path=None,
                         recursive=None, with_size=None, with_commit=None,
                         name_only=None)

    assert ret
