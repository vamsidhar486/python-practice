"""
Given an array of size N and an integer K, return the count of distinct numbers in all windows of size K.

Examples:

Input: arr[] = {1, 2, 1, 3, 4, 2, 3}, K = 4
Output: 3 4 4 3
Explanation: First window is {1, 2, 1, 3}, count of distinct numbers is 3
                      Second window is {2, 1, 3, 4} count of distinct numbers is 4
                      Third window is {1, 3, 4, 2} count of distinct numbers is 4
                      Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

Input: arr[] = {1, 2, 4, 4}, K = 2
Output: 2 2 1
Explanation: First window is {1, 2}, count of distinct numbers is 2
                      First window is {2, 4}, count of distinct numbers is 2
                      First window is {4, 4}, count of distinct numbers is 1
"""
from collections import defaultdict


def count_distinct_elements_sliding(arr,k):
    mp = defaultdict(lambda:0)

    dist_count = 0

    res = []

    for i in range(k):
        if mp[arr[i]] == 0:
            dist_count += 1
        mp[arr[i]] += 1

    res.append(dist_count)

    for i in range(k, len(arr)):

        if mp[arr[i - k]] == 1:
            dist_count -= 1
        mp[arr[i - k]] -= 1

        if mp[arr[i]] == 0:
            dist_count += 1
        mp[arr[i]] += 1

        res.append(dist_count)

    return res


print(count_distinct_elements_sliding([1,2,4,4], 2))
