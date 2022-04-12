"""
function to sum list elements
"""


def sum_list(arr):
    """

    :param arr:
    :return:
    """
    sum = 0
    for i in arr:
        sum += i
    return sum


def mul_list(arr):
    """

    :param arr:
    :return:
    """
    mul = 1
    for i in arr:
        mul = mul * i
    return mul


if __name__ == '__main__':
    print(sum_list([1, 4, 5, 6, 7]))
    print(mul_list([1, 2, 3, 4, 5]))
