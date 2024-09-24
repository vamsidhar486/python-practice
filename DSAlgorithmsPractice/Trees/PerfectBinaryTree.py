"""

"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


#calculating height of the tree
def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1


def isPerfectBinary(root, d, level = 0 ):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return d == level+1
    if root.left is None or root.right is None:
        return False
    return isPerfectBinary(root.left, d , level+1) and isPerfectBinary(root.right, d, level+1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print(height(root))

