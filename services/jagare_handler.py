# coding: utf-8

from ellen.repo import Jagare

from service_gen.jagare.ttypes import (Repository,
                                       ProcessResult,
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

    def list_remotes(self, path):
        try:
            repo = Jagare(path)
            return [r.name for r in repo.remotes()]
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

    def delete_branch(self, path, name):
        try:
            repo = Jagare(path)
            repo.delete_branch(name)
            return True
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

    def list_references(self, path):
        try:
            repo = Jagare(path)
            return repo.listall_references()
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def add_remote(self, path, name, url):
        try:
            repo = Jagare(path)
            repo.add_remote(name, url)
            return True
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def update_ref(self, path, ref, newvalue):
        try:
            repo = Jagare(path)
            repo.update_ref(ref, newvalue)
            return True
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def update_head(self, path, branch_name):
        try:
            repo = Jagare(path)
            repo.update_head(branch_name)
            return True
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def sha(self, path, revision):
        try:
            repo = Jagare(path)
            return repo.sha(revision)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def merge_base(self, path, to_sha, from_sha):
        try:
            repo = Jagare(path)
            oid = repo.merge_base(to_sha, from_sha)
            return oid.hex if oid else None
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def fetch_all(self, path):
        repo = Jagare(path)
        repo.fetch_all()

    def fetch(self, path, name):
        repo = Jagare(path)
        repo.fetch(name)

    def merge(self, path, ref, msg, commit_msg, no_ff, env):
        try:
            repo = Jagare(path)
            ret = repo.merge(ref=ref, msg=msg, commit_msg=commit_msg,
                             no_ff=no_ff, _env=env)
            return ProcessResult(**ret)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def push(self, path, remote, ref, env):
        try:
            repo = Jagare(path)
            ret = repo.push(remote, ref, _env=env)
            return ProcessResult(**ret)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def archive(self, path, prefix, ref):
        try:
            repo = Jagare(path)
            # TODO: ref, fix ellen
            stdout = repo.archive(prefix=prefix)
            return stdout
        except Exception as e:
            raise ServiceUnavailable(repr(e))
