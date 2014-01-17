# coding: utf-8

"""
struct Tag {
    1: required string type,  # 'tag'
    2: required string sha,
    3: required string name,
    4: required string target,  # tag.target.sha
    5: required Signature tagger,
    6: required string message,
    7: required string body,
}
"""

from jagare.converter.base import Converter, Tag
from jagare.converter.signature import SignatureConverter


class TagConverter(Converter):
    target_type = Tag

    def prepare(self):
        self.tagger = SignatureConverter(**self.tagger).convert()

        self.drop('tag')

        self.unicode_str('message')
        self.unicode_str('body')
