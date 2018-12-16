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
result = 0
cmd_options = [None]*16
while read_line < len(input):
    if input[read_line]=='':
        break
    before = [int(x) for x in input[read_line].replace('Before: [','').replace(']','').split(', ')]
    cmd = [int(x) for x in input[read_line+1].split(' ')]
    after = [int(x) for x in input[read_line+2].replace('After:  [','').replace(']','').split(', ')]
    interps = []
    op,a,b,c = cmd
    for cmd_try in ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']:
        if after[c] == operate(cmd_try,a,b,before):
            interps.append(cmd_try)

    read_line += 4
    if cmd_options[op]==None:
        cmd_options[op] = set(interps)
    else:
        cmd_options[op] = cmd_options[op].intersection(set(interps))

cmds = [None]*16
while None in cmds:
    for i in range(16):
        if len(cmd_options[i])==1:
            cmds[i] = list(cmd_options[i])[0]
        for j in range(16):
            try:
                cmd_options[j].remove(cmds[i])
            except KeyError:
                pass

regs = [0]*4

for line in input[read_line+2:]:
    op,a,b,c = [int(x) for x in line.split(' ')]
    regs[c] = operate(cmds[op],a,b,regs)
    
print regs
