# coding: utf-8

"""
struct GitObject {
    1: required string type,
    2: optional Blob blob,
    3: optional Tree tree,
    4: optional Commit commit,
    5: optional Tag tag,
}
"""

from .base import GitObject
from .blob import BlobConverter
from .tree import TreeConverter
from .commit import CommitConverter
from .tag import TagConverter


def get_gitobject_from_show(formatted_dict):
    # FIXME: hack
    if not formatted_dict:
        return GitObject(type='')

    type_ = formatted_dict.get('type', 'commit')
    converter = {
        'blob': BlobConverter,
        'tree': TreeConverter,
        'commit': CommitConverter,
        'tag': TagConverter,
    }[type_]

    kw = {
        'type': type_,
        type_: converter(**formatted_dict).convert(),
    }
    return GitObject(**kw)
