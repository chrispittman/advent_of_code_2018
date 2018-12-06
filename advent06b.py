import sys
import collections

input = [line.rstrip().split(',') for line in sys.stdin.readlines()]
input = [(int(x), int(y)) for [x,y] in input]
min_x = min([line[0] for line in input])
max_x = max([line[0] for line in input])
min_y = min([line[1] for line in input])
max_y = max([line[1] for line in input])

total = 0
max_region_size = 10000
# make a rough estimate of the area we didn't care about in problem A
# that we now have to search
search_bounds = (max_region_size / len(input)) + 10
for x in range(min_x-search_bounds,max_x+1+search_bounds):
    for y in range(min_y-search_bounds,max_y+1+search_bounds):
       coord_distances = map(lambda (this_x,this_y): abs(x-this_x)+abs(y-this_y), input)
       if sum(coord_distances) < max_region_size:
           total += 1

print total
