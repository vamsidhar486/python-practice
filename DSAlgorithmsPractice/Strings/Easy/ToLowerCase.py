"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
"""


def lowercase(str):
    out = ""
    for ch in str:
        n = ord(ch)
        if 64 < n < 91:
            out += chr(n+32)
        else:
            out += ch
    print(out)


lowercase("Vamsidhar Reddy")

