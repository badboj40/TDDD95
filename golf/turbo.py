import sys;N=int(input())
d={int(x):i+1 for i,x in enumerate(sys.stdin)}
a=[0]*(N+1);i=1;j=N
def u(i):
 while i<=N:a[i]+=1;i+=i&-i
def s(i):
 r=i
 while i:r-=a[i];i-=i&-i
 return r
while i<=j:
 print(s(d[i])-1);u(d[i])
 if i<j:print(s(N)-s(d[j]));u(d[j])
 i+=1;j-=1