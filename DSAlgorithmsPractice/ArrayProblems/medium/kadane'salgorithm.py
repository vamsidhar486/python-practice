"""
Python program to find the maximum sum contiguous array
"""


def sum_contiguous_array(arr):
    max_so_far = arr[0]
    max_ending_here = 0

    for i in range(0, len(arr)):
        max_ending_here = max_ending_here + arr[i]

        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


if __name__ == '__main__':
    print(sum_contiguous_array([1, -3, 4, 7, -3, 6, 7, 9, -2]))
