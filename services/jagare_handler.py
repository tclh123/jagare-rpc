# coding: utf-8

from ellen.repo import Jagare

from service_gen.jagare.ttypes import (Repository,
                                       ServiceUnavailable)


# TODO: wrap commands to Handler

class Handler(object):

    def get(self, path):
        try:
            repo = Jagare(path)
            return Repository(path=repo.path,
                              is_empty=repo.empty,
                              is_bare=repo.bare,
                              workdir=repo.repository.workdir,
                              head=repo.head.name)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def list_branches(self, path):
        try:
            repo = Jagare(path)
            return repo.branches
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def list_tags(self, path):
        try:
            repo = Jagare(path)
            return repo.tags
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def format_patch(self, path, ref, from_ref):
        try:
            repo = Jagare(path)
            return repo.format_patch(ref, from_ref)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def detect_renamed(self, path, ref):
        try:
            repo = Jagare(path)
            return repo.detect_renamed(ref)
        except Exception as e:
            raise ServiceUnavailable(repr(e))
