# coding: utf-8

"""
struct Signature {
    1: required string name,
    2: required string email,
    3: required i64 time,
    4: required i16 offset,  # Offset from UTC in minutes.
}
"""

from jagare.converter.base import Converter, Signature


class SignatureConverter(Converter):
    target_type = Signature
