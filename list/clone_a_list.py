# First Way
# def clone_list(list):
#     clone = list[:]
#     print(f'Previous list:-{list}')
#     return f'List After Clone:-{clone}'
#
# print(clone_list([11,13,15,17,19,21,24]))

# Second Way

# def clone_list(list):
#     clone = list.copy()
#     print(f'Previous list:-{list}')
#     return f'List After Clone:-{clone}'
#
# print(clone_list([11,13,15,17,19,21,24]))

# Third Way

def clone_list(my_list):
    clone = list(my_list)
    print(f'Previous list:-{my_list}')
    return f'List After Clone:-{clone}'

print(clone_list([11,13,15,17,19,21,24]))