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

from jagare.converter.base import GitObject
from jagare.converter.blob import BlobConverter
from jagare.converter.tree import TreeConverter
from jagare.converter.commit import CommitConverter
from jagare.converter.tag import TagConverter


def get_gitobject_from_show(formatted_dict):
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
