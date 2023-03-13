def addition(list):
    sum = 0
    for i in list:
        sum += i
    return sum

if __name__ == "__main__":
    list = [1,2,-8]
    result = addition(list)
    print(result)

