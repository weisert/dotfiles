#!/usr/bin/env python

from subprocess import check_output, check_call

output = check_output(['git', 'ls-files', '-m'])
files = [x for x in output.split('\n') if x.endswith('BUILD.gn')]
for f in files:
    check_call(['gn', 'format', f])
