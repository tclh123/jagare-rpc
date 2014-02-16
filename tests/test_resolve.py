# coding: utf-8

from ellen.utils import temp_repo


def test_resolve_commit(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)

    t_sha = t_repo.resolve_commit('master')
    sha = Jagare.resolve_commit(path, 'master')

    assert sha == t_sha


def test_resolve_type(tmpdir, Jagare):
    path = tmpdir.strpath
    temp_repo.create_temp_repo(path, is_bare=True)

    type_ = Jagare.resolve_type(path, 'master')
    assert type_ == 'commit'


def test_sha(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)

    t_sha = t_repo.sha('master')
    sha = Jagare.sha(path, 'master')

    assert sha == t_sha
