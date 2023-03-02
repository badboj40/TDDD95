
__author__ = "Gustav Elmqvist"


def is_happy(x):
    previous = set()
    while x != 1:
        x = sum(int(d)**2 for d in str(x))
        if x in previous: return False
        previous.add(x)
    return True


def is_prime(x):
    if x < 2:
        return False

    for d in range(2, int(x**0.5)+1):
        if x%d == 0: return False 
    return True


for _ in range(int(input())):
    i, x = map(int, input().split())
    print(i, x, 'YES' if is_happy(x) and is_prime(x) else 'NO')