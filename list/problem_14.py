# num = [7,8, 120, 25, 44, 20, 27]
# num = [x for x in num if x%2!=0]
# print(num)

num = [7,8, 120, 25, 44, 20, 27]
result_list = []
for x in num:
    if x%2!=0:
        result_list.append(x)
print(result_list)