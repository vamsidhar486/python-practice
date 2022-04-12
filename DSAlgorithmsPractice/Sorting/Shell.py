"""
Shell sort implementation
"""


def shell_sort(input_list):
    """

    :param input_list:
    :return:
    """
    gap = len(input_list)//2
    while gap > 0:
        for i in range(gap, len(input_list)):
            current = input_list[i]
            pos = i
            while current < input_list[pos - gap] and pos >= gap:
                input_list[pos] = input_list[pos - gap]
                pos = pos - gap
            input_list[pos] = current
        gap = gap//2


if __name__ == "__main__":
    num = int(input("Enter the length of the list:"))
    input_list = [int(input()) for x in range(num)]
    print("Unsorted List", input_list)
    shell_sort(input_list)
    print("Sorted List", input_list)

