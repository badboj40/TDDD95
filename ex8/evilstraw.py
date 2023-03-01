
__author__ = "Gustav Elmqvist"


def palindrome(string):

    if len(string) <= 2:
        return 0 if string[0] == string[-1] else -float('inf')

    for i in range(len(string)-1):
        if string[i] == string[-1]:
            return i + palindrome(string[:i] + string[i+1:-1])
        if string[~i] == string[0]:
            return i + palindrome(string[1:~i] + string[~i+1:])

    return -float('inf')


for _ in range(int(input())):
    swaps = palindrome(input())
    print(swaps if swaps >= 0 else "Impossible")