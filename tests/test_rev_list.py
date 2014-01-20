# coding: utf-8

from ellen.utils import temp_repo


def test_rev_list(tmpdir, Jagare):
    path = tmpdir.strpath

    repo = temp_repo.create_temp_repo(path, is_bare=True)
    from_sha = repo.sha('master')
    temp_repo.commit_something(path)

    ret = Jagare.rev_list(path, to_ref='master', from_ref=from_sha,
                          file_path=None, skip=None, max_count=None,
                          author=None, query=None, first_parent=None,
                          since=None, no_merges=None)

    assert ret[0].committer
    assert ret[0].author
    assert ret[0].sha
    assert ret[0].type == 'commit'
