"""w3Resource Solution 2"""

# sample_dict = {1:10,2:20}
# value = {3:30}
# sample_dict.update(value)
# print(sample_dict)

"""w3Resource Solution 3"""
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict4 = {}
# for d in (dic1,dic2,dic3):
#     dict4.update(d)
# print(dict4)

"""w3Resource Solution 4"""
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#     if x in d:
#         print("Given Key is Present")
#     else:
#         print("Given Key is not Present")
#
# is_key_present(5)
# is_key_present(9)

"""w3Resource Solution 5"""
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for key,value in d.items():
#     print(f'Keys = {key}, value = {value}')

"""w3Resource Solution 6"""
# n = int(input("input a Number: "))
# d = dict()
# for x in range(1,n+1):
#     d[x] = x*x
# print(d)

"""w3Resource Solution 7"""
d = {}
for x in range(1,16):
    d[x] = x*x
print(d)