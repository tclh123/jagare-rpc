# coding: utf-8

import pytest

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_get():
    PATH = 'tmp/testdir'

    temp_repo.create_temp_repo(PATH, is_bare=True)
    repo = Jagare.get(PATH)

    assert repo.path
    assert repo.is_bare is True
    assert repo.is_empty is False
    assert repo.workdir is None
