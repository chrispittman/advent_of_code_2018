import sys
import collections

input = [line.rstrip().split(',') for line in sys.stdin.readlines()]
input = [(int(x), int(y)) for [x,y] in input]
min_x = min([line[0] for line in input])
max_x = max([line[0] for line in input])
min_y = min([line[1] for line in input])
max_y = max([line[1] for line in input])

# for each point, compute the closest location
# and build up a map of the neighborhoods around each location
closest_neighbors = collections.defaultdict(lambda:-1)
for x in range(min_x,max_x+1):
    for y in range(min_y,max_y+1):
       coord_distances = map(lambda (this_x,this_y): abs(x-this_x)+abs(y-this_y), input)
       closest_distance = min(coord_distances)
       closest_distance_first_posn = coord_distances.index(closest_distance)
       closest_distance_last_posn = len(coord_distances) - coord_distances[::-1].index(closest_distance) - 1
       if closest_distance_first_posn == closest_distance_last_posn:
#           print x,y,coord_distances,closest_distance,closest_distance_first_posn
           closest_neighbors[x,y] = closest_distance_first_posn

# any neighborhood along the edge extends to infinity...
infinite_neighborhoods = set()
for x in [min_x,max_x]:
    for y in range(min_y,max_y+1):
        infinite_neighborhoods.add(closest_neighbors[x,y])
for x in range(min_x,max_x+1):
    for y in [min_y,max_y+1]:
        infinite_neighborhoods.add(closest_neighbors[x,y])

neighborhood_sizes = map(lambda i: closest_neighbors.values().count(i), range(len(input)))
for inf in infinite_neighborhoods:
    neighborhood_sizes[inf] = 0
print max(neighborhood_sizes)
