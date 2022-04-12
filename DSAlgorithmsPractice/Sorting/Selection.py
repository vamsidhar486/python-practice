"""
Selection Sort:
"""


# Using built-in python methods like index, min
def selection_asc(input_list):
    """
    Selection sort in Ascending order
    :param input_list: unsorted list
    :type: List
    :return: Ascending ordered list
    """
    for i in range(len(input_list) - 1):    # length-1 iteration also would yield the same desired result
        min_val = min(input_list[i:])       # for every unsorted list min value has to be found. hence slicing
        min_ind = input_list.index(min_val, i)  # For duplicates, i is required as it iterate only from ith index
        if input_list[i] != input_list[min_ind]:    # Including this will avoid unnecessary swapping for same values
            input_list[i], input_list[min_ind] = input_list[min_ind], input_list[i]
    print(input_list)


# using built-in methods like index and max
def selection_desc(input_list):
    """
    Selection sort in Descending order
    :param input_list: unsorted list
    :type: List
    :return: Descending Ordered List
    """
    for i in range(len(input_list) - 1):
        max_val = max(input_list[i:])
        max_ind = input_list.index(max_val, i)
        input_list[i], input_list[max_ind] = input_list[max_ind], input_list[i]
    print(input_list)


def selection_sort_asc(input_list):
    for i in range(len(input_list) - 1):
        min_val = input_list[i]
        for j in range(i+1, len(input_list)):
            if input_list[j] < min_val:
                min_val = input_list[j]
        min_ind = input_list.index(min_val, i)
        if input_list[i] != input_list[min_ind]:
            input_list[i], input_list[min_ind] = input_list[min_ind], input_list[i]
    print(input_list)


def selection_sort(input_list):
    for i in range(len(input_list) - 1):
        min_ind = i
        for j in range(i+1, len(input_list)):
            if input_list[j] < input_list[min_ind]:
                min_ind = j
        if input_list[i] != input_list[min_ind]:
            input_list[i], input_list[min_ind] = input_list[min_ind], input_list[i]
    print(input_list)


if __name__ == "__main__":
    # input_list = [1, 1, 7, 6, 8, 0, 3, 3, 5, 8, 9, 9]
    num = int(input("Enter the size of the list:"))
    input_list = [int(input("Enter number:")) for x in range(num)]
    selection_desc(input_list)
    selection_asc(input_list)
    selection_sort_asc(input_list)
    selection_sort(input_list)
