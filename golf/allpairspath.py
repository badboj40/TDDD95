z=float('inf')
f=lambda x:[[*map(int,input().split())]for _ in[1]*x]
while sum(g:=f(1)[0]):
 n,m,q=g;r=range(n);d=[n*[z]for _ in r]
 for u,v,w in f(m):d[u][v]=min(d[u][v],w)
 for v in r:d[v][v]=0
 for k in r:
  for i in r:
   for j in r:d[i][j]=min(d[i][j],d[i][k]+d[k][j])
 for i in r:
  for j in r:
   for k in r:
    if d[k][k]<0 and z>d[i][k]and d[k][j]<z:d[i][j]=-z
 print(*['Impossible'*(d[u][v]==z)or'-Infinity'*(d[u][v]==-z)or d[u][v]for u,v in f(q)])