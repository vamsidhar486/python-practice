"""
DIFFERENCE BETWEEN THE MAXIMUM AND MINIMUM AVERAGE OF ALL K-LENGTH CONTINUOUS SUBARRAYS
Input: arr[ ] = {3, 8, 9, 15}, K = 2
Output: 6.5
All subarrays of length 2 are {3, 8}, {8, 9}, {9, 15} and their averages are (3+8)/2 = 5.5, (8+9)/2 = 8.5, and (9+15)/2 = 12.0 respectively.

Therefore, the difference between the maximum(=12.0) and minimum(=5.5) is 12.0 -5.5 = 6.5
"""


def get_min_max_diff(arr, k):
    window_sum = 0
    min_window_sum = float('inf')
    max_window_sum = float('-inf')
    start = 0

    if len(arr) < k:
        return 0

    for i in range(len(arr)):
        window_sum += arr[i]

        if i - start+1 == k:
            min_window_sum = min(min_window_sum, window_sum)
            max_window_sum = max(max_window_sum, window_sum)
            window_sum -= arr[start]
            start += 1

    print(max_window_sum/k - min_window_sum/k)
    print(max_window_sum - min_window_sum)


get_min_max_diff([3,8,9,15], 2)
