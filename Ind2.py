import random

def print_card(card):
    for i in card:
        print(i, end="\t")
        for num in card[i]:
            print(num, end="\t")
        print("\n")
    print("\n")
   
def check_win(card):

    win = False
    if card["B"][0] == "X" and card["I"][1] == "X" and card["N"][2] == "X" and card["G"][3] == "X" and card["O"][4] == "X":
        win = True
    elif card["O"][0] == "X" and card["G"][1] == "X" and card["N"][2] == "X" and card["I"][3] == "X" and card["B"][4] == "X":
        win = True
    for letter in card:
        if(len(set(card[letter]))==1):
            win = True
    for i in range(5):
        cnt = 0
        for letter in card:
            if card[letter][i] == "X":
                cnt += 1
        print(cnt)
        if cnt == 5:
            win = True
            break
    return win
  
  def main():
    card = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": [],
    }
    min = 1
    max = 15
    for letter in card:
        card[letter] = random.sample(range(min, max), 5)
        min += 15
        max += 15
