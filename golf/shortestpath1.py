from heapq import*;z=float('inf')
f=lambda x:[[*map(int,input().split())]for _ in[1]*x]
while sum(i:=[*map(int,input().split())]):
 n,m,q,s=i;g=[[]for _ in[1]*n];d={};Q=[(0,s)]
 for u,v,w in f(m):g[u]+=[(w,v)]
 while Q:
  c,u=heappop(Q)
  if u not in d:d[u]=c;[heappush(Q,(c+w,v))for w,v in g[u]]
 print(*[d[p[0]]if p[0]in d else'Impossible'for p in f(q)])