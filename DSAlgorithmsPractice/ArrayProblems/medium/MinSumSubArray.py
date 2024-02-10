"""
Given an array of positive integers and a positive number k , find the minimum sum of any contiguous subarray of size k.
.
Input: arr = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3
Output: 11

subarray = [4,2,5]
"""


def min_sum_subarray(arr, k):
    min_sum = float("inf")     # flaot(inf) = infinity  float(-inf) = -infinity
    window_sum = 0
    start = 0
    subarray = []

    for i in range(len(arr)):
        window_sum = window_sum + arr[i]

        if i - start + 1 == k:
            min_sum = min(min_sum, window_sum)
            window_sum = window_sum - arr[start]
            start += 1

    return min_sum


print(min_sum_subarray([10, 4, 2, 5, 6, 3, 8, 1], 3))
