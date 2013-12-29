# coding: utf-8

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_blame(tmpdir):
    path = tmpdir.strpath
    repo = temp_repo.create_temp_repo(path, is_bare=True)

    blobs = [e['name'] for e in repo.ls_tree('master') if e['type'] == 'blob']
    assert blobs

    for b in blobs:
        ret = Jagare.blame(path, ref='master', req_path=b, lineno=1)
        assert ret
