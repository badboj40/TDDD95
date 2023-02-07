import heapq

__author__ = "Gustav Elmqvist"

"""
    This program calculates the shortest path between the start node s and
    every other node. Then every query can easily be answered. Negative edges
    are allowed.

    The shortest path is calculted by using the Bellman-Ford algorithm.

    Time complexity  O(|E||V|) where E are the edges and V the nodes.
    Space complexity O(|E|+|V|) in the average case.
"""


def parse_lines(x):
    """
    Read x lines and convert each line into a list of integers.
    """
    return [[*map(int, input().split())] for _ in range(x)]


def shortest_path(graph, s, n):
    """
    Calculate the shortest path from the start node s to all other nodes in
    graph. Return two dictionaries, one with distances and the other one with
    paths.
    """

    dist = [float('inf')] * n
    dist[s] = 0

    previous = [None] * n


    # Bellman-Ford
    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                previous[v] = u

    # Detect negative cycles
    found_negative_cycle = True
    while found_negative_cycle:
        found_negative_cycle = False
        for u, v, w in graph:
            if dist[v] != -float('inf') and dist[u] == -float('inf') or dist[u] + w < dist[v]:
                dist[v] = -float('inf')
                found_negative_cycle = True
    
    return dist, previous


if __name__ == "__main__":

    while (nmqs := [*map(int, input().split())]) != [0, 0, 0, 0]:
        n, m, q, s= nmqs

        edges = parse_lines(m)
        queries = parse_lines(q)

        # Only the dist array is used here, but the prev array could be used
        # to get the shortest path from s to any other node.
        dist, prev = shortest_path(edges, s, n)
        
        # Answer all queries with the help of the distance array.
        result = []
        # for q in queries:
        #     result.append(dist[q[0]] if q[0] in dist else 'Impossible')
        for q in queries:

            if dist[q[0]] == float("inf"):
                result.append("Impossible")
            elif dist[q[0]] == -float("inf"):
                result.append("-Infinity")
            else:
                result.append(dist[q[0]])

        print(*result)