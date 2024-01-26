"""
Given an integer array, find a maximum product of a triplet in the array.

Examples:

Input:  [10, 3, 5, 6, 20]
Output: 1200
Explanation: Multiplication of 10, 6 and 20

Input:  [-10, -3, -5, -6, -20]
Output: -90

Input:  [1, -4, 3, -6, 7, 0]
Output: 168
"""

import sys


def max_product_triplet1(arr):
    """
    Time complexity O(nLogn) space Complexity O(1)
    :param arr:
    :return:
    """
    if len(arr) < 3:
        return

    arr.sort()
    n = len(arr)

    if arr[n - 1] * arr[n - 2] * arr[n - 3] > arr[0] * arr[1] * arr[n - 1]:
        return arr[n - 1] * arr[n - 2] * arr[n - 3]
    else:
        return arr[0] * arr[1] * arr[n - 1]


def max_product_triplet2(arr):
    """
    Time Complexity O(n^3) Space Complexity O(1)
    :param arr:
    :return:
    """
    if len(arr) < 3:
        return

    n = len(arr)

    max_product = -(sys.maxsize - 1)

    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                max_product = max(max_product, arr[i] * arr[j] * arr[k])

    return max_product


if __name__ == '__main__':
    print(max_product_triplet2([1, -4, 3, -6, 7, 0]))
    print(max_product_triplet2([10, 3, 5, 6, 20]))
    print(max_product_triplet2([-10, -3, -5, -6, -20]))
    print(-(sys.maxsize - 1))
