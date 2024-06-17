def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def recursive_binary_search(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_binary_search(arr, mid + 1, high, target)
        else:
            return recursive_binary_search(arr, low, mid - 1, target)
    else:
        return - 1


print(recursive_binary_search([1, 5, 6, 7, 9, 10], 0, 5, 10))

print(binary_search([1, 5, 6, 7, 9, 10], 10))
