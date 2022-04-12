"""

"""


def flat_values_list(input_dict):
    output_list = []
    for i in input_dict.values():
        output_list.append(i)
    return output_list


def flat_keys_list(input_dict):
    return list(input_dict.keys())


if __name__ == '__main__':
    print(flat_values_list({1:10, 2:20, 3:30}))
    print(flat_keys_list({1: 10, 2: 20, 3: 30}))