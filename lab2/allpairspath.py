
__author__ = "Gustav Elmqvist"

"""
    This program calculates the shortest path between all nodes in the graph
    to make it faster to then answer all the queries.

    Time complexity  O(n^3) where n is the amount of nodes in the graph.
    Space complexity O(n^2) 
"""


def parse_lines(x):
    """
    Read x lines and convert each line into a list of integers.
    """
    return [[*map(int, input().split())] for _ in range(x)]


def shortest_path_all_pairs(edges, n):
    """
    Take a list of graph edges and return a 2d adjancency matrix.

    Time complexity: O(n^3)
    """

    # 2D adjacency matrix initialized to infinity.
    dist = [[float("inf")] * n for _ in range(n)]

    # Add all edges.
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)

    # All nodes have a distance 0 to themselves.
    for v in range(n):
        dist[v][v] = 0

    # Using the Floyd-Warshall algorithm.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Searching for any negative cycles with the following method:
    # dist[k][k] < 0 means that node k has a negative feedback loop to itself,
    # therefore all paths from i to j that pass through k will also have a negative loop.
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[k][k] < 0 and dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = -float("inf")

    return dist


if __name__ == "__main__":

    while (nmq := [*map(int, input().split())]) != [0, 0, 0]:
        n, m, q = nmq

        edges = parse_lines(m)
        queries = parse_lines(q)

        distances = shortest_path_all_pairs(edges, n)
        
        # Answer all queries with the help of the distances 2d array.
        result = []
        for u, v in queries:

            if distances[u][v] == float("inf"):
                result.append("Impossible")
            elif distances[u][v] == -float("inf"):
                result.append("-Infinity")
            else:
                result.append(distances[u][v])

        print(*result)