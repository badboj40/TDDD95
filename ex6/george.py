import heapq

__author__ = "Gustav Elmqvist"


N, M = map(int, input().split())
start, goal, dt, G = map(int, input().split())
georges_path = [*map(int, input().split())]

# Initialize the graph.
graph = [{} for _ in range(N+1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u][v] = d
    graph[v][u] = d

# Create a dict containing the blocked roads and the times they are blocked.
t = -dt
blocked = {}
for i in range(G-1):
    u, v = georges_path[i:i+2]
    blocked[(u, v)] = t
    blocked[(v, u)] = t
    t += graph[u][v]

distances = {}
priority_queue = [(1, start)]

# Find the shortest path to the goal, including wait times for blocked streets.
while priority_queue:
    t, u = heapq.heappop(priority_queue)

    if u in distances: continue

    distances[u] = t

    for v, d in graph[u].items():

        # If the street is blocked, wait until it is available again.
        if (u,v) in blocked and t >= blocked[(u,v)]:
            time_to_v = max(t, blocked[(u,v)]+d) + d
        else:
            time_to_v = t + d

        heapq.heappush(priority_queue, (time_to_v, v))

print(distances[goal])