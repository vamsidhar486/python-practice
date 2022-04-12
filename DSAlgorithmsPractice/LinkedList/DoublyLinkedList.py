# A simple program to introduce a double linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class LinkedList:
    # Constructor to create Empty Double Linked List
    def __init__(self):
        self.head = None

    # Method to print the doubly linked list data
    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                # print(n.data)
                n = n.nref

    # Backward Traversing
    def print_reverse_linked_list(self):
        print()  # to avoid printing both forward and backward in same line
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

    # Insert to empty linked list
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")

    # Inserting a node at beginning of the doubly linked list
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Inserting a node a the end of the linked list
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    # Adding a node after a given node
    def add_after(self, data, x):
        if self.head is None:
            print("Doubly Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    # Adding a new node before given node
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    # Deleting a node from beginning of the doubly linked list
    """
    three cases: empty linked list, one node in linked list, more nodes in linked list
    """
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.head.pref = None

    # Delete a node at the end of a doubly linked list
    """
    three cases: empty linked list, only one node, more nodes
    """
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    # Delete by value
    """
    three cases : empty linked list, only one node, first node, last node, middle node
    """
    def delete_value(self, x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print("Given Node is not present in Linked List")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("Given Node is not present in the Linked List")



if __name__ =='__main__':
    l_list = LinkedList()
    l_list.insert_empty(10)
    l_list.add_end(20)
    l_list.add_begin(0)
    l_list.add_end(30)
    l_list.add_begin(-10)
    l_list.add_after(5, 0)
    l_list.add_before(-5, 0)
    l_list.delete_end()
    l_list.delete_begin()
    l_list.delete_value(5)
    l_list.print_linked_list()
    l_list.print_reverse_linked_list()









