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

"""Solution 8"""
# sample_string = "php python Java"
# convert_into_list = sample_string.split(" ")
# result = max(convert_into_list,key=len)
# count = 0
# for i in result:
#     count +=1
# print(f'Longest Word is:-{result}')
# print(f'Number of Letter is:-{count}')

"""Solution 9"""
# sample_string = "python"
# n = int(input("Enter the index of removing char:"))
# if len(sample_string) >= n:
#     result = sample_string.replace(sample_string[n],'')
#     print(result)
# else:
#     print("Index Out of Range")

"""Solution 10"""
# sample_string = "abcd"
# first_char = sample_string[-1:]
# print(first_char)
# last_char = sample_string[:1]
# print(last_char)
# result = last_char + sample_string[1:-1] + first_char
# print(result)

"""Solution 11"""
# sample_string = "Rajatchoudhary"
# result = ''
# for i in range(len(sample_string)):
#     if i % 2 == 0:
#         result = result + sample_string[i]
# print(result)

"""Solution 12"""
# sample_string = "the quick brown fox jumps over the lazy dog."
# words = sample_string.split(" ")
# d = dict()
# for word in words:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
# print(d)


"""Solution 13"""
# sample_string = "the quick brown fox jumps over the lazy dog."
# sample_string2 = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
# print(sample_string.upper())
# print(sample_string2.lower())