"""

"""


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def isFullBinaryTree(node):
    if node is None:
        return True

    if node.left is None and node.right is None:
        return True

    if node.left is not None and node.right is not None:
        return isFullBinaryTree(node.left) and isFullBinaryTree(node.right)

    return False


root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)


if isFullBinaryTree(root):
    print("The tree is full binary tree")
else:
    print("The tree is not full binary tree")
