import sys;r=[];*p,=range(int(input().split()[0]))
def f(v):
	v=int(v)
	if v!=p[v]:p[v]=f(p[v])
	return p[v]
for l in sys.stdin:
	o,a,b=l.split()
	if o=='=':p[f(b)]=f(a)
	else:r+=['yes'if f(a)==f(b)else'no']
print('\n'.join(r))