
def calc_power(x,y,ser_num):
    rack_id = x+10
    power = (rack_id*y) + ser_num
    power *= rack_id
    power = (power/100) % 10
    return power-5

grid_ser_num = 5177

power = {}
for x in range(1,300):
   for y in range(1,300):
       power[(x,y)] = calc_power(x,y,grid_ser_num)
max_power_sum = 0
max_power_posn = None
for x in range(1,300):
    for y in range(1,300):
        max_size = 300-max(x,y)
        max_size = min(20,max_size)
        for size in range(max_size):
            this_sum = sum([power[(x+x2,y+y2)] for x2 in range(size) for y2 in range(size)])
            if this_sum > max_power_sum:
                max_power_sum = this_sum
                max_power_posn = (x,y,size)
print max_power_sum
print max_power_posn
