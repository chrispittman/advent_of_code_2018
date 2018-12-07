import sys

input = [line.rstrip() for line in sys.stdin.readlines()]
input = [[line[5],line[36]] for line in input]

order = ""
while len(input) > 0:
    parents = set([pair[0] for pair in input])
    children = set([pair[1] for pair in input])
    for parent in sorted(parents.difference(children)):
        order += parent
        input = filter(lambda i: i[0]!=parent, input)
        break
    if len(input)==0:
        order += "".join(sorted(children))

print order
