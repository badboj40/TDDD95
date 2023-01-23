import sys
r=range;f=lambda:[*map(int,sys.stdin.readline().split())]
def k(p):
	C,n=p;y="";s=0;v,c=zip(*[f()for _ in r(n)]);t=[[0]*(C+1)for _ in r(n+1)]
	for i in r(n):
		for w in r(1,C+1):t[i+1][w]=max(t[i][w-c[i]]+v[i],t[i][w])if w>=c[i]else t[i][w]
	while n:
		n-=1
		if t[n+1][C]>t[n][C]:y=f"{n} "+y;s+=1;C-=c[n]
	print(s,'\n'+y)
while(p:=f()):k(p)