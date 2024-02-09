"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".



Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""


def jewels_stones(jewels, stones):
    dict = {}
    output = 0
    for i in stones:
        dict[i] = dict.get(i, 0) + 1

    for i in jewels:
        if i in dict:
            output = output + dict[i]
    return output


print(jewels_stones("aA", "aAAbbbb"))
