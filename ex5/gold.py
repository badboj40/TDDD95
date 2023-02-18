
__author__ = "Gustav Elmqvist"

"""
    Search for gold with DFS while avoiding potential traps.
"""

W, H = map(int, input().split())

grid = [list(input()) for _ in range(H)]

stack = [(y,x) for y in range(H) for x in range(W) if grid[y][x]=='P']

gold = 0
while stack:
    y,x = stack.pop()

    # We reached a dead end, so we skip to the next position in the queue
    if grid[y][x] == '#': continue

    # Increment the gold counter if we found gold
    if grid[y][x] == 'G': gold += 1

    # Since we already explored the current position, it will be treated
    # as a dead end in the future
    grid[y][x] = '#'

    # All orthogonally adjacent neighbors in the grid
    neighbors = [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]

    # If none of the neighbors are traps they are safe to explore
    if all(grid[ny][nx]!='T' for ny,nx in neighbors): stack += neighbors


print(gold)