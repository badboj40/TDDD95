f=input;r=range
for _ in[1]*int(f()):
	M=int(f());d=[*map(int,f().split())];S=999;t=[[(S,'')]*S for _ in r(M)];t[0][d[0]]=d[0],'U'
	for k in r(S,M*S):
		i=k//S;y=k%S;s=d[i];c,p=t[i-1][y];m=max(c,y+s)
		if y>=s and c<t[i][y-s][0]:t[i][y-s]=c,p+'D'
		if m<S and m<t[i][y+s][0]:t[i][y+s]=m,p+'U'
	print(t[-1][0][1]or'IMPOSSIBLE')