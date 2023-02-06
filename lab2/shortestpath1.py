import heapq

__author__ = "Gustav Elmqvist"

"""
    This program calculates the shortest path between the start node s and
    every other node. Then every query can easily be answered.

    The shortest path is calculted by using Dijkstra's algorithm.

    Time complexity  O((|E|+|V|)log|V|) where E are the edges and V the nodes.
    Space complexity O(|E|+|V|) in the average case.
"""


def parse_lines(x):
    """
    Read x lines and convert each line into a list of integers.
    """
    return [[*map(int, input().split())] for _ in range(x)]


def shortest_path(graph, s):
    """
    Calculate the shortest path from the start node s to all other nodes in
    graph. Return two dictionaries, one with distances and the other one with
    paths.
    """

    distances = {}
    previous = {}

    priority_queue = [(0, s)]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)

        if node in distances: continue

        distances[node] = dist

        for weight, neighbor in graph[node]:
            heapq.heappush(priority_queue, (dist + weight, neighbor))
            previous[neighbor] = node

    return distances, previous


if __name__ == "__main__":

    while (nmqs := [*map(int, input().split())]) != [0, 0, 0, 0]:
        n, m, q, s= nmqs

        edges = parse_lines(m)
        queries = parse_lines(q)

        # Adjacency list. It was not possible to use an adjacency matrix
        # because it exceeded the memory restriction of this exercise.
        graph = [[] for _ in range(n)]

        # Populate the graph
        for u, v, w in edges:
            graph[u].append((w, v))

        # Only the dist array is used here, but the prev array could be used
        # to get the shortest path from s to any other node.
        dist, prev = shortest_path(graph, s)
        
        # Answer all queries with the help of the distance array.
        result = []
        for q in queries:
            result.append(dist[q[0]] if q[0] in dist else 'Impossible')

        print(*result)