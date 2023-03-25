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
# d = {}
# for x in range(1,16):
#     d[x] = x*x
# print(d)

"""w3Resource Solution 8"""
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d = d1.copy()
# d.update(d2)
# print(d)

"""w3Resource Solution 9"""
# d = {'Red': 1, 'Green': 2, 'Blue': 3}
# for key,value in d.items():
#     print(f'Color:{key} & Value is:{value}')

"""w3Resource Solution 10"""
# my_dict = {'data1':100,'data2':-54,'data3':247}
# sum = 0
# for value in my_dict.values():
#     sum = sum + value
# print(sum)

"""w3Resource Solution 11"""
# my_dict = {'data1':100,'data2':-54,'data3':247}
# mul = 1
# for value in my_dict.values():
#     mul = mul * value
# print(mul)

"""w3Resource Solution 12"""
# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'a' in myDict:
#     del myDict['a']
# print(myDict)

"""w3Resource Solution 13"""
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# color_dict = dict(zip(keys,values))
# print(color_dict)

print("This is for practice")