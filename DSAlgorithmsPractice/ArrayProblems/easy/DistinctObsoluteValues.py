"""
COUNT DISTINCT ABSOLUTE VALUES IN A SORTED ARRAY
Input:  { -1, -1, 0, 1, 1, 1 }
Output: The total number of distinct absolute values is 2 (0 and 1)
"""


def get_obsolute(arr):
    d = {}
    count = 0
    for i in range(len(arr)):
        if arr[i] >= 0 and arr[i] not in d:
            d[arr[i]] = 1
            count += 1
    return count


print(get_obsolute([-1, -1, 0, 1, 1, 1]))
