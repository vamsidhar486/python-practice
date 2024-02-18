"""
Python Program for Array Rotation Using temp array
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
arr = [1,2,3,4,5,6,7] d = 2
Rotation of the above array by 2 will make array
output = [3,4,5,6,7,1,2]
"""

"""
Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
1) Store d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]
"""


# Time complexity :O(n)
# Space complexity: O(d)
def rotate_array(arr, d):
    n = len(arr)
    temp = []
    i = 0
    while i < d:
        temp.append(arr[i])
        i += 1
    i = 0
    while d < n:
        arr[i] = arr[d]
        i += 1
        d += 1
    arr[:] = arr[:i] + temp
    return arr


"""
Using List slicing
"""


# Time-complexity : O(n)
# Space Complexity : O(1)
def rotate_list(arr, d):
    n = len(arr)
    arr[:] = arr[d:n] + arr[0:d]
    return arr


print(rotate_array([1, 2, 3, 4, 5, 6], 2))
print(rotate_list([1, 2, 3, 4, 5, 6], 3))
