from heapq import*;import math;z=float('inf')
f=lambda x:[[*map(int,input().split())]for _ in[1]*x]
while sum(i:=f(1)[0]):
 n,m,q,s=i;g=[[]for _ in[1]*n];d={};Q=[(0,s)]
 for u,*e in f(m):g[u]+=[e]
 while Q:
  c,u=heappop(Q)
  if u not in d:d[u]=c;[heappush(Q,(t+math.ceil(max(0,c-t)/max(1,P))*P+d,v))for v,t,P,d in g[u]if P>0or c<=t]
 print(*[d[p[0]]if p[0]in d else'Impossible'for p in f(q)])