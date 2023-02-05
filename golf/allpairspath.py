z=float('inf');r=range
f=lambda x:[[*map(int,input().split())]for _ in r(x)]
while sum(g:=f(1)[0]):
 n,m,q=g;e=f(m);y=f(q);d=[n*[z]for _ in r(n)]
 for u,v,w in e:d[u][v]=min(d[u][v],w)
 for v in r(n):d[v][v]=0
 for k in r(n):
  for i in r(n):
   for j in r(n):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
 for i in r(n):
  for j in r(n):
   for k in r(n):
    if d[k][k]<0 and z>d[i][k]and d[k][j]<z:d[i][j]=-z
 print(*['Impossible'*(d[u][v]==z)or'-Infinity'*(d[u][v]==-z)or d[u][v]for u,v in y])