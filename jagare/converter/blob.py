# coding: utf-8

"""
struct Blob {
    1: required string type,  # 'blob'
    2: required string sha,
    3: required string data,
    4: required i64 size,
    5: required bool is_binary,  # binary is keyword?
}
"""

from jagare.converter.base import Converter, Blob


class BlobConverter(Converter):
    target_type = Blob

    def prepare(self):
        self.is_binary = self.replace('binary')
