"""
Given an integer array, move all elements that are 0 to the left while maintaining
the order of other elements in the array. The array has to be modified in-place.

Let’s look at the following integer array:

[1,10,20,0,59,63,0,88,0]

After moving all zeros to the left, the array should like this:
[0,0,0,1,10,20,59,63,88]

Remember to maintain the order of non-zero elements
"""


def solution(arr):
    if len(arr) < 1:
        return

    read_index = len(arr) - 1
    write_index = len(arr) - 1

    while read_index >= 0:
        if arr[read_index] != 0:
            arr[write_index] = arr[read_index]
            write_index -= 1
        read_index -= 1

    while write_index >= 0:
        arr[write_index] = 0
        write_index -= 1

    return arr


if __name__ == '__main__':
    print(solution([1, 10, 20, 0, 59, 63, 0, 88, 0]))
