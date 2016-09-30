#!/usr/bin/env python

import sys
from subprocess import check_output, check_call


def format_gn_file(filename):
    check_call(['gn', 'format', filename])


def get_modified_gn_files():
    output = check_output(['git', 'ls-files', '-m'])
    return [x for x in output.split('\n') if x.endswith('BUILD.gn')]


def get_all_gn_files():
    output = check_output(['git', 'ls-files'])
    return [x for x in output.split('\n') if x.endswith('BUILD.gn')]


if len(sys.argv) == 1:
    files = get_modified_gn_files()
elif len(sys.argv) == 2 and sys.argv[1] == 'all':
    files = get_all_gn_files()
else:
    print 'Usage: ' + sys.argv[0] + '[all]'
    exit(1)

for f in files:
    format_gn_file(f)
