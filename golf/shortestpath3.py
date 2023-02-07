from heapq import*;z=float('inf')
f=lambda x:[[*map(int,input().split())]for _ in[1]*x]
while sum(i:=f(1)[0]):
 n,m,q,s=i;g=[[]for _ in[1]*n];d=[z]*n;d[s]=0;e=f(m)
 for _ in[1]*n:
  for u,v,w in e:d[v]=min(d[v],d[u]+w)
 c=1
 while c:
  c=0
  for u,v,w in e:
   if-z!=d[v]and-z==d[u]or d[u]+w<d[v]:d[v]=-z;c=1
 print(*['Impossible'*(d[p[0]]==z)or'-Infinity'*(d[p[0]]==-z)or d[p[0]]for p in f(q)]) 