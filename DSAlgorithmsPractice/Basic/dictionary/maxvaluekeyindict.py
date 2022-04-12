"""

"""


def find_max_value_key(input_dict):
    keys = list(input_dict.keys())
    values = list(input_dict.values())
    max_value_index = 0
    for i in range(len(values)):
        if values[i] > values[max_value_index]:
            max_value_index = i
    return keys[max_value_index]


if __name__ == '__main__':
    print(find_max_value_key({1:10, 2:20, 3:30}))