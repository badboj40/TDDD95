
__author__ = "Gustav Elmqvist"


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

    def flip(self, i: int) -> None:
        """
        Flip the a[i]'th bit.

        Time complexity: O(logn)
        """
        delta = 1 if self.sum(i+1)-self.sum(i) == 0 else -1

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


N, K = map(int, input().split())

fenwick = FenwickTree(N+1)

for _ in range(K):
    query = input()
    if query[0] == 'F':
        i = int(query.split()[1])
        fenwick.flip(i)

    elif query[0] == 'C':
        l, r = map(int, query.split()[1:])
        print(fenwick.sum(r+1)-fenwick.sum(l))