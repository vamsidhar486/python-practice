"""
Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array.

Examples:

Input: arr[] = {12, 35, 1, 10, 34, 1}
Output: The second largest element is 34.
Explanation: The largest element of the array is 35 and the second largest element is 34

Input: arr[] = {10, 5, 10}
Output: The second largest element is 5.
Explanation: The largest element of the array is 10 and the second largest element is 5

Ex: [10,10,10]
no element found
"""

import sys
import math

print(sys.maxsize)
print(-sys.maxsize)
print(math.inf)
print(-math.inf)
print(float('inf'))
print(float('-inf'))

def second_largest_element(arr):

    largest_element, second_largest_element = -math.inf, -math.inf

    for i in arr:
        if i > largest_element:
            largest_element = i

    for i in arr:
        if second_largest_element < i < largest_element:
            second_largest_element = i

    if second_largest_element != float('-inf'):
        print("second largest element is ", second_largest_element)
    else:
        print("no second largest element")


if __name__ == '__main__':
    second_largest_element([12,1,5,1])