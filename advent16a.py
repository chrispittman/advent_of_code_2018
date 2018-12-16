import sys

input = [line.rstrip() for line in sys.stdin.readlines()]
read_line = 0
result = 0
while read_line < len(input):
    if input[read_line]=='':
        break
    before = [int(x) for x in input[read_line].replace('Before: [','').replace(']','').split(', ')]
    cmd = [int(x) for x in input[read_line+1].split(' ')]
    after = [int(x) for x in input[read_line+2].replace('After:  [','').replace(']','').split(', ')]
    interps = []
    op,a,b,c = cmd
    #addr
    if after[c] == before[a] + before[b]:
        interps.append('addr')
    #addi
    if after[c] == before[a] + b:
        interps.append('addi')
    #mulr
    if after[c] == before[a] * before[b]:
        interps.append('mulr')
    #muli
    if after[c] == before[a] * b:
        interps.append('muli')
    #banr
    if after[c] == before[a] & before[b]:
        interps.append('banr')
    #bani
    if after[c] == before[a] & b:
        interps.append('bani')
    #borr
    if after[c] == before[a] | before[b]:
        interps.append('borr')
    #bori
    if after[c] == before[a] | b:
        interps.append('bori')
    #setr
    if after[c] == before[a]:
        interps.append('setr')
    #seti
    if after[c] == a:
        interps.append('seti')
    #gtir
    if after[c] == (1 if (a > before[b]) else 0):
        interps.append('gtir')
    #gtri
    if after[c] == (1 if (before[a] > b) else 0):
        interps.append('gtri')
    #gtrr
    if after[c] == (1 if (before[a] > before[b]) else 0):
        interps.append('gtrr')
    #eqir
    if after[c] == (1 if (a == before[b]) else 0):
        interps.append('eqir')
    #eqri
    if after[c] == (1 if (before[a] == b) else 0):
        interps.append('eqri')
    #eqrr
    if after[c] == (1 if (before[a] == before[b]) else 0):
        interps.append('eqrr')

    if len(interps) >= 3:
        result += 1
    read_line += 4

print result
