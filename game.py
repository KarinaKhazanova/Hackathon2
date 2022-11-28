import random

from data import DRAW
from functools import reduce

WORDS = ["elephant", "giraffe", "tiger", "wolf", "kangaroo", "sheep", "zebra", "hippopotamus", "hyena", "deer", "monkey", "racoon"]



def get_word(words=WORDS):
    return random.choice(words)


def get_symbol(word, answer):
    symbol = input("Enter a letter : ")
    if symbol not in word:
        return None
    return symbol


def game():
    word = list(get_word())
    answer = list("_" * len(word))
    answer[0] = word[0]
    answer[-1] = word[-1]
    draw_position = 0
    tries = len(DRAW)
    
    

    while True:
        print(DRAW[draw_position])
        if draw_position == tries - 1:
            w = "".join(word)
            print(f"LOSE. The answer was {w}")
            return
        print(f"The word is {answer}")
        symbol = get_symbol(word, answer)
        if not symbol:
            draw_position += 1
            continue

        answer[word.index(symbol)] = symbol
        word[word.index(symbol)] = "_"

        if answer.count("_") == 0:
            a = "".join(answer)
            print(f"The word is : {answer}")
            print(f"WIN. The answer is {a}")
            return


def start_game():
    while True:
        answer = input("Guess the animal. Do you want to start the game? Y or N\n")
        if answer == "Y":
            game()
        else:
            break
    return


def main():
    start_game()


if __name__ == "__main__":
    main()
