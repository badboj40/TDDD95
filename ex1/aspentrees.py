import sys

__author__ = "Gustav Elmqvist"

"""
	The solution of the problem is a combination of a greedy approach and
	dynamic programming which makes the algorithm run in O(N^2) time where 
	N is the number of trees to be planted on each side.

	The greedy assumption is that each tree, in sorted order, should be
	put in the next free spot on either side.

	At first I tried to implement a recursive solution with caching, and
	although it completed the first Kattis tests, it was too slow to complete
	the longer tests.

	Then I change the approach to instead use a 2D dp array that contains the
	optimal distance so far of each tree placed. The indexes represent the
	amount of trees that has been placed so far on the left and right side
	respectively.

	The dp array is then populated with the base cases that trees only have been
	placed on one side.

	Lastly the whole dp array is filled with the optimal choice based on the
	previously calculated results.

	The result can be found in dp[N][N] which represents the minimum distance
	required to place N trees on the left side and N trees on the right side.
"""


N=int(input()) // 2
L, W = map(int,input().split())
trees = sorted(map(int,sys.stdin))
space_between_trees = L / (N-1)


def distance(tree_index, y, x):
	"""
	Return the distance between a tree and the (y,x) coordinates of a location.
	"""
	dy = trees[tree_index] - y * space_between_trees
	return (x*x + dy*dy) ** (1/2)


def aspentrees():
	"""
	Return the smallest total distance that the trees have to be moved in order
	for them to reach the desired position.

	Time complexity: O(N^2)
	Space complexity: O(N^2)
	"""

	# 2D dynamic programming array where each position represents the
	# minimum total distance required to reach that state.
	dp = [[0]*(N+1) for _ in range(N+1)]

	# The distances where trees only have been placed on the left side.
	for left in range(N):
		dp[left+1][0] = dp[left][0] + distance(left, left, 0)

	# The distances where trees only have been placed on the right side.
	for right in range(N):
		dp[0][right+1] = dp[0][right] + distance(right, right, W)

	# Go through and populate every state in the 2D dp array.
	for left in range(1,N+1):
		for right in range(1,N+1):

			# Update the current state based on the previous states.
			dp[left][right] = min(
				dp[left-1][right] + distance(left+right-1, left-1, 0),
				dp[left][right-1] + distance(left+right-1, right-1, W)
			)

	# The minimum total distance required to place N trees on both the left and
	# right side
	return dp[N][N]
	
print(aspentrees())