import sys
from functools import lru_cache

__author__ = "Gustav Elmqvist"

@lru_cache
def solve(k, d, n):
    if not 0 <= d <= k: return 0
    if n == 1: return 1
    
    return solve(k,d+1,n-1) + solve(k,d,n-1) + solve(k,d-1,n-1)


for row in sys.stdin:
    k, n = map(int, row.split())

    result = 0
    total_combinations = (k+1)**n

    if n == 1:
        result += k + 1
    else:
        for d in range(k+1):
            result += solve(k, d, n)

    print(100*result/total_combinations)