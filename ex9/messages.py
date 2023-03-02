import sys, re

__author__ = "Gustav Elmqvist"


# Parse indata
indata = sys.stdin.read().split('#')[:-1]
words = indata[0].split()
messages = [msg.replace('\n', '') for msg in indata[1].split('|')[:-1]]


for message in messages:

    # Generate a list of all possible match intervals.
    intervals = [m.span() for w in words for m in re.finditer(w, message)]

    # Sort the intervals based on the end of each interval.
    intervals.sort(key=lambda x:x[1])

    result = 0 
    i = 0

    # Greedily add all intervals that you can.
    for start, end in sorted(intervals, key=lambda x:x[1]):
        if start >= i:
            result += 1
            i = end

    print(result)