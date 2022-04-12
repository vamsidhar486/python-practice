"""
create list of 10s with length 10
"""

print([[0,0,0]]*3)


def create_nested_list(x,num):
    nested_list = []
    for i in range(x):
        nested_list.append([])
        for j in range(x):
            nested_list[i].append(num)
    return nested_list


if __name__ == '__main__':
    print(create_nested_list(3,0))
