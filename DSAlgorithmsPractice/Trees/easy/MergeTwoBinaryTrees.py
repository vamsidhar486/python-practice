"""
Given two binary trees. We need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the non-null node will be used as the node of new tree.

Example:

Input:
     Tree 1            Tree 2
       2                 3
      / \               / \
     1   4             6   1
    /                   \   \
   5                     2   7

Output: Merged tree:
         5
        / \
       7   5
      / \   \
     5   2   7
Note: The merging process must start from the root nodes of both trees.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def merge_two_bt(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.data += t2.data
    t1.left = merge_two_bt(t1.left, t2.left)
    t1.right = merge_two_bt(t1.right, t2.right)
    return t1

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
