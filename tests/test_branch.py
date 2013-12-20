# coding: utf-8

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_list_branches(tmpdir):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    branches = Jagare.list_branches(path)

    assert branches == t_repo.branches


def test_create_branch(tmpdir):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)

    TEST_CREATE_BRANCH = 'br_test_create_branch'

    ret = Jagare.create_branch(path, name=TEST_CREATE_BRANCH,
                               ref='master', force=False)

    assert ret is True
    assert TEST_CREATE_BRANCH in t_repo.branches
