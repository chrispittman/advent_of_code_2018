import sys

input = [line.rstrip() for line in sys.stdin.readlines()]
input = [int(line) for line in input]
print sum(input)
