"""
Implementing Stack with Single Linked List
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            print("Stack is empty !")
        else:
            print("Stack is not empty !")

    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def print_stack(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                # print(n.data)
                n = n.next


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)
    my_stack.print_stack()
    my_stack.pop()
    my_stack.pop()

