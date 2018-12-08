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

root_node = TreeNode()
all_metadata = []
def parse(current_node, current_parse_posn, depth):
#    print depth, "**starting node, pp:",current_parse_posn
    num_child_nodes = input[current_parse_posn]
    num_metadata_entries = input[current_parse_posn+1]
    current_parse_posn = current_parse_posn+2
#    print depth, "num child",num_child_nodes,"num_md",num_metadata_entries
    for c_ix in range(num_child_nodes):
        child = TreeNode()
        current_node.add(child)
#        print depth, "processing",current_parse_posn
        current_parse_posn = parse(child, current_parse_posn,depth+1)
#        print depth, "processed",current_parse_posn
    for m in input[current_parse_posn:current_parse_posn+num_metadata_entries]:
        current_node.metadata.append(m)
        all_metadata.append(m)
#    print depth, "metadata is ",current_node.metadata
#    print depth,"returning",current_parse_posn+num_metadata_entries
    return current_parse_posn + num_metadata_entries

parse(root_node,0,0)
print sum(all_metadata)

