"""
Implement a binary tree of height h with array data structure
"""
# For a height h, the array size should be 2^(h=1) - 1
# Index of root node is 0
# Index of left child: 2*i + 1
# Index of right child is 2*i +2
# parent node : (i-1)/2   -- needs to be checked in other articles
"""
Pros: Easy traversal
Cons:   1.Need to know max node count before hand
        2.Inefficient space Utilize
"""


def tree_size(height):
    return [None] * (pow(2, height + 1) - 1)


def root(tree, data):
    if tree[0] is None:
        tree[0] = data
    else:
        print("Tree already has root")


def set_left(tree, parent_index, data):
    if tree[parent_index] is None:
        print("Cannot set child")
    else:
        tree[(2 * parent_index) + 1] = data


def set_right(tree, parent_index, data):
    if tree[parent_index] is None:
        print("Cannot set child")
    else:
        tree[(2*parent_index)+2] = data


# execution
height = 3
BT = tree_size(3)
root(BT,'A')
print(BT)
set_left(BT, 0, 'B')
set_right(BT,0,'C')
set_right(BT,1,'D')
set_left(BT,2,'E')
print(BT)