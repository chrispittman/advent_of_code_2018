
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
power_sums = {}
for x in range(1,298):
    for y in range(1,298):
        power_sums[(x,y)] = sum([power[(x+x2,y+y2)] for x2 in range(3) for y2 in range(3)])
max_power = max(power_sums.values())
print power_sums.keys()[power_sums.values().index(max_power)]
