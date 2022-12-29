import csv

def time_separation(time):
    seps = time.split(".")
    for sep in seps:
        print(sep)
    seconds = 0
    for sep in seps:
        if "дн" in sep:
            seconds += int(sep.split()[0]) * 24 * 60 * 60
        elif "час" in sep:
            seconds += int(sep.split()[0]) * 60 * 60
        elif "мин" in sep:
            seconds += int(sep.split()[0]) * 60
        elif "сек" in sep:
            seconds += int(sep.split()[0])
    return seconds

def float_maker(almost_number):
    return float(almost_number.split(",")[0])

def check_good(guy_dict, marked_time, result_need):
    if(guy_dict['Состояние'] == "Завершено") and (time_separation(guy_dict['Затраченное время']) > marked_time):
        if 'Оценка/10,00' in guy_dict:
            return (float_maker(guy_dict['Оценка/10,00']) == float(result_need))
        else:
            return (float_maker(guy_dict['Оценка/100,00']) == float(result_need*10))

rows = []

time_compl = input("Введите заданное время, в формате XX дн.  YY час. ZZ мин. WW сек.\n")
marked_time = time_separation(time_compl.strip())
result_need = float(input("Введите заданное количество баллов (0 - 10)\n"))

good = set()

with open("15_1.csv", encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=",")
    count1 = 0
    key = 0
    for row in file_reader:
        if key == 0:
            print(f'Файл сожержит столбцы: {",".join(row)}')
            key += 1
        else:
            if check_good(row, marked_time, result_need):
                good.add(str(str(row['Фамилия'].capitalize()) +" "+str(row['Имя']).capitalize()))
                count1 += 1

print(good)


with open("15_2.csv", encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=",")
    count2 = 0
    key = 0
    for row in file_reader:
        if key == 0:
            print(f'Файл сожержит столбцы: {",".join(row)}')
            key += 1
        else:
            if check_good(row, marked_time, result_need):
                good.add(str(str(row['Фамилия']) +" "+str(row['Имя'])))
                count2 += 1

print(good)

print()
print("Отсортированные значения:", sorted(good))
count = count1 + count2
print("Количество:", count)

"""Найти количество людей, выполнивших тест более чем за заданное время и набравших
ровно заданное количество баллов. Вывести их список в алфавитном порядке."""
"""
00 дн. 00 час. 12 мин. 00 сек.
7
4 человека
"""
"""
01 дн. 00 час. 00 мин. 00 сек.
10
0 человек
"""
