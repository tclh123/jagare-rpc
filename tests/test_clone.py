# coding: utf-8

import os

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_clone(tmpdir):
    path = tmpdir.mkdir('source').strpath
    to_path = tmpdir.mkdir('target').strpath

    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    to_repo = Jagare.clone_to(path, to_path, is_bare=False, branch='master',
                              is_mirror=False, env={})

    assert to_repo.path.rstrip('/') == os.path.join(to_path, '.git')
    assert to_repo.is_bare is False
    assert to_repo.is_empty is False
    assert to_repo.workdir.rstrip('/') == to_path
    assert to_repo.head == t_repo.head.name


def test_mirror(tmpdir):
    path = tmpdir.mkdir('source').strpath
    to_path = tmpdir.mkdir('target').strpath

    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    to_repo = Jagare.mirror(url=path, to_path=to_path, is_bare=True,
                            branch='master', env={})

    assert to_repo.path.rstrip('/') == to_path
    assert to_repo.is_bare is True
    assert to_repo.is_empty is False
    assert to_repo.workdir is None
    assert to_repo.head == t_repo.head.name
