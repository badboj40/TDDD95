
__author__ = "Gustav Elmqvist"

def spiderman(distances):
	"""
	Return the optimal climbing path for spiderman, for example UUDDUDDDUDUDD.

	If there is no valid climbing path IMPOSSIBLE is returned.

	Time complexity: O(M*S) where M = len(distances) and S = sum(distances).
	"""

	M = len(distances) # Total amount of steps.
	S = sum(distances) # The highest possible height that can be reached.

	# There has to be at least two steps and they need to have an even sum.
	if M < 2 or S%2 != 0:
		return 'IMPOSSIBLE'

	# Dynamic Programming 2D array containing the lowest height required to 
	# reach the current step and also the steps previously taken (U/D).
	#
	# dp[index][height] = best previous height and path
	dp = [[(S,'')] * S for _ in range(M)]

	dp[0][distances[0]] = (distances[0], 'U')

	for i in range(1, M):
		for height in range(S):

			previous = dp[i-1][height]
			down = height - distances[i]
			up = height + distances[i]

			if down >= 0 and previous[0] < dp[i][down][0]:
				dp[i][down] = (previous[0], previous[1]+'D')

			if max(up, previous[0]) < S and max(up, previous[0]) < dp[i][up][0]:
				dp[i][up] = (max(up, previous[0]), previous[1]+'U')

	return dp[-1][0][1] or 'IMPOSSIBLE'


if __name__ == '__main__':
	N = int(input())
	for i in range(N):
		M = input()
		distances = [*map(int, input().split())]
		print(spiderman(distances))