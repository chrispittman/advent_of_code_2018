import sys

input = [line.rstrip() for line in sys.stdin.readlines()]
input = "".join(input)
input = [int(line) for line in input.split(" ")]

class TreeNode(object):
    def __init__(self):
        self.children = []
        self.metadata = []
        self.parent = None
    def add(self, node):
        node.parent = self
        self.children.append(node)
    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        v = 0
        for child_ix in self.metadata:
            if child_ix <= len(self.children):
                v = v + self.children[child_ix-1].value()
        return v

root_node = TreeNode()
all_metadata = []
def parse(current_node, current_parse_posn, depth):
    num_child_nodes = input[current_parse_posn]
    num_metadata_entries = input[current_parse_posn+1]
    current_parse_posn = current_parse_posn+2
    for c_ix in range(num_child_nodes):
        child = TreeNode()
        current_node.add(child)
        current_parse_posn = parse(child, current_parse_posn,depth+1)
    for m in input[current_parse_posn:current_parse_posn+num_metadata_entries]:
        current_node.metadata.append(m)
        all_metadata.append(m)
    return current_parse_posn + num_metadata_entries

parse(root_node,0,0)
print root_node.value()

