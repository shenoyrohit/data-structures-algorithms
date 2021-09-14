class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_children(self, name):
        self.children.append(Node(name))
        return self

    # O (V + E) time | O (V)  Space
    # Visit every node, add to the array, recursively visit all children, final return is called for first call only
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array