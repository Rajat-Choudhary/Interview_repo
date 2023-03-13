''' Write a Python function that takes two lists and returns True if they have at least one common member.'''

def command_ele(list1,list2):
    result = False
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1
                result = True
    return result,count

list1 = [1,2,3,4,5]
list2 = [5,6,7,4,9]
result,count = command_ele(list1,list2)
print(result)
print(count)

