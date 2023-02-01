from fractions import Fraction

__author__ = "Gustav Elmqvist"

"""
    This program converts repeating decimal numbers to fractions.

    The fractions library is very helpful here, but since we don't know
    how many of the decimals are actually repeating we have to be careful.

    For example: x = 0.6529...
                                           _      __     ___      ____
    We don't know if it translates to 0.6529, 0.6529, 0.6529 or 0.6529.

    Therefore we have to check all of the alternatives and find out which one
    is the best. The best one is the one with the smallest denominator as
    specified in the problem description.

    The algorithm is based on the second example in this math lesson:
    https://www.greenemath.com/Algebra2/5/RepeatingDecimaltoFractionLesson.html

"""


while (x := input()[2:-3]):

    # We don't have a best fraction yet.
    best = None

    # Try every possible number of repeating decimals.
    for n in range(1, len(x)+1):

        # Calculate the numerator and denominator based on the algorithm
        # mentioned above.
        numerator = (int(x + x[-n:]) - int(x)) // 10**n
        denominator = int('9'*n + '0'*(len(x)-n))

        # Use the fractions library to simplify the fraction.
        fraction = Fraction(numerator, denominator)

        # If the new fraction is the best one yet, we update the best fraction.
        if best is None or fraction.denominator < best.denominator:
            best = fraction

    # Edge case: if the input is for example 0.9999... this will evaluate
    # to 1, But Kattis require the answer to be 1/1 so therefore the if
    # statement below is needed.
    print('1/1' if best == 1 else best)