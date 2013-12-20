# coding: utf-8

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_get(tmpdir):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    repo = Jagare.get(path)

    assert repo.path.rstrip('/') == path
    assert repo.is_bare is True
    assert repo.is_empty is False
    assert repo.workdir is None
    assert repo.head == t_repo.head.name
