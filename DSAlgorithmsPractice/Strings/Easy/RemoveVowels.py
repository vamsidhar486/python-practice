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
    letter = [letter for letter in input if letter not in vowels]
    output = ''.join(letter)
    print(output)


remove_vowels("vamsi is a good boy")



