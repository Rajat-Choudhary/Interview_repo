# Without using In-Built Function
def min_num_of_list(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
if __name__ == "__main__":
    list = [1, 2, -8, 0]
    result = min_num_of_list(list)
    print(result)

# By using In-Built Function
list = [1, 2, -8, 0]
sort = sorted(list)
result = min(sort)
print(result)