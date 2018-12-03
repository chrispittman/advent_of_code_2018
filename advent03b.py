import sys
import collections

input = [line.rstrip() for line in sys.stdin.readlines()]
counters = collections.defaultdict(lambda:[])
claim_ids = set()
for line in input:
    [claim_id, trash, lefttop, widthheight] = line.split()
    claim_ids.add(claim_id)
    [left,top] = [int(x) for x in lefttop[:-1].split(",")]
    [width,height] = [int(x) for x in widthheight.split("x")]
    
    for x in range(left,left+width):
        for y in range(top,top+height):
            counters[x,y].append(claim_id)

contested_claims = set()
for square_claims in counters.values():
    if len(square_claims) == 1:
        continue
    for claim in square_claims:
        contested_claims.add(claim)
        
print claim_ids.difference(contested_claims)

