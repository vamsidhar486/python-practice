"""
merge two sorted arrays with out duplicates
"""


def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1 + arr2)))


if __name__ == '__main__':
    print(merge_arrays([1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8]))
