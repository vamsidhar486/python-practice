"""
Exercises
"""


def extendList(val, input_list=['a']):
    input_list.append(val)
    return input_list


list1 = extendList(10)
print(list1)
list2 = extendList(123, [])
print(list2)
list3 = extendList('a')
print(list3)


list = ['a', 'b', 'c', 'd', 'e']
print(list[-3::-1])
print(list[-3:][::-1])