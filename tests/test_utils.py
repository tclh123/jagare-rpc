# coding: utf-8

from ellen.repo import Jagare as JagareRepo

from jagare_client.service_gen.jagare.ttypes import NoneResult
from service_gen.jagare.ttypes import NoneResult as NoneResultMock


def test_check_none_result(tmpdir, Jagare):
    path = tmpdir.strpath
    JagareRepo.init(path, bare=True)

    try:
        sha = Jagare.resolve_commit(path, 'master')
    except Exception as e:
        assert type(e) in (NoneResult, NoneResultMock)
