"""
Given an array of N distinct elements, find the minimum number of swaps required to sort the array.

Examples:

Input: {4, 3, 2, 1}
Output: 2
Explanation: Swap index 0 with 3 and 1 with 2 to form the sorted array {1, 2, 3, 4}

Input: {1, 5, 4, 3, 2}
Output: 2
"""


def min_swap(arr):
    if len(arr) <= 1:
        return 0

    swaps = 0
    tmp_arr = arr.copy()
    h = {}

    tmp_arr.sort()

    for i in range(len(arr)):
        h[arr[i]] = i

    init = 0

    for i in range(len(arr)):
        if arr[i] != tmp_arr[i]:
            swaps += 1
            init = arr[i]
            arr[i], arr[h[tmp_arr[i]]] = arr[h[tmp_arr[i]]], arr[i]
            h[init] = h[tmp_arr[i]]
            h[tmp_arr[i]] = 1
    return swaps


if __name__ == "__main__":
    print(min_swap([2, 1]))
