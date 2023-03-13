input_string = "hello how is everyone"
print(input_string)
"""
Question 1
Print length of each word as a space separated string
output = "5 3 2 8"

print(output)
5 3 2 8
"""
new = input_string.split()
empt_list = []
for i in new:
    length_of_word = len(i)
    empt_list.append(str(length_of_word))
result = " ".join(empt_list)
print(result)

"""
Question 2
Reverse each word of the sentence

Output: -olleh woh si enoyreve
"""
new = input_string.split(" ")
empt_list = []
temp = ''
for i in new:
    value = i[::-1]
    empt_list.append(value)
result = temp.join(' ').join(empt_list)
print(result)

"""
Question 3
Print the longest word
everyone
"""
new = input_string.split(" ")
longest_word = max(new,key=len)
print(longest_word)



"""
Question 4
Create a dict, key would be first character of each word,
 and value would be list containing the words starting with the character

{
"h":["hello","how"],
"i":["is"],
"e":["everyone"]
}
"""
words =  input_string.split(" ")
dict = {}
for word in words:
    if ( word[0] not in dict.keys()):
        dict[word[0]] = []
        dict[word[0]].append(word)
    else:
        if (word not in dict[word[0]]):
            dict[word[0]].append(word)
print(dict)

