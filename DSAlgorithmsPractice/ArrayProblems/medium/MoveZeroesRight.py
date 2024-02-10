"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

def move_zeroes_right(arr):
    if len(arr) <= 1:
        return arr

    p1 = 0
    p2 = 0

    while p1 <= len(arr) - 1:
        if arr[p1] != 0:
            arr[p2] = arr[p1]
            p2 += 1
        p1 += 1

    while p2 <= len(arr) - 1:
        arr[p2] = 0
        p2 += 1