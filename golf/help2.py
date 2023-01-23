z=input;e=enumerate;f=lambda x:x[0]!='<'
def s(a,b):
	for i,x in e(a):
		y=b[i]
		if x!=y and f(x)and f(y):return'-'
		if'<'in x and f(y):a=[w if w!=x else y for w in a]
		if f(x)and'<'in y:b=[w if w!=y else x for w in b]
	return s(a,b)if any(f(z)!=f(b[i])for i,z in e(a))else' '.join(w if f(w)else'x'for w in a)
for _ in range(int(z())):print(s(z().split(),z().split()))