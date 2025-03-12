#!/usr/bin/env python3
import os
import sys
from dataclasses import dataclass
from typing import TextIO


@dataclass
class WcStatistics:
    line_count: int
    word_count: int
    byte_count: int


def get_statistics(io: TextIO) -> WcStatistics:
    text = io.read()
    line_count = text.count(os.linesep)
    word_count = len(text.split())
    byte_count = len(text.encode("utf-8"))
    return WcStatistics(line_count, word_count, byte_count)


def print_statistics(statistics: WcStatistics, name=None, end_by_new_line=True) -> None:
    end_separator = "\n" if end_by_new_line else ""
    if name is None:
        print(f"\t{statistics.line_count}\t{statistics.word_count}\t{statistics.byte_count}", end=end_separator)
    else:
        print(f"\t{statistics.line_count}\t{statistics.word_count}\t{statistics.byte_count} {name}", end=end_separator)


def main() -> None:
    if len(sys.argv) == 1:
        statistics = get_statistics(sys.stdin)
        print_statistics(statistics)
    if len(sys.argv) > 1:
        total_statistics = WcStatistics(0, 0, 0)
        for index, filename in enumerate(sys.argv[1:]):
            end_by_new_line = True
            if index == len(sys.argv) - 2 and len(sys.argv) <= 2:
                end_by_new_line = False
            with open(filename, "r") as file:
                file_statistics = get_statistics(file)
                print_statistics(file_statistics, filename, end_by_new_line=end_by_new_line)
                total_statistics.line_count += file_statistics.line_count
                total_statistics.word_count += file_statistics.word_count
                total_statistics.byte_count += file_statistics.byte_count
        if len(sys.argv) > 2:
            print_statistics(total_statistics, "total", end_by_new_line=False)


if __name__ == '__main__':
    main()
