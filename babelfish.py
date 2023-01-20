# https://liu.kattis.com/problems/babelfish

import sys

indata = [line.strip() for line in sys.stdin]

i = indata.index('')
translation = [line.split() for line in indata[:i]]
words = indata[i+1:]

d = {line[1] : line[0] for line in translation}

for word in words:
	print(d[word] if word in d else 'eh')	