
__author__ = "Gustav Elmqvist"


def prim(graph, n):
    """
    Return the total weight of the graph's minimum spanning tree using prim's
    algorithm.

    Time complexity: O(n^2)
    """
    selected = set()
    shortest_edge = [0] + [float('inf')] * n

    total_weight = 0

    for _ in range(n):
        v = -1
        for i in range(n):
            if i not in selected and shortest_edge[i] < shortest_edge[v]:
                v = i
        
        selected.add(v)
        total_weight += shortest_edge[v]

        for i in range(n):
            if graph[v][i] < shortest_edge[i]:
                shortest_edge[i] = graph[v][i]

    return total_weight


def dist(i, j, points):
    dx = points[i][0] - points[j][0]
    dy = points[i][1] - points[j][1]
    return (dx**2 + dy**2) ** 0.5


for _ in range(int(input())):
    n = int(input())
    islands = [tuple(map(float, input().split())) for _ in range(n)]

    graph = [[dist(i,j,islands) for i in range(n)] for j in range(n)]

    total_weight = prim(graph, n)

    print(total_weight)