"""
All preorder, inorder and post order traversals of binary tree are DFS traversals
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


def inorder(root):
    stack = [root]
    while len(stack) > 0:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            current = stack[-1]
            current = stack.pop()
            print(current.data, end="->")
            current = current.right


def preorder(root):
    stack = [root]
    while len(stack) > 0:
        curr = stack[-1]
        print(curr.data, end="->")
        stack.pop()
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)


def postorder(root):
    """
    post order traversal using two stacks
    :param root:
    :return:
    """
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:
        curr = stack1[-1]
        stack1.pop()
        stack2.append(curr)
        if curr.left is not None:
            stack1.append(curr.left)
        if curr.right is not None:
            stack2.append(curr.right)

    while stack2:
        curr = stack2[-1]
        print(curr.data, end="->")
        stack2.pop()


def postorder(root):
    """
    using one stack
    :param root:
    :return:
    """
    stack = []
    curr = root
    prev = None
    while curr is not None or len(stack) > 0:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack[-1]
            if curr.right is None or curr.right == prev:
                print(curr.data, end="->")
                stack.pop()
                prev = curr
                curr = None
            else:
                curr = curr.right


root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")


print(preorder(root))
print(postorder(root))