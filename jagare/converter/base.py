# coding: utf-8

from service_gen.jagare.ttypes import (ProcessResult,
                                       Signature,
                                       Commit,
                                       TreeEntry, Tree,
                                       Blob,
                                       Tag,
                                       GitObject,
                                       Blame, BlameHunk,
                                       Diff, Patch, Hunk, DiffLine)


class Converter(object):
    """convert ellen formatted dict into type defined in thrift"""
    target_type = type

    def __init__(self, **kw):
        self.__dict__.update(kw)

    def export(self):
        return self.__dict__

    def prepare(self):
        pass

    def replace(self, name):
        return self.__dict__.pop(name)

    def drop(self, name):
        del self.__dict__[name]

    def convert(self):
        self.prepare()
        return self.target_type(**self.export())
