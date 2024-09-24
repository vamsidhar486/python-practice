"""

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
            return
        if self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)


root = Node(1)
list1 = [2, 3, 4, 5, 6, 7, 8]
for i in list1:
    root.insert(i)

print(root)
print(root.data)
print(root.left)
