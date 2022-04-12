"""

"""


def first_repeat_element(input_list):
    if len(input_list) == 0:
        return None
    for i in range(1, len(input_list) - 1):
        if input_list[i] != input_list[i + 1] and input_list[i - 1] != input_list[i]:
            return i, input_list[i]


def dependent_course(course, course_dict):
    for i in course_dict[course]:
        for j in course_dict[i]:
            if j not in course_dict[course]:
                course_dict[course].append(j)
        return course_dict[course]


courses = {'a': ['b', 'c', 'd'], 'b': ['d', 'e', 'f'], 'c': ['f'], 'd': ['c', 'e', 'f'], 'e': ['f'], 'f': []}


if __name__ == '__main__':
    print(first_repeat_element([1, 1, 2, 2, 3, 4, 5, 5, 6]))
    print(dependent_course('e', courses))