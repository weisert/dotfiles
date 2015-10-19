#!/usr/bin/env python
# Copyright (c) 2015 Igor Vayzert

import argparse
import datetime
import os
import re
import subprocess
import sys

HEADERS = ['// Copyright (c) {year} {company} LLC. All rights reserved.',
           '// Author: {name} <{mail}>']


def create_headers():
    data = {'year': str(datetime.date.today().year),
            'company': raw_input('Please enter your company: '),
            'name': subprocess.check_output(
                ['git', 'config', 'user.name']).strip(),
            'mail': subprocess.check_output(
                ['git', 'config', 'user.email']).strip()}
    result = []
    for line in HEADERS:
        result.append(line.format(**data))
    return result


def check_cwd():
    if os.path.basename(os.getcwd()) != 'src':
        print 'Your current directory must be \"src\".'
        return False
    return True


def parse_command_line_options(argv):
    parser = argparse.ArgumentParser(description='Create something in browser.')
    parser.add_argument('-w', '--what',metavar='WHAT', type=str.lower,
                        help='What to create: "class", "header", "source", "browsertest", "unittest"',
                        choices=['class', 'header', 'source', 'browsertest', 'unittest'])
    parser.add_argument('path', nargs='?', help='Full path.', default=None, type=str)
    if len(argv) == 0:
        parser.print_help()
    return parser.parse_args(argv)


def to_camel_case(string):
    def to_upper(patern):
        s = patern.group(1)
        if s.startswith('_'):
            return s[1:].upper()
        return s.upper()
    return re.sub(r'(^.|_.)', to_upper, string)


def create_cc_file_content(path, file):
    lines = create_headers()
    lines.append('')
    dir_name = os.path.dirname(path)
    lines.append('#include "' + dir_name + '/' + file + '.h"')
    lines.append('')
    return lines


def create_h_file_content(path, file):
    lines = create_headers()
    lines.append('')
    dir_name = os.path.dirname(path)
    guard = dir_name.replace('/', '_').upper() + '_' + file.upper() + '_H_'
    lines.append('#ifndef ' + guard)
    lines.append('#define ' + guard)
    lines.append('')
    class_name = to_camel_case(file)
    lines.append('class ' + class_name + '{')
    lines.append('')
    lines.append('};')
    lines.append('')
    lines.append('#endif  // ' + guard)
    lines.append('')
    return lines


def create_class(path):
    file = os.path.basename(path)
    if file.endswith('.h'):
        file.replace('.h', '')
    if file.endswith('.cc'):
        file.replace('.h', '')
    cc_file = os.path.join(os.getcwd(), os.path.dirname(path), file + '.cc')
    with open(cc_file, 'wb') as f:
        f.write('\n'.join(create_cc_file_content(path, file)))
    h_file = os.path.join(os.getcwd(), os.path.dirname(path), file + '.h')
    with open(h_file, 'wb') as f:
        f.write('\n'.join(create_h_file_content(path, file)))


def create_browser_test(path):
    lines = create_headers()
    lines.append('')
    included_file = path.replace('_browsertest.cc', '.h')
    lines.append('#include "' + included_file + '"')
    lines.append('')
    lines.append('#include "chrome/test/base/in_process_browser_test.h"')
    lines.append('')

    class_name = os.path.basename(included_file).replace('.h', '')
    class_name = to_camel_case(class_name) + 'Test'

    lines.append('class ' + class_name + ' : public InProcessBrowserTest {')
    lines.append('};')
    lines.append('')
    lines.append('IN_PROC_BROWSER_TEST_F(' + class_name +', Draft) {')
    lines.append('')
    lines.append('}')
    lines.append('')

    filename = os.path.join(os.getcwd(), path)
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))


def main(argv):
    if not check_cwd():
        return 1
    options = parse_command_line_options(argv[1:])
    if options.what == 'class':
        create_class(options.path)
    if options.what == 'browsertest':
        create_browser_test(options.path)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
