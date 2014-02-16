# coding: utf-8

from ellen.utils import temp_repo


def test_diff(tmpdir, Jagare):
    path = tmpdir.strpath

    temp_repo.create_temp_repo(path, is_bare=True)
    diff = Jagare.diff(path, ref='master', from_ref=None, ignore_space=None,
                       flags=None, context_lines=None, paths=None,
                       rename_detection=None)

    assert diff.patches[0].hunks[0].lines[0].attr == '+'
    assert diff.patch
