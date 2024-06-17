"""
moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
k = 3
"""
from collections import deque


def moving_average(arr, k):
    win_sum = sum(arr[:k])
    win_avg = win_sum/k
    output = [win_avg]

    for i in range(len(arr) - k):
        win_sum = win_sum - arr[i] + arr[i+k]
        win_avg = win_sum / k
        output.append(win_avg)

    return output



print(moving_average([40,30,50,46,39,44], 3))