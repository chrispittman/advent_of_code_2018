import sys

def operate(cmd,a,b,regs):
    if cmd=='addr': return regs[a]+regs[b]
    if cmd=='addi': return regs[a]+b
    if cmd=='mulr': return regs[a]*regs[b]
    if cmd=='muli': return regs[a]*b
    if cmd=='banr': return regs[a]&regs[b]
    if cmd=='bani': return regs[a]&b
    if cmd=='borr': return regs[a]|regs[b]
    if cmd=='bori': return regs[a]|b
    if cmd=='setr': return regs[a]
    if cmd=='seti': return a
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
instrs = [line.split(' ') for line in input]
instrs = [(op,int(a),int(b),int(c)) for op,a,b,c in instrs]

while read_line < len(input) and read_line >= 0:
    regs[inst_reg] = read_line
    op,a,b,c = instrs[read_line]
    regs[c] = operate(op,a,b,regs)
    read_line = regs[inst_reg]
    read_line += 1

print regs
