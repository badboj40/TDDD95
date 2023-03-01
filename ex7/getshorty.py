import heapq

__author__ = "Gustav Elmqvist"


"""
    Almost the same solution as shortest path 1.

"""

def solve(graph, n):

    sizes = {}

    priority_queue = [(-1, 0)]

    while priority_queue:
        size, node = heapq.heappop(priority_queue)

        if node in sizes: continue

        sizes[node] = size

        for f, neighbor in graph[node]:
            heapq.heappush(priority_queue, (size*f, neighbor))

    return -sizes[n-1]


while (nm := [*map(int, input().split())]) != [0, 0]:
    n, m = nm

    edges = [input().split() for _ in range(m)]

    # Adjacency list.
    graph = [[] for _ in range(n)]

    # Populate the graph
    for u, v, f in edges:
        graph[int(u)].append((float(f), int(v)))
        graph[int(v)].append((float(f), int(u)))

    size = solve(graph, n)
    print(f"{size:.4f}")