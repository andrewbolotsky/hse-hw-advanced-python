#!/usr/bin/env python3
import sys
from typing import TextIO


def print_enumerated_lines(io: TextIO) -> None:
    for index, line in enumerate(io):
        print("\t", index + 1, line, sep="\t", end="")


def main() -> None:
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            print_enumerated_lines(file)
    elif len(sys.argv) == 1:
        print_enumerated_lines(sys.stdin)
    else:
        print('usage: task_1.py [file]')


if __name__ == '__main__':
    main()
