"""
You are given two things a string “S” and an Array “indices”. Array indices will contain index .
Now you have to shuffle the string s such that the character at ith index in string s is moved to indices[i]th position in the shuffle string.
In above example the string s = “MEDIUM” and the indices = [2,4,5,0,1,3]
output: IUMMED
"""


def shuffle_string(input, indices):
    output = []
    for i in input:

