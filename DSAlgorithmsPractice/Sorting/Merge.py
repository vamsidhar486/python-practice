"""
Merge Sort Implementation
"""


def merge_sort(input_list):
    """

    :param input_list:
    :return:
    """
    if len(input_list) > 1:     # Base case
        mid = len(input_list)//2
        left_sublist = input_list[:mid]
        right_sublist = input_list[mid:]
        merge_sort(left_sublist)  # Recursive case
        merge_sort(right_sublist)   # Recursive case
        i = 0
        j = 0
        k = 0
        while i < len(left_sublist) and j < len(right_sublist):
            if left_sublist[i] < right_sublist[j]:
                input_list[k] = left_sublist[i]
                i = i + 1
                k = k + 1
            else:
                input_list[k] = right_sublist[j]
                j = j + 1
                k = k + 1
        while i < len(left_sublist):
            input_list[k] = left_sublist[i]
            i = i + 1
            k = k + 1
        while j < len(right_sublist):
            input_list[k] = right_sublist[j]
            j = j + 1
            k = k + 1


if __name__ == "__main__":
    num = int(input("Enter the length of the list:"))
    input_list = [int(input()) for x in range(num)]
    merge_sort(input_list)
    print(input_list)
