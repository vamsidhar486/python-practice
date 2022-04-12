"""
Bubble sort
"""


def bubble_sort(input_list):
    """

    :param input_list:
    :return:
    """
    for i in range(len(input_list) - 1):
        for j in range(len(input_list) - 1 - i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                print(input_list)
            else:
                print(input_list)
        print()


if __name__ == "__main__":
    bubble_sort([6, 4, 5, 8, 2, 9, 5, 1, 0])
