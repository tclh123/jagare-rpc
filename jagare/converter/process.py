# coding: utf-8

"""
struct ProcessResult {
    1: required string stdout,
    2: required string stderr,
    3: required string fullcmd,
    4: optional i16 returncode,  # None if process hasn't terminated yet.
}
"""

from .base import Converter, ProcessResult


class ProcessResultConverter(Converter):
    target_type = ProcessResult
