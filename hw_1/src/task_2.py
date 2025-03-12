#!/usr/bin/env python3
import sys
from typing import TextIO



def print_tail(io: TextIO, line_count: int):
    io_lines = io.readlines()
    if not len(io_lines):
        return
    for line in io_lines[-line_count:]:
        print(line, end="")
    print()

def main() -> None:
    if len(sys.argv) == 1:
        print_tail(sys.stdin, line_count=17)
    else:
        for filename in sys.argv[1:]:
            print(f"==> {filename} <==")
            with open(filename, 'r') as file:
                print_tail(file, line_count=10)


if __name__ ==  '__main__':
    main()