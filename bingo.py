def print_card(card):
    for i in card:
        print(i, end="  ")
        for num in card[i]:
            print(num, end="  ")
        print("\n")

def check_num(card):
    num_win = (14, 3, 7, 10, 1, 18, 37, 48, 75, 18, 35, 49, 74, 3, 6)
    for num in num_win:
        for letter in card:
            i = 0
            for number in card[letter]:
                if number == num:
                    card[letter][i] = 0
                i += 1
    return card

def check_win(card):
    win = False
    if card["B"][0] == 0 and card["I"][1] == 0 and card["N"][2] == 0 and card["G"][3] == 0 and card["O"][4] == 0:
        win = True
    elif card["O"][0] == 0 and card["G"][1] == 0 and card["N"][2] == 0 and card["I"][3] == 0 and card["B"][4] == 0:
        win = True
    for letter in card:
        if (len(set(card[letter])) == 1):
            win = True
    for i in range(5):
        count = 0
        for letter in card:
            if card[letter][i] == 0:
                count += 1
        if count == 5:
            win = True
            break
    return win


dict1 = {
    "B": [14, 7, 9, 13, 15],
    "I": [18, 17, 16, 26, 19],
    "N": [35, 43, 36, 41, 42],
    "G": [49, 51, 46, 54, 50],
    "O": [74, 61, 70, 64, 72],
}
dict2 = {
    "B": [14, 10, 1, 3, 6],
    "I": [20, 17, 16, 26, 19],
    "N": [31, 43, 36, 41, 42],
    "G": [56, 51, 46, 54, 50],
    "O": [73, 61, 70, 64, 72],
}
dict3 = {
    "B": [14, 11, 4, 2, 5],
    "I": [21, 18, 18, 19, 20],
    "N": [31, 43, 37, 41, 42],
    "G": [60, 51, 55, 48, 50],
    "O": [73, 65, 72, 69, 75],
}
dict4 = {
    "B": [2, 1, 3, 11, 12],
    "I": [16, 20, 30, 29, 27],
    "N": [31, 45, 42, 41, 43],
    "G": [48, 46, 50, 60, 56],
    "O": [73, 65, 72, 69, 75],
}

print("Словарь 1:\n")
print_card(dict1)
dict_new = check_num(dict1)
print("\nСловарь 1(обр):\n")
print_card(dict_new)
if (check_win(dict_new)==True):
    print("Ответ: Победа")
else:
    print("Ответ: Поражение")

print("Словарь 2:\n")
print_card(dict2)
dict_new = check_num(dict2)
print("\nСловарь 2(обр):\n")
print_card(dict_new)
if (check_win(dict_new)==True):
    print("Ответ: Победа")
else:
    print("Ответ: Поражение")

print("Словарь 3:\n")
print_card(dict3)
dict_new = check_num(dict3)
print("\nСловарь 3(обр):\n")
print_card(dict_new)
if (check_win(dict_new)==True):
    print("Ответ: Победа")
else:
    print("Ответ: Поражение")

print("Словарь 4:\n")
print_card(dict4)
dict_new = check_num(dict4)
print("\nСловарь 4(обр):\n")
print_card(dict_new)
if (check_win(dict_new)==True):
    print("Ответ: Победа")
else:
    print("Ответ: Поражение")

