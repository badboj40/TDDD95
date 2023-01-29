import sys
from heapq import*
n=int(input());a=[*map(int,sys.stdin)]
q=[];r=[];d=[1]*(n+1)
for v in a:d[v-1]+=1
[heappush(q,i)for i in range(n)if d[i]<2]
for v in a:
 if q:
  u=heappop(q);r+=[u+1];d[u]-=1;d[v-1]-=1
  if d[v-1]==1:heappush(q,v-1)
if sum(d)>1:r=['Error']
print(*r)