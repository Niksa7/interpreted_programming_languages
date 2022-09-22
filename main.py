import re
string = "fhb5kbfыshfm"
"""reg_exp = re.compile('[^a-zA-Z]') - сохранение полученного объекта регулярного выражения для повторного использования
print(reg_exp.sub('', string))"""
result = re.sub('[^a-zA-Z]', '', string) #стр. шаблона регулярки, стр. замены, стр. поиска
sorted_result = sorted(result) # сортировка списка, корт., строки и т.д. На выходе получаем список
sorted_result_new = ''.join(sorted_result) #метод '?'.join() - преобразование списка в строку с использованием разделителей
print(sorted_result_new)
alphabet = ""
for i in sorted_result_new:
    if i not in alphabet:
        print(i + str(len(re.findall(i, sorted_result_new))))
        alphabet += i