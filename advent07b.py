import sys

input = [line.rstrip() for line in sys.stdin.readlines()]
input = [[line[5],line[36]] for line in input]

costs = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
workers = [{'task':'','time_remaining':0},{'task':'','time_remaining':0},{'task':'','time_remaining':0},{'task':'','time_remaining':0},{'task':'','time_remaining':0}]
ticks = 0

def calc_cost(task):
    return 60+costs.index(task)

while len(input) > 0:
    ticks=ticks+1
    parents = set([pair[0] for pair in input])
    children = set([pair[1] for pair in input])
    # current pairs represent one or more trees - find the
    # root nodes of those trees
    treetops = sorted(parents.difference(children))
    # try to assign workers to root-level tasks
    for parent in treetops:
        # skip if there's already a worker on this task
        if parent in map(lambda w:w['task'],workers):
            continue
        # find a worker ready to do the job
        available_worker_ix = -1
        for i in range(len(workers)):
            worker = workers[i]
            if worker['task'] == '':
               available_worker_ix = i
               break
        if available_worker_ix == -1:
            continue
        available_worker = workers[available_worker_ix]
        available_worker['task'] = parent
        available_worker['time_remaining'] = calc_cost(parent)
    # decrement clock ticks for all tasks and remove completed ones
    for worker in workers:
        worker['time_remaining'] = worker['time_remaining'] - 1
        if worker['time_remaining'] == 0:
            input = filter(lambda i: i[0]!=worker['task'], input)
            worker['task'] = ''
    # if we're down to a bunch of (formerly-leaf) nodes, the remaining
    # cost is the most expensive leaf node
    if len(input)==0:
        ticks = ticks + max(map(calc_cost,children))

print ticks
