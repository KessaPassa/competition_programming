class NodeList:
    def __init__(self):
        self.node_dict = {}

    def set_node(self, node):
        if not node.val in self.node_dict:
            self.node_dict[node.val] = node
        else:
            # print(self.node_dict[node.val].children)
            self.node_dict[node.val].set_child(node.children)

    def get_info(self):
        return self.node_dict

    def search(self, num):
        queue = self.node_dict[num].children
        while len(queue) > 0:
            node = queue.pop(0)
            if len(node.children) <= 0:
                continue


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def set_child(self, children):
        self.children.extend(children)


n = int(input())
node_dict = NodeList()
# ab_list = []
for _ in range(n-1):
    a, b = map(int, input().split())
    node = Node(a)
    node.set_child([b])
    node_dict.set_node(node)

    node = Node(b)
    node.set_child([a])
    node_dict.set_node(node)

for node in node_dict.get_info().values():
    print(node.val, node.children)
