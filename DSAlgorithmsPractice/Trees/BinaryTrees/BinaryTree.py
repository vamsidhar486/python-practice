"""

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def search(root, data):
    if root.data == data:
        print("Node found in tree")
        return
    if data < root.data:
        if root.left:
            search(root.left, data)
        else:
            print("Node not found in tree")
    else:
        if root.right:
            search(root.right, data)
        else:
            print("Node not found in tree")



def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(str(root.data) + "->", end="")
        inorder_traversal(root.right)


def preoprder_traversal(root):
    if root is not None:
        print(str(root.data) + "->", end="")
        preoprder_traversal(root.left)
        preoprder_traversal(root.right)


def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(str(root.data) + "->", end="")





root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

search(root, 15)

print(preoprder_traversal(root))
print(inorder_traversal(root))
print(postorder_traversal(root))
