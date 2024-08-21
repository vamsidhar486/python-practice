# Queue implementation using array

class Queue:

    def __init__(self):
        self.queue = []

    # adding an element
    def enqueue(self, element):
        self.queue.append(element)

    # removing an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # displaying queue
    def display(self):
        print(self.queue)

    # size of the queue
    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()
