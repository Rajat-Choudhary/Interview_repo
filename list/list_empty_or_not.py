def list_empty(list):
    if len(list) == 0:
        return "Your List is Empty"
    else:
        return list

print(list_empty([]))
print(list_empty([12,54,23,54]))