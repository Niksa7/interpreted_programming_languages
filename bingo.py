def print_card(card):
    for i in card:
        print(i, end="  ")
        for num in card[i]:
            print(num, end="  ")
        print("\n")

def check_num(card):
    num_win = (14, 3, 7, 10, 1, 17, 36, 54, 72, 18, 35, 49, 74, 9, 13, 15)
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
    """for letter in card:
        if (len(set(card[letter])) == 1):
            win = True"""
    for i in range(5):
        count = 0
        for letter in card:
            if card[letter][i] == 0:
                count += 1
        if count == 5:
            win = True
            break
    return win


dict = {
    "B": [14, 7, 9, 13, 15],
    "I": [18, 17, 16, 26, 19],
    "N": [35, 43, 36, 41, 42],
    "G": [49, 51, 46, 54, 50],
    "O": [74, 61, 70, 64, 72],
}
print("Словарь 1:\n")
print_card(dict)
dict_new = check_num(dict)
print("\nСловарь 1(обр):\n")
print_card(dict_new)
if (check_win(dict_new)==True):
    print("Ответ: Победа")
else:
    print("Ответ: Поражение")
