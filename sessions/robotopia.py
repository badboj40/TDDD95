
__author__ = "Gustav Elmqvist"

# Brute force solution, test every x value and check if the corresponding
# y value is valid.

for _ in range(int(input())):
    legs_x, arms_x, legs_y, arms_y, legs, arms = map(int, input().split())

    solutions = []

    for x in range(1, 10001):

        y = (legs - legs_x*x) / legs_y  # From legs_x*x + legs_y*y == legs.

        if y.is_integer() and 1 <= y <= 10000 and arms_x*x + arms_y*y == arms:
            solutions.append((x, int(y)))

    print(*solutions[0] if len(solutions)==1 else '?')