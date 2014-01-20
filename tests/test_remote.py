# coding: utf-8

from ellen.utils import temp_repo
from ellen.repo import Jagare as JagareRepo


def test_list_remotes(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    remotes = Jagare.list_remotes(path)

    assert remotes == t_repo.remotes()

    t_repo.add_remote('upstream', 'git@localhost:test.git')
    remotes = Jagare.list_remotes(path)
    assert remotes == [r.name for r in t_repo.remotes()]
    assert 'upstream' in remotes


def test_add_remote(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    ret = Jagare.add_remote(path, 'upstream', 'git@localhost:test.git')

    assert t_repo.remotes() == []  # why?? pygit2 bug??

    repo = JagareRepo(path)

    assert ret is True
    assert 'upstream' in [r.name for r in repo.remotes()]
