
__author__ = "Gustav Elmqist"

"""
	This program solves the 0-1 knapsack problem using dynamic programming.

	To solve this kattis problem (using python) within the time limit of 
	2.00 seconds a lot of optimizations had to be made. For example using
	sys.stdin.readline() instead of input(), because it was a few percent
	faster.

	link to the problem: https://liu.kattis.com/problems/knapsack
"""

import sys


def get_pair() -> tuple[int,...]:
	"""
	Read a line of input and split it into a integer tuple
	"""
	return tuple(int(x) for x in sys.stdin.readline().split())


def knapsack(capacity, n, values, weights):
	"""
	Solve the 0-1 knapsack problem with dynamic programming.

	Time complexity: O(capacity * n)
	Space complexity: O(capacity * n)
	"""

	# Item table with space complexity O(capacity * n)
	table = [[0]*(capacity+1)for _ in range(n+1)]

	# Nested for loops with time complexity O(n * capacity).
	for i in range(n):
		for w in range(1, capacity+1):

			if weights[i] <= w:
				# Choose to include the item if it's the optimal choice.
				table[i+1][w] = max(
					table[i][w-weights[i]] + values[i],
					table[i][w]
				)
			else:
				# the item is too heavy, so it is not included. 
				table[i+1][w] = table[i][w] 

	# Looping through the table backwards in time O(n) to get the result.
	# Each time the value changes we know that the item at that index has
	# been included.
	result = []
	while n > 0:
		if table[n][capacity] > table[n-1][capacity]:
			result += [n-1]
			capacity -= weights[n-1]
		n -= 1
	return result[::-1]


if __name__ == "__main__":

	# This while loop will be executed once for each test case until there
	# is no more user input.
	while (pair := get_pair()):

		# Split up the input pair.
		capacity, n = pair

		# Get n values and weights from the test case.
		values, weights = zip(*[get_pair() for _ in range(n)])

		result = knapsack(capacity, n, values, weights)

		print(len(result))
		print(' '.join(str(x) for x in result))