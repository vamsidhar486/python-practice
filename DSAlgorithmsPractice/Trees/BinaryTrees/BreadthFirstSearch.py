"""

"""



class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def BFS(root):
    if root is None:
        return

    # Replaced with queue = [] and queue.append(root)
    queue = []

    queue.append(root)

    while len(queue) > 0:
        print(queue[0].data, end="->")
        root = queue.pop(0)
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


BFS(root)

