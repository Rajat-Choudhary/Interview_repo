"""Solution 1"""
# string = "Rajat"
# # print(len(string))
# count = 0
# for char in string:
#     count += 1
# print(count)

"""Solution 2"""

# sample_string = "rajata"
# dict = {}
# for n in sample_string:
#     if n in dict.keys():
#         dict[n] +=1
#     else:
#         dict[n] = 1
# print(dict)

"""Solution 3"""

# sample_string = "rajat"
# first_two_char = sample_string[0:2]
# last_two_char = sample_string[2:]
# if len(sample_string) < 2:
#     print('')
# else:
#     result = first_two_char + last_two_char
#     print(result)

'''Solution 4'''
# sample_string = 'restartrtatrgrt'
# first_char = sample_string[0]
# sample_string = sample_string.replace(first_char,'$')
# sample_string = first_char + sample_string[1:]
# print(sample_string)

'''Solution 5'''
# a = "abc"
# b = 'xyz'
# new_a = b[:2] + a[2:]
# new_b = a[:2] + b[2:]
# result = new_a + ' ' + new_b
# print(result)

'''Solution 6'''
# def fun(string):
#     if len(string) >= 3:
#         if string[3:] != 'ing':
#             string = string + 'ing'
#             return string
#         else:
#             string = string + 'ly'
#             return string
# print(fun("abc"))
# print(fun("string"))

