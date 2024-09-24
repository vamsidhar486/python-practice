"""

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1


def print_level(root, level):
    if root is None:
        return
    if level == 0:
        print(root.data, end="->")
    else:
        print_level(root.left, level - 1)
        print_level(root.right, level - 1)


def level_order_traversal(root, height):
    for i in range(height):
        print_level(root, i)


root = Node(5)
insert(root, 4)
insert(root,6)
insert(root,3)
insert(root, 7)

print(height(root))

level_order_traversal(root, height(root))