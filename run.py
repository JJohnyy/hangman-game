# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import word_list
from game import hangman_stages




player_name = input("Hello players, please enter your name:\n").upper()
 
def get_word():
    word = random.choice(word_list)
    return word.upper()

def game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(f"Hello {player_name}, lets play hangman")
    print(hangman_stages(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess a letter or word:\n").upper()
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
                word_completion = "".join(word_list)
                if"_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"Well done {player_name} you guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print(hangman_stages(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print(f"Well done {player_name}, you win")
    else:
        print(f"Sorry {player_name},you lost, word was" + word + "try again")


def main():
    word = get_word()
    game(word)




if __name__ == "__main__":
    main()



