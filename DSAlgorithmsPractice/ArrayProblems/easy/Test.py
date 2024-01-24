from typing import List


def countPairs(nums: List[int], target: int) -> int:
    pairs = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print(i,j)
            if (i < j) and (nums[i] + nums[j] < target):
                pairs += 1
    print(pairs)

countPairs( [-1,1,2,3,1],2)
