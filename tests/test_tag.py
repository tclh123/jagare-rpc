# coding: utf-8

from ellen.utils import temp_repo


def test_list_branches(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)
    tags = Jagare.list_tags(path)

    assert tags == list(t_repo.tags)
