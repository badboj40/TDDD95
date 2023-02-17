
__author__ = "Gustav Elmqvist"


class DSU:
    """
    Disjoint Set Union data structure implementation.
    """

    def __init__(self, N: int) -> None:
        self.parent = [*range(N)]
        self.sets = N

    def find(self, v: int) -> int:
        """
        Find the parent of the set that v is in.

        Time complexity: O(logn)
        """
        while v != self.parent[v]:
            v = self.parent[v]
        return v

    def union(self, a: int, b: int) -> None:
        """
        Merge the sets containing the elements a and b.

        Time complexity: O(logn)
        """
        a = self.find(a)
        b = self.find(b)
        self.parent[b] = a
        self.sets -= a != b


def primes_greater_than(x):
    MAX = 1001
    primes = []
    is_prime = [True] * (MAX)
    for i in range(2, MAX):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, MAX, i):
                is_prime[j] = False
    return [prime for prime in primes if prime >= x]


for test_case in range(int(input())):

    A, B, P = map(int, input().split())

    primes = primes_greater_than(P)

    dsu = DSU(B - A + 1)

    for prime in primes:
        
        number_classes = [n-A for n in range(A, B+1) if n%prime == 0]

        for n in number_classes[1:]:
            dsu.union(number_classes[0], n)

    print(f"Case #{test_case+1}: {dsu.sets}")
