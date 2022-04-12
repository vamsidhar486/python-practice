"""

"""


def clone_list(arr):
    clone_arr = []
    for i in arr:
        clone_arr.append(i)
    return clone_arr


def clone_list1(arr):
    clone_arr = list(arr)
    return clone_arr


if __name__ == '__main__':
    print(clone_list([1,2,3,4,5]))
    print(clone_list1([1, 2, 3, 4, 5]))