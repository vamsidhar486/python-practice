"""

"""


def print_list(arr):
    count = 0
    for i in arr:
        if len(i) > 2:
            if i[0] == i[-1]:
                count += 1
    return count


if __name__ == '__main__':
    print(print_list(['aba','abc','1221', 'saas']))