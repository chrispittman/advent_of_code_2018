import sys

"""
Bleh, brute-forced this one b/c it's a bad puzzle.  You can either
read the instructions and reverse-engineer a cleverer way of getting
the answer manually, or you can brute-force it, and both seem like they're
unkosher given the parameters of AoC.
"""

def operate(cmd,a,b,regs):
    if cmd=='addr': return regs[a]+regs[b]
    if cmd=='addi': return regs[a]+b
    if cmd=='mulr': return regs[a]*regs[b]
    if cmd=='muli': return regs[a]*b
    if cmd=='setr': return regs[a]
    if cmd=='seti': return a
    if cmd=='banr': return regs[a]&regs[b]
    if cmd=='bani': return regs[a]&b
    if cmd=='borr': return regs[a]|regs[b]
    if cmd=='bori': return regs[a]|b
    if cmd=='gtir': return 1 if (a > regs[b]) else 0
    if cmd=='gtri': return 1 if (regs[a] > b) else 0
    if cmd=='gtrr': return 1 if (regs[a] > regs[b]) else 0
    if cmd=='eqir': return 1 if (a == regs[b]) else 0
    if cmd=='eqri': return 1 if (regs[a] == b) else 0
    if cmd=='eqrr': return 1 if (regs[a] == regs[b]) else 0
    return None

input = [line.rstrip() for line in sys.stdin.readlines()]
read_line = 0
inst_reg = int(input[0][-1:])
input = input[1:]
regs = [0]*6
regs[0] = 1
instrs = [line.split(' ') for line in input]
instrs = [(op,int(a),int(b),int(c)) for op,a,b,c in instrs]

num_instrs = len(input)
while read_line < num_instrs and read_line >= 0:
    regs[inst_reg] = read_line
    op,a,b,c = instrs[read_line]
    regs[c] = operate(op,a,b,regs)
    read_line = regs[inst_reg]
    read_line += 1
    print regs[5]

print regs
