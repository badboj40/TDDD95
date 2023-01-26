import sys;a=range
N=int(input())//2
L,W=map(int,input().split())
z=sorted(map(int,sys.stdin))
d=lambda t,y,x=0:(x*x+(z[t]-y*L/(N-1))**2)**.5
dp=[[0]*(N+1)for _ in a(N+1)]
for l in a(N):dp[l+1][0]=dp[l][0]+d(l,l)
for r in a(N):dp[0][r+1]=dp[0][r]+d(r,r,W)
for k in a(N*N):l=k//N;r=k%N;dp[l+1][r+1]=min(dp[l][r+1]+d(l+r+1,l),dp[l+1][r]+d(l+r+1,r,W))
print(dp[N][N])