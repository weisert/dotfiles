#!/usr/bin/env python

import sys
import re
from tempfile import NamedTemporaryFile
import subprocess
import os.path
import platform

path = sys.argv[1]

def get_cmdline(left, right, ancestor, merged, left_title, right_title):
	#return ['opendiff', left, right, '-ancestor', ancestor, '-merge', merged]
	#return ['vim', '-o', left, right, ancestor, merged]
	platform_name = platform.platform()
	if platform_name.startswith('Windows'):
		binary = 'C:\\Program Files\\SourceGear\\Common\\DiffMerge\\sgdm.exe'
	elif platform_name.startswith('Darwin'):
		binary = '/Applications/DiffMerge.app/Contents/MacOS/DiffMerge'
	return [
		binary,
		'-caption={}'.format(os.path.basename(path)),
		'-result={}'.format(merged),
		#'-ro2',
		'-t1={}'.format(left_title),
		'-t2=common',
		'-t3={}'.format(right_title),
		left, ancestor, right
	]

def temp(prefix):
	platform_name = platform.platform()
	if platform_name.startswith('Windows'):
		delete_on_exit = False
	elif platform_name.startswith('Darwin'):
		delete_on_exit = True
	return NamedTemporaryFile(prefix='{}-'.format(prefix), delete=delete_on_exit)

RE_LEFT   = re.compile(r'^<<<<<<< (.+)$')
RE_COMMON = re.compile(r'^\|\|\|\|\|\|\| merged common ancestors$')
RE_RIGHT  = re.compile(r'^=======$')
RE_END    = re.compile(r'^>>>>>>> (.+)$')

marker_regexps = dict(left=RE_LEFT, common=RE_COMMON, right=RE_RIGHT, end=RE_END)

with open(path) as f:
	with temp(prefix='left') as l, temp(prefix='common') as c, temp(prefix='right') as r:
		conflicts_found = False
		left_title = None
		right_title = None

		dest = [l, r, c]
		for line in f:
			for kind, regexp in marker_regexps.items():
				match = regexp.match(line)
				if match:
					if kind == 'left':
						conflicts_found = True
						left_title = match.group(1)
						dest = [l]
					elif kind == 'right':
						dest = [r]
					elif kind == 'common':
						dest = [c]
					elif kind == 'end':
						right_title = match.group(1)
						dest = [l, r, c]
					break
			else:
				for d in dest: d.write(line)

		l.flush()
		c.flush()
		r.flush()
		f.close()

		if conflicts_found:
			cmdline = get_cmdline(l.name, r.name, c.name, path, left_title, right_title)
			print cmdline
			subprocess.check_call(cmdline)
		else:
			print 'no conflict markers found'

