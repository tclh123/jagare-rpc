# coding: utf-8

from ellen.repo import Jagare

from service_gen.jagare.ttypes import (Repository,
                                       ServiceUnavailable)

# Code provide jagare_client wrapper, save `path` arg.


# TODO: wrap commands to Handler
class Handler(object):

    def get(self, path):
        try:
            repo = Jagare(path)
            return Repository(path=repo.path,
                              is_empty=repo.empty,
                              is_bare=repo.bare,
                              workdir=repo.repository.workdir,
                              head=repo.head and repo.head.name)
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

    def commit(self, path, branch, parent_ref,
               author_name, author_email, message, reflog, data):
        try:
            repo = Jagare(path)
            repo.commit_file(branch, parent_ref,
                             author_name, author_email,
                             message, reflog, data)
            return True
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def resolve_commit(self, path, ref):
        try:
            repo = Jagare(path)
            return repo.resolve_commit(ref)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def resolve_type(self, path, version):
        """version means git object sha, return str of blob/tree/commit/tag"""
        try:
            repo = Jagare(path)
            return repo.resolve_type(version)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def create_branch(self, path, name, ref, force):
        try:
            repo = Jagare(path)
            return repo.create_branch(name, ref, force)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def clone_to(self, path, to_path, is_bare, branch, is_mirror, env):
        try:
            repo = Jagare(path)
            to_repo = repo.clone(path=to_path, bare=is_bare, branch=branch,
                                 mirror=is_mirror, env=env)
            return Repository(path=to_repo.path,
                              is_empty=to_repo.empty,
                              is_bare=to_repo.bare,
                              workdir=to_repo.repository.workdir,
                              head=to_repo.head and to_repo.head.name)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def mirror(self, url, to_path, is_bare, branch, env):
        try:
            to_repo = Jagare.mirror(url=url, path=to_path, bare=is_bare,
                                    branch=branch, env=env)
            return Repository(path=to_repo.path,
                              is_empty=to_repo.empty,
                              is_bare=to_repo.bare,
                              workdir=to_repo.repository.workdir,
                              head=to_repo.head and to_repo.head.name)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def init(self, to_path, work_path, is_bare):
        try:
            to_repo = Jagare.init(path=to_path, work_path=work_path,
                                  bare=is_bare)
            return Repository(path=to_repo.path,
                              is_empty=to_repo.empty,
                              is_bare=to_repo.bare,
                              workdir=to_repo.repository.workdir,
                              head=to_repo.head and to_repo.head.name)
        except Exception as e:
            raise ServiceUnavailable(repr(e))
