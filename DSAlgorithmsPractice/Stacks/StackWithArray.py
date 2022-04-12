"""
Implement stack with Array or list
"""


def isEmpty(s):
    """
    Function to check whether stack is empty or not
    :param s: input stack
    :return: emptiness of stack
    """
    if len(s) == 0:
        print("Stack is empty !")


def push(s, element):
    """
    Function to push element in to stack
    :param s: input stack
    :param element: item to push to stack
    :return:
    """
    s.append(element)
    print("element pushed to stack", element)


def pop(s):
    """
    Function to pop out element from stack
    :param s: input stack
    :return:
    """
    if isEmpty(s):
        print("Stack is empty !")
    else:
        e = s.pop()
        print("Popped out the element from stack is", e)


def top_bottom(s):
    """
    Function to fetch top and bottom elements of stack
    :param s: input stack
    :return:
    """
    print("Top element from stack is", s[-1])
    print("Bottom element from stack is", s[0])


if __name__ == '__main__':
    stack = []
    isEmpty(stack)
    push(stack, 10)
    push(stack, 20)
    push(stack, 30)
    push(stack, 40)
    push(stack, 50)
    print(stack)
    top_bottom(stack)
    pop(stack)
    print(stack)
