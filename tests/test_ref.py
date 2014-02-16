# coding: utf-8

from ellen.utils import temp_repo


def test_list_references(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    refs = Jagare.list_references(path)

    assert refs == t_repo.listall_references()


def test_update_ref(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=False)

    assert t_repo.head.name == 'refs/heads/master'
    head_sha = t_repo.head.target.hex

    temp_repo.commit_something(path)
    assert t_repo.head.target.hex != head_sha
    ret = Jagare.update_ref(path, 'refs/heads/master', head_sha)

    assert ret is True
    assert t_repo.head.target.hex == head_sha


def test_update_head(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=False)
    t_repo.create_branch('br_test_update_head', 'master')

    head_sha = t_repo.head.target.hex
    temp_repo.commit_something(path)
    assert t_repo.head.target.hex != head_sha

    ret = Jagare.update_head(path, 'br_test_update_head')

    assert ret is True
    assert t_repo.head.target.hex == head_sha
