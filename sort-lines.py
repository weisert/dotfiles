#!/usr/bin/env python
# Copyright (c) 2015 Igor Vayzert

import os
import sys
import argparse


def check_cwd():
    if os.path.basename(os.getcwd()) != 'src':
        print 'Your current directory must be \"src\".'
        return False
    return True


def parse_command_line_options(argv):
    parser = argparse.ArgumentParser(description='Create something in browser.')
    parser.add_argument('from_line', nargs='?', help='From line inclusive.', default=None, type=int)
    parser.add_argument('to_line', nargs='?', help='To line exclusive.', default=None, type=int)
    parser.add_argument('path', nargs='?', help='Full path.', default=None, type=str)
    if len(argv) == 0:
        parser.print_help()
    return parser.parse_args(argv)


def sort_headers(path, from_line, to_line):
    assert from_line < to_line
    assert from_line > 0
    assert to_line > 0
    from_line -= 1  # we count line from 1 in source files
    to_line -= 1  # we count line from 1 in source files
    full_path = os.path.join(os.getcwd(), path)
    with open(full_path, 'r') as f:
        lines = f.readlines()
    to_sort = lines[from_line:to_line]
    to_sort.sort()
    lines[from_line:to_line] = to_sort
    with open(full_path, 'w') as f:
        f.writelines(lines)


def main(argv):
    if not check_cwd():
        return 1
    options = parse_command_line_options(argv[1:])
    sort_headers(options.path, options.from_line, options.to_line)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
