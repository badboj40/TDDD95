import sys

__author__ = "Gustav Elmqvist"


indata = [row for row in sys.stdin][1:]


def is_word(string):
	return '<' not in string


def solve(first, second):
	if len(first) != len(second): return '-'

	for i in range(len(first)):
		w1, w2 = first[i], second[i]
		if w1 != w2 and is_word(w1) and is_word(w2):
			return '-'

		if not is_word(w1) and is_word(w2):
			first[:] = [w if w != w1 else w2 for w in first]
		elif is_word(w1) and not is_word(w2):
			second[:] = [w if w != w2 else w1 for w in second]
	
	for i in range(len(first)):
		w1, w2 = first[i], second[i]
		if is_word(w1) != is_word(w2):
			return solve(first, second)
		
	return ' '.join(w if is_word(w) else 'x' for w in first)


for i in range(len(indata)//2):
	first = indata[2*i].split()
	second = indata[2*i+1].split()
	result = solve(first, second)
	print(result)