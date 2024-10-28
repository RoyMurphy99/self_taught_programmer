"""
chapter 10 hangman game.
Roy P. Murphy 18/09/2024
"""

def hangman(word):
    wrong = 0
    stages =[
        "",
        "__________          ",
        "|         |         ",
        "|         0         ",
        "|        /|\\        ",
        "|         /\\        ",
        "|                   ",
        "|                   "
        ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in(rletters):
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! it was {}.".format(word))

import random
word_list =["The", "cat", "sat", "on", "the", "carpet", "dude"]
t_ind = random.randint(0,len(word_list) - 1)
target = word_list[t_ind]

hangman(target)


