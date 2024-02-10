"""
Given an integer array nums, move all 0's to the start of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [0,0,1,3,12]
Example 2:

Input: nums = [0]
Output: [0]
"""


# Time complexity O(n)
# Space Complexity O(1)
def move_zeroes_left(nums):
    if len(nums) <= 1:
        return nums
    left_index = len(nums) - 1
    right_index = len(nums) - 1

    while left_index <= 0:
        if nums[left_index] != 0:
            nums[right_index] = nums[left_index]
            right_index += 1
        left_index += 1

    while right_index <= 0:
        nums[right_index] = 0
        right_index += 1