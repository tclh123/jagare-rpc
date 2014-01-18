# coding: utf-8

"""
struct MergeResult {
    1: required bool is_uptodate,
    2: required bool is_fastforward,
    3: required string fastforward_oid,
}

struct MergeIndex {
    1: required bool has_conflicts,
}
"""

from jagare.converter.base import Converter, MergeResult, MergeIndex


class MergeResultConverter(Converter):
    target_type = MergeResult


class MergeIndexConverter(Converter):
    target_type = MergeIndex
