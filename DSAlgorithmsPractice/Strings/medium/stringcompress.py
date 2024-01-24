"""


"""
def stringCompress(str):
    output = []
    count = 0
    for i in range(len(str) - 1):
        if str[i] == str[i+1]:
            count = count+1
            output.append((count, str[i]))
        else:
            count = 0
            output.append((1, str[i]))
    for i in range(len(output)):
        print(output[i], end =" ")


stringCompress("1222311")