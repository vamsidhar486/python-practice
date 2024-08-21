"""
Generate all sub arrays from a given array
"""


def sub_arrays(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            output = []
            for k in range(i, j + 1):
                output.append(arr[k])
            print(output)
            print("\n", end="")


sub_arrays([1, 2, 3, 4, 5])
