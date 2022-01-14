# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import word_list
from game import hangman_stages




player_name = input("Hello players, please enter your name: ")
 

def get_word():
    word = random.choice(word_list)
    return word.upper()

def game(word):
    word_completion = "_" * len(word)
    guessed = false
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(f"Hello {player_name}, lets play hangman")
    print(hangman_stages(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"Hey, {player_name} you already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"good job {player_name}", guess, "is in the word")
                guessed_letters.append(guess)
                word_list = list(word_completion)
                symbols = [i for i, letter in enumerate(word) if letter == guess]
                for index in symbols:
                    word_list[index] = guess
                word_completion = "".join(word_as_list)
                if"_" not in word_completion:
                    guessed = True



