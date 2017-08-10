#!/usr/bin/env python

import sys
import re
import platform
import os


def main(argv):
    if len(argv) < 2 or len(argv) > 3 or len(argv) == 3 and argv[1] != '-r':
        print 'Usage: {} [-r] filename.cpp'.format(argv[0])
        return 1
    if not os.path.isfile(argv[-1]):
        print 'File: {} does not exist.'
        return 2
    with open(argv[-1], 'rb') as f:
        data = f.read()
    if platform.system() == 'Windows':
        line = 'LOG(ERROR) << "  -----------  " << __FUNCTION__;\n'
    else:
        line = 'LOG(ERROR) << "  -----------  " << __PRETTY_FUNCTION__;\n'

    with open(argv[-1], 'wb') as f:
        if argv[1] == '-r':
            # Remove inserted logs
            f.write(data.replace('{' + line, '{'))
        else:
            # Insert logs
            simple_function = R'\n[a-zA-Z0-9_]+\s+[a-zA-Z0-9_:]+\(([^)]+)?\) {'
            destructor = R'\n([a-zA-Z0-9_:]+)?~[a-zA-Z0-9_]+\(([^)]+)?\) {'
            constructor = R'\n[a-zA-Z0-9_:]+\(([^)]+)?\)\s+(:[^{]+)?{'
            func_re = re.compile('(' + simple_function +
                                 '|' + destructor +
                                 '|' + constructor + ')')

            last = 0
            for func in func_re.finditer(data):
                f.write(data[last:func.end()])
                f.write(line)
                last = func.end()
            f.write(data[last:])
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
