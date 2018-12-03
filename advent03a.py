import sys
import collections

input = [line.rstrip() for line in sys.stdin.readlines()]
counters = collections.defaultdict(lambda:0)
for line in input:
    [claim_id, trash, lefttop, widthheight] = line.split()
    [left,top] = [int(x) for x in lefttop[:-1].split(",")]
    [width,height] = [int(x) for x in widthheight.split("x")]
    
    for x in range(left,left+width):
        for y in range(top,top+height):
            counters[x,y] += 1

print len(filter(lambda x:x>1 ,counters.values()))

