import sys
x=[r.strip()for r in sys.stdin]
i=x.index('')
d={k:v for v,k in[r.split()for r in x[:i]]}
[print(d[w]if w in d else'eh')for w in x[i+1:]]