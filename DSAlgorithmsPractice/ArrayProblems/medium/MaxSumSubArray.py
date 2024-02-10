"""
Given an array of positive integers and a positive numberk, find the maximum sum of any contiguous subarray of size k.

Input: [3, 5, 2, 1, 7], k=2
Output: 8

K =3
Output: 10

The subarray [1, 7] is the sum of the maximum sum.
"""


def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0
    start = 0
    sub_array = []

    for i in range(len(arr)):
        window_sum += arr[i]
        if i - start + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    print(max_sum)
    print(max_sum/k)


max_sum_subarray([3, 5, 2, 1, 7], 3)