import sys

__author__ = "Gustav Elmqvist"

"""
	An implementation of a data structure to solve the Union-Find problem.
	From the start there are N different sets, but they are later joined
	together with the union function. Because the find function squashes
	the parent relationship graph with each call the time complexity is
	logarithmic.

	Kattis problem: https://liu.kattis.com/problems/unionfind
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


if __name__ == "__main__":
	N, Q = [int(x) for x in input().split()]
	dsu = DSU(N)
	result = []
	for row in sys.stdin:
		operator, a, b = row.split()
		if operator == '=':
			dsu.union(int(a), int(b))
		else:
			result.append('yes' if dsu.same(int(a), int(b)) else 'no')
	print('\n'.join(result))