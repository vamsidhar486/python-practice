"""

"""


def words_greater(str, n):
    str_arr = str.split(" ")
    output = []
    for i in str_arr:
        if len(i) > n:
            output.append(i)
    return output


if __name__=='__main__':
    print(words_greater("My Name is Vamsi", 3))