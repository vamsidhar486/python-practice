"""
All preorder, inorder and post order traversals of binary tree are DFS traversals
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None


def inorder(root):
    current = root
    stack = []

    while stack :
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data, end="->")
            current = current.right
        else:
            break



def preorder(root):

    if root is None:
        return

    stack = []
    stack.append(root)

    while len(stack) > 0:
        root = stack.pop()
        print(root.data, end="->")
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)




def postorder(root)
    if root is None:
        return

    stack = []
    stack.append(root)

    while len(stack) > 0:
        root = stack.pop()
        