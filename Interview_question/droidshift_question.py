"""Question-1. Take a list as an input and reverse it"""
# total_element = int(input("How many element you want in list:"))
# input_list = []
# for i in range(total_element):
#     ele = int(input("Enter a Element:"))
#     input_list.append(ele)
# print(f'Your List is {input_list}')
# '''Way to Reverse a List'''
# # First Way
# output_result = input_list[::-1]
# print(output_result)
# # Second Way
# input_list.reverse()
# print(input_list)

''' Question-2. How to take list as an input'''
# n = int(input("Enter number of elements:"))
# a = list(map(int,input("Enter Element").strip().split( )))[:n]
# print(a)

'''Question-3. How to flatten a list of list into single list
Example:-1  = [[1,2],[3,4]]
output:-1   = [1,2,3,4]
Example:-2  = [[1,2],[3,4],5]
output:-2   = [1,2,3,4,5]
Example:-3  = [[1,2],[3,4],5,'Rajat']
output:-3   = [1,2,3,4,5,'Rajat']
'''
# First Way using for loop

# sample_list = [[1,2],[3,4]]
# list_flat = []
# for i in range(len(sample_list)):
#     for j in range(len(sample_list[i])):
#         list_flat.append(sample_list[i][j])
# print(list_flat)

# Second Way using itertool
'''This will only work in iterable but 5 is not iterable so it will not work'''

# from itertools import chain
# sample_list = [[1,2],[3,4],5]
# flattened_list = list(chain.from_iterable(sample_list))
# print(flattened_list)

# Third Way is a Universal Way
# sample_list = [[1,2],[3,4]]
# sample_list = [[1,2],[3,4],5]
# sample_list = ['Shiva',[1,2],[3,4],'Rajat',5,8,[31,32]]
# flattened_list = []
# for element in sample_list:
#     if isinstance(element,list):
#         for sub_element in element:
#             flattened_list.append(sub_element)
#     else:
#         flattened_list.append(element)
# print(flattened_list)

"""Question:-4 Sort a given list in the output format ?
		Sample_list = [-1,-1,150,140,-1,190,170]
		output      = [-1,-1,140,150,-1,170,190]"""
# Sample_list = [-1,-1,150,140,-1,190,170]
# non_negative = [x for x in Sample_list if x>0]
# non_negative.sort()
#
# sorted_list =[]
# non_neg_index = 0
# for num in Sample_list:
#     if num < 0:
#         sorted_list.append(num)
#     else:
#         sorted_list.append(non_negative[non_neg_index])
#         non_neg_index +=1
# print(sorted_list)

"""Question:-5 Count the maximum consecutive 0 in the given string
		'10101100100001111' ?
		Example: '10101100100001111'
		Output : Maximum number of consecutive 0 is:- 4"""

# string = '10101100100000011110'
# count = 0
# max_count= 0
# for char in string:
#     if char == '0':
#         count +=1
#     else:
#         max_count = max(max_count,count)
#         count = 0
# print('Maximum number of consecutive 0 is:',max_count)