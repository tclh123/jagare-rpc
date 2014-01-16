# coding: utf-8

"""
struct BlameHunk {
    1: required i32 lines_in_hunk,
    2: required string final_commit_id,
    3: required i32 final_start_line_number,
    4: required Signature final_committer,
    5: required string orig_commit_id,
    6: required string orig_path,
    7: required i32 orig_start_line_number,
    # 2: required Signature orig_committer,  #  orig_committer is None
    8: required string boundary,  # Tracked to a boundary commit.
}

struct Blame {
    1: required Blob blob,
    2: required list<BlameHunk> hunks,
}
"""

from jagare.converter.base import Converter, Blame, BlameHunk
from jagare.converter.signature import SignatureConverter
from jagare.converter.blob import BlobConverter


class BlameConverter(Converter):
    target_type = Blame

    def prepare(self):
        self.blob = BlobConverter(**self.blob).convert()
        self.hunks = [BlameHunkConverter(**hunk).convert()
                      for hunk in self.hunks]


class BlameHunkConverter(Converter):
    target_type = BlameHunk

    def prepare(self):
        self.final_committer = (SignatureConverter(**self.final_committer)
                                .convert())
