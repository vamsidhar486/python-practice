# A simple Python program to introduce a linked list

# Node class
class Node:

    # Constructor to initialise the node object
    def __init__(self, data=None, ref=None):
        self.data = data  # Assign data
        self.ref = ref  # Initialize ref as null


# Linked List class contains a Node object
class LinkedList:

    # Method to initialize head
    def __init__(self):
        self.head = None

    # Method to print Linked List
    def print_linked_list(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                # print(n.data)
                n = n.ref

    # Method to add element at the beginning of the linked list
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Method to add element at the end of the linked list
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # Method to add element in between two Nodes in the linked list
    # Case 1: Method to add element after the x element in the linked list
    def add_after(self, data, x):
        n = self.head
        while n.ref is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Case 2: Method to ass element before the x element in the linked list
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List ie empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node not found in linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Method to add nodes to the empty linked list
    def add_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    # Method to delete node from the beginning of Linked List:
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            self.head = self.head.ref

    # Method to delete the node from the end of the linked list
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty!")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    # Method to delete the node from middle of the Linked List
    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List ie empty!")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
            if n.ref is None:
                print("Node not present in linked list")
            else:
                n.ref = n.ref.ref


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   l_list = LinkedList()
   # l_list.head = Node(1)
   # second = Node(2)
   # third = Node(3)
   # l_list.head.ref = second
   # second.ref = third
   l_list.add_begin(40)
   l_list.add_begin(30)
   l_list.add_begin(20)
   l_list.add_begin(10)
   l_list.add_end(50)
   l_list.add_end(60)
   l_list.add_after(55,50)
   l_list.add_after(45,40)
   l_list.add_before(35,40)
   l_list.add_before(25,30)
   # l_list.add_empty(10)
   # l_list.add_empty(20)
   l_list.print_linked_list()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
