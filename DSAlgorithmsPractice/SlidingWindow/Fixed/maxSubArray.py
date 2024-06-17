"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
from collections import deque


def max_sliding_window(nums, k) :
    dq = deque()
    res = []

    for i in range(k):
        print(i)
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
            print(dq)
        dq.append(i)
        print(dq)

    res.append(nums[dq[0]])
    print(res)

    for i in range(k, len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()
        print(dq)
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        print(dq)
        dq.append(i)
        print(dq)
        res.append(nums[dq[0]])
        print(res)

    return res



print(max_sliding_window([1,2,3,1,4,5,2,3,6], 3))