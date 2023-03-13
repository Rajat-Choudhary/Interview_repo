def multiply(list):
    sum = 1
    for i in list:
        sum *= i
    return sum

if __name__ == "__main__":
    list = [1,2,-8]
    result = multiply(list)
    print(result)