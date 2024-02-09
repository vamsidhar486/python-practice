"""
Given a balanced string str of size N with an equal number of L and R, the task is to find a maximum number X, such that a given string can be partitioned into X balanced substring. A string called to be balanced if the number of ‘L’s in the string equals the number of ‘R’s.
Examples:


Input : str = “LRLLRRLRRL”
Output : 4
Explanation: { “LR”, “LLRR”, “LR”, “RL”} are the possible partitions.
Input : “LRRRRLLRLLRL”
Output : 3
Explanation: {“LR”, “RRRLLRLL”, “RL”} are the possible partitions.
"""


# Time Complexity O(n)
# Space Complexity O(1)
def max_balanced_parts(input):
    l = 0
    r = 0
    parts = 0
    for i in input:
        if i == 'L':
            l += 1
        else:
            r += 1
        if l == r:
            parts += 1
    print(parts)


max_balanced_parts('LRLLRRLRRL')
max_balanced_parts('LRRRRLLRLLRL')
