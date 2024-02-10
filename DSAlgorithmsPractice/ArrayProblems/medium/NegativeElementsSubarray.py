"""
COUNT NEGATIVE ELEMENTS PRESENT IN EVERY K-LENGTH SUBARRAY
Input: arr = [-1, 2, -2, 3, 5, -7, -5], K = 3
Output: 2, 1, 1, 1, 2
"""


def negative_elements(arr, k):
    output = []
    start = 0
    count = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            count += 1

        if i - start + 1 == k:
            output.append(count)
            if arr[start] < 0:
                count -= 1
            start += 1

    print(output)


negative_elements([-1, 2, -2, 3, 5, -7, -5], 3)
