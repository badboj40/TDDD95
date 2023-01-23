import sys,bisect
z=sys.stdin.readline
while z():
	s=list(map(int,z().split()));n=len(s);T=[0];R=[-1]*n
	for i in range(n):
		j=bisect.bisect_left(T,s[i])
		if j>0:R[i]=T[j-1]
		if j==len(T):T+=[s[i]]
		else:T[j]=s[i]
	p=T[-1];r=[];v=0
	for i in range(n-1, -1, -1):
		if s[i] == p:v+=1;r+=[str(i)];p = R[i]
	print(v,'\n'+' '.join(r[::-1]))