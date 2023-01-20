import sys
m,n=map(int,input().split())
c=sorted(map(int,sys.stdin))
r,a=sum(c)-m,0
for w in c:g=min(w,r//n);a+=g*g;r-=g;n-=1
print(a)