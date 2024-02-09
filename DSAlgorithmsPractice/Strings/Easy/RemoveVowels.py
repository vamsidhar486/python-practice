"""
Given a string, remove the vowels from the string and print the string without vowels.

Examples:

Input : welcome to geeksforgeeks
Output : wlcm t gksfrgks

Input : what is your name ?
Output : wht s yr nm ?
"""


def remove_vowels(input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter = [letter for letter in input if letter.lower() not in vowels]
    output = ''.join(letter)
    print(output)


import re


def remove_vowels2(input):
    return re.sub("[aeiouAEIOU]", "", input)


remove_vowels("Vamsi is a good boy")
print(remove_vowels2("Vamsi is a good boy"))
