"""
FIND DUPLICATES WITHIN A RANGE ‘K’ IN AN ARRAY

Input: nums = [5, 6, 8, 2, 4, 6, 9]
k = 2
Ouput: False
"""


def is_having_duplicates(arr, k):
    if len(arr) < k:
        return False
    d = {}

    for i in range(len(arr)):
        if arr[i] in d and i - d[arr[i]] <= k:
            return True
        else:
            d[arr[i]] = i
    return False


print(is_having_duplicates([5, 5, 8, 2, 4, 6, 9], 2))
