# coding: utf-8

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_list_branches(tmpdir):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    tags = Jagare.list_tags(path)

    assert tags == list(t_repo.tags)
