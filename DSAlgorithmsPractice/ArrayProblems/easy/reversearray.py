"""
Program to reverse an array
"""


def reverse_array_iter(arr):
    """
    Iterative way to reverse an array
    :param arr: input array / list / string
    :return: reversed array / list / string
    """
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
    return arr


def reverse_array_recursive(arr, start, end):
    """
    Reversing array in recursive approach
    :param arr: input array / list / string
    :param start: starting index of the array / list / string
    :param end: ending index of the array / list /string
    :return: reversed array/ list / string
    """
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array_recursive(arr, start+1, end-1)


def reverse_array_slicing(arr):
    """
    Reversing array / list / string using slice operator
    :param arr: input array / list / string
    :return: reversed array
    """
    return arr[::-1]


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5]
    print('Input Array is', arr)
    print('Reversed Array is', reverse_array_iter(arr))
    print('Reversed Array is', reverse_array_recursive(arr, 0, 5))
    print('Reversed Array is', reverse_array_slicing(arr))
