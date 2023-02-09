
__author__ = "Gustav Elmqvist"

"""
    This program generatest a minimum spanning tree using Kruskal's algorithm
    with a Disjoint Set Union data structure.


    Time complexity O(nlogn) 
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
		a = self.find(a)
		b = self.find(b)
		if a != b:
			self.parent[b] = a

	def same(self, a: int, b: int) -> bool:
		"""
		Test whether a and b are in the same set.

		Time complexity: O(logn)
		"""
		return self.find(a) == self.find(b)


def parse_lines(x):
    """
    Read x lines and convert each line into a list of integers.
    """
    return [[*map(int, input().split())] for _ in range(x)]


def mst(graph, n):
    """
    Return the graph's minimum spanning tree if there is one, else return
    an empty list.

    Time complexity: O(|E|*(logn + log|E|))
    """

    tree = set()
    dsu = DSU(n)

    # Kruskals algorithm
    for w, u, v in graph:
        if not dsu.same(u, v):
            tree.add((min(u, v), max(u, v), w))
            dsu.union(u, v)

    return sorted(tree) if len(tree) == n-1 else []


if __name__ == "__main__":

    while (nm := parse_lines(1)[0]) != [0, 0]:
        n, m = nm

        edges = parse_lines(m)

        graph = sorted((w, u, v) for u, v, w in edges)
        tree = mst(graph, n)

        if tree:
            print(sum(w for u,v,w in tree))
            for u,v,w in tree:
                print(u, v)
        else:
            print('Impossible')