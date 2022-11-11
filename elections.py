f = open("Input.txt", "r")
strings = f.readlines()
dictionary = {}
word = ''
n = ''
number = ''
for string in strings:
    for char in string:
        if char.isalpha():
            n += char
        elif char.isdigit():
            number += char
        elif char == ' ':
            word += n + ' '
            n = ''
        elif char == '\n':
            dictionary[word] = int(number)
            word = ''
            number = ''
            break
dictionary[word] = int(number)
f.close()
"""print(dictionary)"""
sum = 0
for key in dictionary:
    sum += dictionary[key]
TFEP = int(round(sum/450))
"""print(TFEP)"""
sum = 0
dictionary_new1 = dictionary
for key in dictionary_new1:
    dictionary[key] = int(round(dictionary_new1[key]/TFEP))
    sum += dictionary[key]
print(dictionary)

"""dictionary_new2 = dictionary
for key in dictionary_new2:
    dictionary_new2[key] = (dictionary_new1[key]/TFEP) % 1
max_value = max(dictionary_new2.values())
final_dict = {k: v for k, v in dictionary_new2.items() if v == max_value}
print(final_dict)"""

if sum != 450:
    i = 450 - sum
    dictionary_new2 = dictionary
    for key in dictionary_new2:
        dictionary_new2[key] = (dictionary_new1[key]/TFEP) % 1
    while i != 0:
        max_value = max(dictionary_new2.values())
        final_dict = {k: v for k, v in dictionary_new2.items() if v == max_value} # находит все ключи словаря с макс. дробной частью
        if(len(final_dict) == 1):
            keys = final_dict.keys()
            dictionary[keys[1]] += 1
            i -= 1
        if(len(final_dict) > 1):
            keys = final_dict.keys()
            
