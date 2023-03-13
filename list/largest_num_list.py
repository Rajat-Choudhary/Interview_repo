# Without using In-Built Function
def max_num_of_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
if __name__ == "__main__":
    list = [1, 2, -8, 0]
    result = max_num_of_list(list)
    print(result)

# By using In-Built Function
list = [1, 2, -8, 0]
sorted = sorted(list)
print(sorted)
result = max(sorted)
print(result)