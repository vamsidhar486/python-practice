"""
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint
"""


def min_size_sum_subarray(arr, k):
    currSum = 0
    start = 0
    minCount = float("inf")

    for i in range(len(arr)):
        currSum += arr[i]

        while currSum >= k:
            minCount = min(minCount, i - start + 1)
            currSum -= arr[start]
            start += 1

        if minCount == float('inf'):
            return 0

    return minCount


def minSubArrayLen(target, nums):
    currSum = 0
    start = 0
    count = 0
    minCount = float("inf")

    for i in range(len(nums)):
        currSum += nums[i]

        while currSum >= target:
            minCount = min(minCount, i - start + 1)
            currSum -= nums[start]
            start += 1

        if minCount == float("inf"):
            return 0

    return minCount


print(minSubArrayLen(7,[2, 3, 1, 2, 4, 3]))
