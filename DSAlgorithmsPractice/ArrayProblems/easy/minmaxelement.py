"""
Python program to find the minimum and maximum element in an array using minimum number of comparisions
"""


class pair:
    def __init__(self):
        """
        Constructor to initialize min and max element as 0
        """
        self.min = 0
        self.max = 0


def min_max_pair(arr, n) -> pair:
    """
    :param arr: array of length n
    :param n: length of an array
    :return: pair which has min and max element of an array
    """
    min_max = pair()

    if len(arr) == 1:
        min_max.min = arr[0]
        min_max.max = arr[0]
        return min_max

    if arr[0] > arr[1]:
        min_max.max = arr[0]
        min_max.min = arr[1]
    else:
        min_max.max = arr[1]
        min_max.min = arr[0]

    for i in range(2, n):
        if arr[i] > min_max.max:
            min_max.max = arr[i]
        elif arr[i] < min_max.min:
            min_max.min = arr[i]

    return min_max


if __name__ == '__main__':
    print(min_max_pair([1,5,7,2,4,5,9,0,10,-1], 10).max)