
__author__ = "Gustav Elmqvist"

"""
    This program determines the voting outcome of the Uxuhul indian priests.
    

    The problem is solved with dynamic programming starting with the vote of
    the last priest and going towards the first priest.

    1. For every possible state, determine the final outcome after the final
       priest has voted.

    2. Go through all priests backwards and determine the final outcome by 
       using the knowledge of what the next priest will vote for.

    3. At last the final outcome will be the state that is reached after the
       first priest votes on the state 'NNN'.

    Time complexity: O(N) where N is the amount of priests that are voting.
"""


def voting(preferences):
    """
        Determine the voting result based on the preferences of each priest.
    """
    result = []
    for preference in preferences[::-1]:

        best_outcomes = []
        for state in range(8):

            # Vote by flipping stone 1, 2 or 3. Determine what the outcome
            # will be for each voting alternative.
            outcomes = []
            for vote in (0b100, 0b010, 0b001):
                new_state = state ^ vote
                outcome = result[new_state] if result else new_state
                outcomes.append(outcome)

            # The best outcome is the one that has the lowest preference value
            best_outcomes += [min(outcomes, key = lambda x: preference[x])]

        # These outcomes will be used to determine the next priest's votes in
        # different scenarios.
        result = best_outcomes

    return result[0]


if __name__ == "__main__":
    
    states = ["NNN", "NNY", "NYN", "NYY", "YNN", "YNY", "YYN", "YYY"]

    for _ in range(int(input())):

        preferences = [[*map(int, input().split())] for _ in range(int(input()))]

        outcome = voting(preferences)

        print(states[outcome])