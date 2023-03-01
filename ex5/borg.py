from collections import deque

__author__ = "Gustav Elmqvist"


"""
    This program calculate the minimum total distance that the Borg have to
    travel in order to find the aliens in the maze. 
    

    Solution:

    1.  Create a complete graph with the position of borg and aliens as nodes
        and the distance between them as edges.

    2.  Create a minimum spanning tree of the graph.

    3.  The answer is the total length of the miminum spanning tree.

"""

class DSU:
	"""
	Disjoint Set Union data structure implementation.
	"""

	def __init__(self, N: int) -> None:
		self.parent = [n for n in range(N)]

	def find(self, v: int) -> int:
		"""
		Find the parent of the set that v is in.

		Time complexity: O(logn)
		"""
		if v == self.parent[v]:
			return v
		self.parent[v] = self.find(self.parent[v])
		return self.parent[v]

	def union(self, a: int, b: int) -> None:
		"""
		Merge the sets containing the elements a and b.

		Time complexity: O(logn)
		"""
		self.parent[self.find(b)] = self.find(a)

	def same(self, a: int, b: int) -> bool:
		"""
		Test whether a and b are in the same set.

		Time complexity: O(logn)
		"""
		return self.find(a) == self.find(b)


def mst(graph, n):
    """
    Return the graph's minimum spanning tree if there is one, else return
    an empty list.

    Time complexity: O(|E|*(logn + log|E|))
    """

    tree = set()
    dsu = DSU(n)

    # Kruskals algorithm
    for w, u, v in sorted(graph):
        if not dsu.same(u, v):
            tree.add((w, min(u, v), max(u, v)))
            dsu.union(u, v)

    return sorted(tree) if len(tree) == n-1 else []


def BFS(grid, nodes, start_node):
    global pops
    q = deque([(0,*start_node)])
    distances = {start_node: 0}
    while q:
        pops += 1
        d,y,x = q.popleft()

        if grid[y][x] == '#': continue

        neighbors = [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]

        for ny,nx in neighbors:
            if (ny,nx) not in distances:
                distances[(ny,nx)] = d+1
                q.append((d+1,ny,nx))

    edges = [(distances[goal],goal) for goal in nodes if goal!=start_node]

    return edges

import time
t0=time.time()

for _ in range(int(input())):
    W, H = map(int, input().split())

    grid = [list(input()) for _ in range(H)]

    nodes = [(y,x) for y in range(H) for x in range(W) if grid[y][x] in 'AS']
    node_indexes = {node:i for i,node in enumerate(nodes)}

    pops = 0
    graph = set()
    for i,node in enumerate(nodes):
        for w, goal in BFS(grid, nodes, node):
            j = node_indexes[goal]
            graph.add((w, min(i,j), max(i,j)))
            
    tree = mst(graph, len(nodes))

    print("pops",pops)
    print(sum(w for w,u,v in tree))

print(time.time()-t0)