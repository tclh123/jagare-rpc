# coding: utf-8

from ellen.utils import temp_repo


def test_fetch_all(tmpdir, Jagare):
    path = tmpdir.mkdir('local').strpath
    path_remote = tmpdir.mkdir('remote').strpath

    repo_remote = temp_repo.create_temp_repo(path_remote, is_bare=True)
    repo = repo_remote.clone(path, bare=False, branch='master')

    assert repo.remotes()

    # oneway method
    Jagare.fetch_all(path)


def test_fetch(tmpdir, Jagare):
    path = tmpdir.mkdir('local').strpath
    path_remote = tmpdir.mkdir('remote').strpath

    repo_remote = temp_repo.create_temp_repo(path_remote, is_bare=True)
    repo = repo_remote.clone(path, bare=False, branch='master')

    remote_name = [r.name for r in repo.remotes()][0]
    assert remote_name == 'origin'

    # oneway method
    Jagare.fetch(path, remote_name)


def test_fetch_raw(tmpdir, Jagare):
    path = tmpdir.mkdir('local').strpath
    path_remote = tmpdir.mkdir('remote').strpath

    repo_remote = temp_repo.create_temp_repo(path_remote, is_bare=True)
    repo = repo_remote.clone(path, bare=False, branch='master')

    remote_name = [r.name for r in repo.remotes()][0]
    assert remote_name == 'origin'

    if not isinstance(remote_name, str):
        remote_name = remote_name.encode('utf-8')

    # oneway method
    Jagare.fetch_raw(path, name=remote_name, is_q=False, env=None)
