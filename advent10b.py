import sys
import re

input = [line.rstrip() for line in sys.stdin.readlines()]
pos_vel = [re.split('[\<,/>]',l) for l in input]
pos_vel = [[int(l[1]),int(l[2]),int(l[4]),int(l[5])] for l in pos_vel]

def print_msg(pos_vel):
    xys = [(x,y) for [x,y,vx,vy] in pos_vel]
    min_x = min([x for [x,y,vx,vy] in pos_vel])
    max_x = max([x for [x,y,vx,vy] in pos_vel])
    min_y = min([y for [x,y,vx,vy] in pos_vel])
    max_y = max([y for [x,y,vx,vy] in pos_vel])
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            if (x,y) in xys:
               c = "*"
            else:
               c = " "
            sys.stdout.write(c)
        print

def move(point):
     return [point[0]+point[2], point[1]+point[3], point[2], point[3]]

msg_font_size = 10
num_secs = 0
while True:
    min_y = min([y for [x,y,vx,vy] in pos_vel])
    max_y = max([y for [x,y,vx,vy] in pos_vel])
    if max_y-min_y < msg_font_size:
        print_msg(pos_vel)
        print num_secs
        break
    num_secs += 1
    pos_vel = map(move, pos_vel)

