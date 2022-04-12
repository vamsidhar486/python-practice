"""

"""


def largest_element(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


def smallest_element(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min


if __name__ == '__main__':
    print(largest_element([1,2,3,4,5]))
    print(smallest_element([1,2,3,4,5]))
