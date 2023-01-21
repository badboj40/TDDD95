import sys
import bisect

__author__ = "Gustav Elmqvist"

"""
    The solution uses dynamic programming and binary search to find the 
    longest increasing subsequence (LIS).

    T stores the current LIS and R is used to track which numbers are
    included in the solution.

    With binary search a postion is found where num should be inserted into T.

    Track the result and insert number at the right position. 

    When done, loop through the result list R backwards to find which numbers
    are included in the final solution and return the result.

    Kattis problem: https://liu.kattis.com/problems/longincsubseq
"""


def lis(sequence):
    """
    Return a list containing longest increasing subsequence of sequence.

    Time complexity: O(nlogn)
    """
    n = len(sequence)
    T = [0]
    R = [-1] * n
    for i, num in enumerate(sequence): # for loop O(n)

        # find the position in T where num should be inserted
        pos = bisect.bisect_left(T, num) # binary search O(logn)
        if pos > 0:
            # Track the result
            R[i] = T[pos-1]
        
        # add num to T at the right position
        if pos < len(T):
            T[pos] = num
        else:
            T.append(num)

    # go through R backwards, starting with the last number in T, to
    # find the solution.
    num = T[-1]
    result = []
    while n > 0: # while loop O(n)
        n -= 1
        if sequence[n] == num:
            result.append(n)
            num = R[n]
    return result[::-1]


if __name__ == "__main__":

	# This while loop will be executed once for each test case until there
	# is no more input.
	while sys.stdin.readline():

		sequence = [int(x) for x in sys.stdin.readline().split()]

		result = lis(sequence)

		print(len(result))
		print(' '.join(str(x) for x in result))