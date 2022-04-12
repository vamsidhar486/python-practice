"""
Generate The below series
0 1 1 2 3 5 8 13 21
"""


def generate_series(n):
    output = []
    for i in range(n):
        if i == 0 or i == 1:
            output.append(i)
        else:
            output.append(output[i-2]+output[i-1])
    for i in output:
        print(i, end=" ")


generate_series(10)
