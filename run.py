# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import word_list

player_name = input("Hello player, enter your name: ").upper()
print(player_name)


def get_word():
    """
    get word from from a list and convert it to uppercase
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    setup game
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(f"hello {player_name}, lets play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

