# coding: utf-8

"""
struct Commit {
    1: required string type,  # 'commit'
    2: required string sha,
    3: required list<string> parents,  # shas
    4: required string tree,  # sha of the tree object attached to the commit
    5: required Signature committer,
    6: required Signature author,
    7: required string email,
    8: required i64 time,
    9: required i16 offset,
    10: required string commit,
    11: required string message,
    12: required string body,  # commit message body
}
"""

from jagare.converter.base import Converter, Commit
from jagare.converter.signature import SignatureConverter


class CommitConverter(Converter):
    target_type = Commit

    def prepare(self):
        self.drop('parent')

        self.type = 'commit'
        self.committer = SignatureConverter(**self.committer).convert()
        self.author = SignatureConverter(**self.author).convert()
