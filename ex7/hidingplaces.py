
__author__ = "Gustav Elmqvist"


def pos2coord(pos):
    return ord(pos[0])-97, int(pos[1])-1


def coord2pos(x, y):
    return chr(x+97) + str(y+1)


def get_neighbors(x, y):
    return [
        (x+2, y+1), (x+2, y-1),
        (x-2, y+1), (x-2, y-1),
        (x+1, y+2), (x-1, y+2),
        (x+1, y-2), (x-1, y-2),
    ]


for _ in range(int(input())):

    start_x, start_y = pos2coord(input())

    distances = {}
    visited = set()

    queue = [(0, start_x, start_y)]

    # Search through all chess board squares with BFS
    while queue:

        d,x,y = queue.pop(0)

        # Skip the square if it is outside of the chess board or if it has
        # already been visited.
        if not (0 <= x < 8 and 0 <= y < 8) or (x,y) in visited:
            continue

        # No need to explore (x, y) in the future
        visited.add((x, y))

        # Add (-y, x) coordinates instead of (x, y) to simplify the sorting
        distances[d] = distances.get(d, []) + [(-y, x)]

        # Add all neighboring squares to the bfs queue
        queue += [(d+1,nx,ny) for nx,ny in get_neighbors(x,y)]

    # The distance of the square that is furthest away
    max_distance = max(distances)

    # Convert all coordinates to chess notation in sorted order
    squares = [coord2pos(x,-y) for y,x in sorted(distances[max_distance])]

    print(max_distance, *squares)