import sys
from heapq import heappush, heappop

__author__ = "Gustav Elmqvist"

"""
    This problem is about Prüfer sequences and the solution is based on
    the pseudo code from the Prüfer sequence wikipedia page:

    https://en.wikipedia.org//wiki/Pr%C3%BCfer_sequence

    If the number of leaves doesn't get to big the time complexity is about
    O(n) but worst case with a big heapq of leaves is probably O(nlogn).
"""

def chopwood(n, sequence):
    leaves = []
    degree = [1] * (n+1)

    for node in sequence:
        degree[node-1] += 1

    for i in range(n):
        if degree[i] == 1:
            heappush(leaves, i)

    result = []
    for node in sequence:
        if not leaves: break

        leaf = heappop(leaves)
        result.append(leaf+1)

        degree[leaf] -= 1
        degree[node-1] -= 1

        if degree[node-1] == 1:
            heappush(leaves, node-1)

    if sum(degree) > 1:
        result = ['Error']

    return result


if __name__ == "__main__":
    n = int(input())
    sequence = [*map(int, sys.stdin)]
    result = chopwood(n, sequence)
    print(*result)