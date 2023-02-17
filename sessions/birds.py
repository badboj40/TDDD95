
__author__ = "Gustav Elmqvist"


def solve(l, d, birds):
    if l < 12: return 0
    result = 0
    for i in range(len(birds)-1):
        free_space = (birds[i+1]-birds[i]) // d - 1
        result += max(free_space, 0)
    return result


l, d, n = map(int, input().split())
birds = sorted([6-d, l-6+d] + [int(input()) for _ in range(n)])

result = solve(l, d, birds)
print(result)
