# coding: utf-8

from ellen.repo import repository

from service_gen.jagare.ttypes import (Repository,
                                       ServiceUnavailable)


class Handler(object):

    def get(self, path):
        try:
            repo = repository(path)
            return Repository(path=repo.path,
                              is_empty=repo.is_empty,
                              is_bare=repo.is_bare)
        except Exception as e:
            raise ServiceUnavailable(repr(e))
