__author__ = "Gustav Elmqvist"

"""
    A program that print the largest integer p such that x is a 
    perfect p:th power.
"""

while x:=int(input()):

    # Go through all divisiors b from 2 to the square root of x and
    # ignore the sign of x for now.
    for b in range(2,int(abs(x)**.5)+1):
        
        y = abs(x)
        p = 0

        while y % b == 0:
            y //= b
            p += 1

        # if x is negative, p has to be an odd number.
        if y==1 and (x>0 or x<0 and p%2):
            print(p)
            break
    
    # If no perfect square was found, the answer is 1
    else:
        print(1)