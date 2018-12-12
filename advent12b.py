import sys

input = [line.rstrip() for line in sys.stdin.readlines()]
state = input[0].split(" ")[2]
state_beg_posn = 0
rule_segs = [line.split(" ") for line in input[2:]]
rules = {rule_seg[0]:rule_seg[2] for rule_seg in rule_segs}
for rule_seg in rule_segs:
    rules[rule_seg[0]] = rule_seg[2]

num_gens = 50000000000
# I didn't actually run this many generations; experimenting with
# smaller runs showed this (at least for my particular input)
# turned into Game-of-Life-style gliders, so it converged to a
# predictable pattern after a few thousand generations.
for gen in range(num_gens):
    state = "...." + state + "...."
    state_beg_posn -= 2
    new_state = ""
    for i in range(2,len(state)-2):
        try:
            new_state += rules[state[i-2:i+3]]
        except KeyError:
            new_state += "."
    state = new_state
    while state[0:5]==".....":
       state = state[2:]
       state_beg_posn += 2
    while state[-5:]==".....":
       state = state[0:-2]

print state
sum = 0
for i in range(len(state)):
    if state[i]=="#":
        sum += i+state_beg_posn
print sum
