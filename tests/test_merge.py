# coding: utf-8

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_merge_base(tmpdir):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=True)

    to_sha = from_sha = t_repo.sha('master')
    t_oid = t_repo.merge_base(to_sha, from_sha)
    sha = Jagare.merge_base(path, to_sha, from_sha)

    assert sha == t_oid.hex
