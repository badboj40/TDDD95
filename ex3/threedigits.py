__author__ = "Gustav Elmqvist"

"""
    This program prints the last three digits of the factorial of the input
    number that are non-zero. The result is continuously truncated so that 
    the calculations does not have to be that big.

    Time complexity: O(n)
"""

result = 1

for i in range(1, int(input())+1):

    # The factorial part.
    result *= i

    # Remove trailing zeroes.
    while result % 10 == 0:
        result //= 10
    
    # Truncate the result.
    result %= 1000000000000

# Print the last three digits of the result.
print(str(result)[-3:])