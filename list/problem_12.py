"""Write a Python program to print a specified list after removing the 0th, 4th and 5th elements."""

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
'''Normal Way'''
# result_list = []
# element_remove_position = [0,4,5]
# for position,color in enumerate(sample_list):
#     if position not in element_remove_position:
#         result_list.append(color)
# print(result_list)
'''Using List comp'''
# color = [color_name for (color_position,color_name) in enumerate(sample_list) if color_position not in (0,4,5)]
# print(color)

