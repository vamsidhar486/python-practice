
class BTreeNode:

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:

    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t
