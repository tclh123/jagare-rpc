# coding: utf-8

import json

from ellen.repo import Jagare

from jagare.converter.gitobject import get_gitobject_from_show
from jagare.converter.process import ProcessResultConverter
from jagare.converter.diff import DiffConverter
from jagare.converter.commit import CommitConverter
from jagare.converter.blame import BlameConverter
from jagare.converter.merge import MergeResultConverter, MergeIndexConverter

from service_gen.jagare.ttypes import (Repository,
                                       ServiceUnavailable)

# Code provide jagare_client wrapper, save `path` arg.


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
            return list(repo.tags)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def show(self, path, ref):
        try:
            repo = Jagare(path)
            obj_dict = repo.show(ref)
            ret = get_gitobject_from_show(obj_dict)
            return ret
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def ls_tree(self, path, ref, req_path, recursive, with_size,
                with_commit, name_only):
        try:
            repo = Jagare(path)
            ret = repo.ls_tree(ref, path=req_path, recursive=recursive,
                               size=with_size, with_commit=with_commit,
                               name_only=name_only)
            return json.dumps(ret)
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def rev_list(self, path, to_ref, from_ref, file_path, skip, max_count,
                 author, query, first_parent, since, no_merges):
        try:
            repo = Jagare(path)
            commit_list = repo.rev_list(to_ref=to_ref, from_ref=from_ref,
                                        path=file_path, skip=skip,
                                        max_count=max_count, author=author,
                                        query=query, first_parent=first_parent,
                                        since=since, no_merges=no_merges)
            return [CommitConverter(**commit_dict).convert()
                    for commit_dict in commit_list]
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def blame(self, path, ref, req_path, lineno):
        try:
            repo = Jagare(path)
            ret = repo.blame(ref, path=req_path, lineno=lineno)
            return BlameConverter(**ret).convert()
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

    def diff(self, path, ref, from_ref, ignore_space, flags,
             context_lines, paths, rename_detection):
        try:
            repo = Jagare(path)
            diff_dict = repo.diff(ref, from_ref=from_ref,
                                  ignore_space=ignore_space, flags=flags,
                                  context_lines=context_lines, paths=paths,
                                  rename_detection=rename_detection)
            return DiffConverter(**diff_dict).convert()
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
            return ProcessResultConverter(**ret).convert()
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def merge_tree(self, path, ours, theirs):
        try:
            repo = Jagare(path)
            ret = repo.merge_tree(ours, theirs)
            return MergeIndexConverter(**ret).convert()
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def merge_head(self, path, ref):
        try:
            repo = Jagare(path)
            ret = repo.merge_head(ref)
            return MergeResultConverter(**ret).convert()
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def merge_commits(self, path, ours, theirs):
        try:
            repo = Jagare(path)
            ret = repo.merge_tree(ours, theirs)
            return MergeIndexConverter(**ret).convert()
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def push(self, path, remote, ref, env):
        try:
            repo = Jagare(path)
            ret = repo.push(remote, ref, _env=env)
            return ProcessResultConverter(**ret).convert()
        except Exception as e:
            raise ServiceUnavailable(repr(e))

    def archive(self, path, prefix, ref):
        try:
            repo = Jagare(path)
            stdout = repo.archive(prefix=prefix, ref=ref)
            return stdout
        except Exception as e:
            raise ServiceUnavailable(repr(e))
