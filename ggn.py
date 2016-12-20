#!/usr/bin/env python
import os

if os.path.basename(os.getcwd()) != 'src':
    print 'Your current directory must be \'src\'.'
    exit(1)

gn_paths = [os.path.join(os.getcwd(), 'out', 'debug_gn'), os.path.join(os.getcwd(), 'out', 'release_gn')]

for p in gn_paths:
    if not os.path.exists(p):
        os.makedirs(p, 0755)
    with open(os.path.join(p, 'args.gn'), 'w') as f:
        f.write('dcheck_always_on = true\n')
        f.write('is_component_build = true\n')
        f.write('enable_nacl = false\n')
        if os.path.basename(p) == 'debug_gn':
            f.write('is_debug = true\n')
        else:
            f.write('is_debug = false\n')
