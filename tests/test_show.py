# coding: utf-8

import os

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_show_commit(tmpdir):
    path = tmpdir.strpath
    temp_repo.create_temp_repo(path, is_bare=True)

    ret = Jagare.show(path, 'master')

    assert ret.commit
    assert ret.commit.sha


def test_show_tree(tmpdir):
    path = tmpdir.strpath
    repo = temp_repo.create_temp_repo(path, is_bare=True)

    # create a tree
    temp_repo.commit_something(path,
                               file_name=os.path.join('test_tree', 'file'))

    ls = repo.ls_tree('master')
    trees = [item['sha'] for item in ls if item['type'] == 'tree']
    assert trees

    for sha in trees:

        ret = Jagare.show(path, sha)

        assert ret.tree


def test_show_blob(tmpdir):
    path = tmpdir.strpath
    repo = temp_repo.create_temp_repo(path, is_bare=True)

    ls = repo.ls_tree('master')
    blobs = [item['sha'] for item in ls if item['type'] == 'blob']
    assert blobs

    for sha in blobs:

        ret = Jagare.show(path, sha)

        assert ret.blob


def test_show_tag(tmpdir):
    path = tmpdir.strpath
    repo = temp_repo.create_temp_repo(path, is_bare=True)

    # create a tag
    ret = repo.create_tag('test_tag', 'master', 'lh', 'lh@localhost', 'msg')
    assert ret is True

    tag_name = repo.tags[0]
    tag_ref = repo.lookup_reference('refs/tags/%s' % tag_name)
    sha = tag_ref.target.hex

    type_ = repo.resolve_type(sha)
    assert type_ == 'tag'

    ret = Jagare.show(path, sha)
    assert ret.tag.name == tag_name
