"""
Binary Search Tree has all left elements less than its parent and right elements grater than its parent
and all subtrees should be binary search trees
"""


# self is object itself

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # Inserting node to BST
    """
    if tree is empty , place at start
    if tree is not empty, find position, place left or right accordingly
    """

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        # ignoring duplicate values
        if self.key == data:
            return
        # considering duplicate values and placing it in right side
        # if needed in left side, replace condition with >=
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    """
    check root if present, then print yes
    if data is smaller search in left sub tree (left can be empty / left can have one or more nodes)
    if data is larger then search right sub tree (right can be empty / right can have more nodes)
    """

    def search(self, data):
        if self.key == data:
            print("Node is found")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")


    def delete(self, data):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Node is not present in the tree")

        else:
            if self.lchild is None:
                temp= self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self




    """
    first root --> left --> right
    print root key, left  key and then right key
    """

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    """
    left --> root --> right same order in left sub tree and right subtree
    """
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    """
    left --> right --> root
    """
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")


root = BST(None)
root.insert(20)

root = BST(10)
list1 = [20, 4, 30, 4, 1, 5, 6]
for i in list1:
    root.insert(i)

print(root)
root.search(6)
(root.search(11))


# print("Pre Order")
# root.preorder()
# print()
# print("In Order")
# root.inorder()
# print()
# print("Post Order")
# root.postorder()