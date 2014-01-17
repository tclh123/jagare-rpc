# coding: utf-8

"""
struct DiffLine {
    1: required string attr,  # char
    2: required string line,
}
struct Hunk {
    1: required string old_start,
    2: required string new_start,
    3: required string old_lines,
    4: required string new_lines,
    5: required list<DiffLine> lines,  # hunk.lines,
}
struct Patch {
    1: required string amode,
    2: required string bmode,
    3: required string old_sha,  # commit from_sha
    4: required string new_sha,  # commit to_sha
    5: required i32 additions,
    6: required i32 deletions,
    7: required i32 similarity,
    8: required list<Hunk> hunks,
    9: required string old_oid,
    10: required string new_oid,
    11: required string status,  # char
    12: required bool is_binary,
    13: required string old_file_path,
    14: required string new_file_path,
}
struct Diff {
    1: required string old_sha,
    2: required string new_sha,
    3: required list<Patch> patches,
}
"""

from jagare.converter.base import Converter, Diff, Patch, Hunk, DiffLine


class DiffConverter(Converter):
    target_type = Diff

    def prepare(self):
        self.drop('diff')

        self.patches = [PatchConverter(**patch).convert()
                        for patch in self.patches]


class PatchConverter(Converter):
    target_type = Patch

    def prepare(self):
        self.is_binary = self.replace('binary')
        self.hunks = [HunkConverter(**hunk).convert()
                      for hunk in self.hunks]


class HunkConverter(Converter):
    target_type = Hunk

    def prepare(self):
        self.lines = [DiffLineConverter(line=line).convert()
                      for line in self.lines]


class DiffLineConverter(Converter):
    target_type = DiffLine

    def prepare(self):
        self.attr, self.line = self.line

        self.unicode_str('line')
