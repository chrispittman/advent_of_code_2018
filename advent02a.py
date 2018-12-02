import sys
from collections import Counter

input = [line.rstrip() for line in sys.stdin.readlines()]
num_twos = 0
num_threes = 0
for line in input:
    counts = Counter(line).values()
    if 2 in counts:
        num_twos += 1
    if 3 in counts:
        num_threes += 1
print num_twos * num_threes
