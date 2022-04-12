def solution(str, column):
    header = str.split("\n")[0].split(",")
    values = str.split("\n")[1:]
    column_index = header.index(column)
    column_values = []
    for i in values:
        column_values.append(int(i.split(",")[column_index]))
    return max(column_values)


str = "id,name,age,act.,room,dep.\n1,jack,68,T,13,8\n17,betty,28,F,15,7"
print(solution(str, "age"))
str1 = "area,land\n3722,cn\n6612,ru\n3855,ca\n3797,usa"
print(solution(str1, "area"))
str2 = "city,temp2,temp\nparis,7,-3\ndubai,4,-4\nporto,-1,-2"
print(solution(str2, "temp"))
