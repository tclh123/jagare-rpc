# coding: utf-8

from jagare_client import Jagare


def test_init(tmpdir):
    to_path = tmpdir.mkdir('target').strpath

    to_repo = Jagare.init(to_path=to_path, work_path=None, is_bare=True)

    assert to_repo.path.rstrip('/') == to_path
    assert to_repo.is_bare is True
    assert to_repo.is_empty is True
    assert to_repo.workdir is None
    assert to_repo.head is None
