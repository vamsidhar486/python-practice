"""
Insertion Sort Implementation
"""


def insertion_sort(input_list):
    """

    :param input_list:
    :return:
    """
    for i in range(1, len(input_list)):
        current = input_list[i]
        pos = i
        while current < input_list[pos-1] and pos > 0:
            input_list[pos] = input_list[pos-1]
            pos = pos - 1
        input_list[pos] = current
    print(input_list)


if __name__ == "__main__":
    input_list = [1, 3, 4, 7, 8, 2, 3, 4, 5]
    insertion_sort(input_list)

