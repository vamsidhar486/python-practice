"""
Implement queue with Array or list
"""


def isEmpty(q):
    """
    Function to check whether queue is empty or not
    :param q: input queue
    :return: emptiness of queue
    """
    if len(q) == 0:
        print("Queue is empty !")


def enqueue(q, element):
    """
    Function to push element in to queue
    :param q: input queue
    :param element: item to push to queue
    :return:
    """
    q.append(element)
    print("element pushed to queue", element)


def dequeue(q):
    """
    Function to remove out element from queue
    :param q: input queue
    :return:
    """
    if isEmpty(q):
        print("Queue is empty !")
    else:
        e = q.pop(0)
        print("Removed out the element from queue is", e)


def top_bottom(q):
    """
    Function to fetch top and bottom elements of queue
    :param s: input queue
    :return:
    """
    print("Top element from queue is", q[-1])
    print("Bottom element from queue is", q[0])


if __name__ == '__main__':
    queue = []
    isEmpty(queue)
    enqueue(queue, 10)
    enqueue(queue, 20)
    enqueue(queue, 30)
    enqueue(queue, 40)
    enqueue(queue, 50)
    print(queue)
    top_bottom(queue)
    dequeue(queue)
    print(queue)
