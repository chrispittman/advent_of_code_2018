import sys

input = [line.rstrip() for line in sys.stdin.readlines()]
input = [int(line) for line in input]

cur_freq = 0
found_freqs = set()
posn = 0
while True:
    if posn >= len(input):
       posn = 0

    cur_freq += input[posn]
    if cur_freq in found_freqs:
       print cur_freq
       break
    found_freqs.add(cur_freq)

    posn += 1
