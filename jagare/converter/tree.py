# coding: utf-8

"""
struct TreeEntry {
    1: required string type,  # in ('commit', 'blob', 'tree')
    2: required string sha,
    3: required string mode,
    4: required string path,  # entry.name
}

struct Tree {
    1: required string type,  # 'tree'
    2: required list<TreeEntry> entries,
}
"""

from .base import Converter, Tree, TreeEntry


class TreeConverter(Converter):
    target_type = Tree

    def prepare(self):
        self.entries = [TreeEntryConverter(**entry).convert()
                        for entry in self.entries]


class TreeEntryConverter(Converter):
    target_type = TreeEntry
