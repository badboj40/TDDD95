import sys

__author__ = "Gustav Elmqvist"

"""
	A Fenwick Tree data structure that can handle incrementation of array
	elements and queries about the prefix sum in a part of the array. Both
	of these operations are done in logarithmic time.
	
	Kattis problem: https://liu.kattis.com/problems/fenwick
"""

class FenwickTree:
	"""
	Implementation of the Fenwick Tree (Binary Indexed Tree) data structure.
	"""

	def __init__(self, N) -> None:
		self.N = N+1
		self.a = [0] * (N+1)
	
	def __g(self, i: int) -> int:
		"""
		Return the rightmost non zero bit in i.
		"""
		return i & -i

	def add(self, i: int, delta: int) -> None:
		"""
		Increase a[i] with delta.

		Time complexity: O(logn)
		"""
		i += 1
		while i < self.N:
			self.a[i] += delta
			i += self.__g(i)

	def sum(self, end: int) -> int:
		"""
		Compute the sum of the first numbers up to a[end] inclusive.

		Time complexity: O(logn)
		"""
		cumsum = 0
		while end > 0:
			cumsum += self.a[end]
			end -= self.__g(end)
		return cumsum


if __name__ == "__main__":
	N, Q = [int(x) for x in input().split()]
	fenwick_tree = FenwickTree(N)
	result = []
	for row in sys.stdin:
		row = row.split()
		if row[0] == '+':
			fenwick_tree.add(int(row[1]), int(row[2]))
		else:
			cumsum = fenwick_tree.sum(int(row[1]))
			result += [str(cumsum)]
	print('\n'.join(result))