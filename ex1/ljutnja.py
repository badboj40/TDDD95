import sys
import heapq

__author__ = "Gustav Elmqvist"


indata = [row for row in sys.stdin]

candy, N = [int(x) for x in indata[0].split()]
children = {0:0}
for child in [int(x) for x in indata[1:]]:
	children[child] = children.get(child, 0) + 1

heap = []

for child in children:
	heapq.heappush(heap, -child)

while candy > 0:

	biggest = -heapq.heappop(heap)
	n = children.pop(biggest)
	big = -heap[0]
	diff = biggest - big

	if n*diff <= candy:
		candy -= n*diff
		children[big] += n
	elif n <= candy:
		give_each = candy // n
		candy -= n * give_each
		children[biggest-give_each] = n
		heapq.heappush(heap, -(biggest-give_each))
	else:	
		children[biggest] = n - candy
		children[biggest-1] = children.get(biggest-1, 0) + candy
		candy = 0

print(sum(child**2 * n for child, n in children.items()))