"""
Quick Sort Implementation
"""


def find_pivot(input_list, first, last):
    """
    Function to find the position of the pivot value
    :param input_list:
    :param first:
    :param last:
    :return:
    """
    pivot = input_list[first]
    left = first + 1
    right = last
    while True:
        while left <= right and input_list[left] <= pivot:
            left = left + 1
        while left <= right and input_list[right] >= pivot:
            right = right - 1
        if left < right:
            break
        else:
            input_list[left], input_list[right] = input_list[right], input_list[left]
    input_list[first], input_list[right] = input_list[right], input_list[first]
    return right


def quick_sort(input_list, first, last):
    """

    :param input_list:
    :param first:
    :param last:
    :return:
    """
    if first < last:
        pivot = find_pivot(input_list, first, last)
        quick_sort(input_list, first, pivot - 1)
        quick_sort(input_list, pivot + 1, last)


if __name__ == "__main__":
    input_list = [4, 56, 78, 2, 3, 98, 7, 0, 1]
    n = len(input_list)
    print(n)
    quick_sort(input_list, 0, n-1)
    print(input_list)



