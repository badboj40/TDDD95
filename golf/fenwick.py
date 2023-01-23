import sys;x=int;N=x(input().split()[0]);t=[0]*(N+1)
def a(i,d):
	while i<=N:t[i]+=d;i+=i&-i
def s(i,c=0):
	while i:c+=t[i];i-=i&-i
	print(c)
[s(x(y))if o=='?'else a(x(y)+1,x(z[0]))for o,y,*z in(r.split()for r in sys.stdin)]