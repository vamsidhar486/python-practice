"""

"""


def remove_duplicates(arr):
    distinct_arr = []
    if len(arr) == 0:
        print("list is empty")
    else:
        for i in arr:
            if i not in distinct_arr:
                distinct_arr.append(i)
    return distinct_arr


if __name__ == '__main__':
    print(remove_duplicates([1,2,3,4,5,6,1,2,3]))
