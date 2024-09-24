"""

"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_depth1(root, node, depth=0):
    if root is None:
        return -1

    if root.key == node:
        return depth

    left_depth = find_depth(root.left, node, depth+1)
    if left_depth != -1:
        return left_depth

    return find_depth(root.right, node, depth+1)


def find_depth(root, node):
    if root is None:
        return -1

    depth = -1

    if root.key == node:
        return depth + 1

    left_depth = find_depth(root.left, node)
    if left_depth >= 0:
        return left_depth + 1

    right_depth = find_depth(root.right, node)
    if right_depth >= 0:
        return right_depth + 1

    return depth


def find_height(root, node):
    global height

    if node is None:
        return -1
    left_height = find_height(root.left, node)
    right_height = find_height(root.right, node)
    ans = max(left_height, right_height) + 1

    if root.key == node:
        height = ans

    return ans


# def get_level_util(root, node, level):
#     if root is None:
#         return -1
#     if root.key == node:
#         return level
#
#     # for left
#     down_level = get_level_util(root.left, node, level + 1)
#     if down_level != 0:
#         return down_level
#     # for right
#     down_level = get_level_util(root.right, node, level + 1)
#     return down_level

# def find_level(root, node):
#     return get_level_util(root, node, 1)


# def test(x):
#     dist = -1
#     if x == 5:
#         return dist + 1
#     return dist


root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("d")
root.left.right = Node("e")
root.right.left = Node("f")
root.right.right = Node("g")

# print(find_height(root, "e"))
# print(find_level(root, "e"))
print(find_depth(root, "g"))

# print(test(5))
