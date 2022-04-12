"""
Python program which depict various python patters
"""

"""
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
"""


def print_simple_number_triangle(rows):
    for i in range(rows+1):
        for j in range(i):
            print(i, end=" ")
        print("")


print_simple_number_triangle(5)


"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""


def print_pyramid_pattern(rows):
    for i in range(rows+1):
        for j in range(i):
            print(j+1, end=" ")
        print("")


print_pyramid_pattern(5)