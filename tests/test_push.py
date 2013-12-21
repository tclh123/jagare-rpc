# coding: utf-8

from jagare_client import Jagare

from ellen.utils import temp_repo
from ellen.repo import Jagare as JagareRepo


def test_push(tmpdir):
    path = tmpdir.mkdir('source').strpath
    path2 = tmpdir.mkdir('target').strpath
    repo = temp_repo.create_temp_repo(path, is_bare=True)

    repo2 = JagareRepo.init(path2, bare=True)
    assert repo2.empty is True

    repo.add_remote('origin', repo2.path)
    ret = Jagare.push(path, 'origin', 'master', env={})
    assert not repo2.empty

    assert ret.stdout is not None  # why stdout == ''
    assert ret.stderr is not None  # why stderr != ''
    assert ret.fullcmd
    assert ret.returncode == 0
