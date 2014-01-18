# coding: utf-8

import os

import pytest

from jagare_client import Jagare

from ellen.utils import temp_repo
from ellen.repo import Jagare as JagareRepo


def test_merge_base(tmpdir):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)

    to_sha = from_sha = t_repo.sha('master')
    t_oid = t_repo.merge_base(to_sha, from_sha)
    sha = Jagare.merge_base(path, to_sha, from_sha)

    assert sha == t_oid.hex


@pytest.fixture(scope="function", params=[True, False])
def no_ff(request):
    return request.param


def test_merge(tmpdir, no_ff):
    path = tmpdir.strpath
    git_dir = os.path.join(path, '.git')

    # `git merge` must be run in a work tree
    t_repo = JagareRepo.init(git_dir,
                             work_path=path, bare=False)
    temp_repo.commit_something(git_dir, file_name='git_init')

    BR = 'br_test_merge'

    ret = t_repo.create_branch(BR, 'master')
    assert ret is True
    sha1 = t_repo.sha('master')

    temp_repo.commit_something(path, branch=BR)

    ret = Jagare.merge(path, ref=BR, msg=None, commit_msg=None,
                       no_ff=no_ff, env=None)
    sha2 = t_repo.sha('master')

    assert sha1 != sha2
    assert t_repo.sha(sha1) == sha1

    assert ret.stdout
    assert ret.stderr == ''
    assert ret.fullcmd
    assert ret.returncode == 0


def test_merge_tree(tmpdir):
    path = tmpdir.strpath
    git_dir = os.path.join(path, '.git')

    # `git merge` must be run in a work tree
    t_repo = JagareRepo.init(git_dir,
                             work_path=path, bare=False)
    temp_repo.commit_something(git_dir, file_name='git_init')

    BR = 'br_test_merge'

    ret = t_repo.create_branch(BR, 'master')
    assert ret is True
    sha1 = t_repo.sha('master')

    temp_repo.commit_something(path, branch=BR)

    ret = Jagare.merge_tree(path, 'master', BR)
    # sha2 = t_repo.sha('master')

    # assert sha1 != sha2
    assert t_repo.sha(sha1) == sha1

    assert ret.has_conflicts is False


def test_merge_head(tmpdir):
    path = tmpdir.strpath
    git_dir = os.path.join(path, '.git')

    # `git merge` must be run in a work tree
    t_repo = JagareRepo.init(git_dir,
                             work_path=path, bare=False)
    temp_repo.commit_something(git_dir, file_name='git_init')

    BR = 'br_test_merge'

    ret = t_repo.create_branch(BR, 'master')
    assert ret is True
    sha1 = t_repo.sha('master')

    temp_repo.commit_something(path, branch=BR)

    ret = Jagare.merge_head(path, BR)
    # sha2 = t_repo.sha('master')

    # assert sha1 != sha2
    assert t_repo.sha(sha1) == sha1

    assert ret.is_fastforward is True
    assert ret.fastforward_oid
    assert ret.is_uptodate is False


def test_merge_commits(tmpdir):
    path = tmpdir.strpath
    git_dir = os.path.join(path, '.git')

    # `git merge` must be run in a work tree
    t_repo = JagareRepo.init(git_dir,
                             work_path=path, bare=False)
    temp_repo.commit_something(git_dir, file_name='git_init')

    BR = 'br_test_merge'

    ret = t_repo.create_branch(BR, 'master')
    assert ret is True
    sha1 = t_repo.sha('master')

    temp_repo.commit_something(path, branch=BR)

    ret = Jagare.merge_commits(path, 'master', BR)
    # sha2 = t_repo.sha('master')

    # assert sha1 != sha2
    assert t_repo.sha(sha1) == sha1

    assert ret.has_conflicts is False
