# coding: utf-8

from ellen.utils import temp_repo


def test_format_patch(tmpdir, Jagare):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)

    t_patch = t_repo.format_patch(ref='master')
    patch = Jagare.format_patch(path, ref='master', from_ref=None)
    assert patch == t_patch
