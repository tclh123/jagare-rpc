# coding: utf-8

from ellen.utils import temp_repo


def test_archive(tmpdir, Jagare):
    path = tmpdir.strpath
    temp_repo.create_temp_repo(path, is_bare=True)

    stdout = Jagare.archive(path, prefix='test', ref='master')

    assert stdout
