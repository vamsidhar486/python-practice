"""
Given a sorted array. Write a function that creates a Balanced Binary Search Tree using array elements.

Examples:

Input: arr[] = {1, 2, 3}
Output: A Balanced BST
      2
    /  \
 1     3
Explanation: all elements less than 2 are on the left side of 2 , and all the elements greater than 2 are on the right side

Input: arr[] = {1, 2, 3, 4}
Output: A Balanced BST
          3
        /  \
     2    4
   /
1
"""


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = (len(arr)) // 2
    root = Node(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid + 1:])
    return root


def preorder(node):
    if not node:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


arr = [1, 2, 3, 4, 5, 6, 7]
root = sorted_array_to_bst(arr)
preorder(root)
