# Hangman

* Hangman gamme is a Python terminal game

* Users can try to find a correct word in 6 steps to win a game.

* Otherwise they will get hanged and lose.



## Here is a version of the game
![look at different screen sizes](assets/images/responsivness.png)


# How to play the game

* hangman is a classic game played from the youngest age especiall at elementary school, game improves vocabulary mastery

* In this version, playes enters their name

* The playes can see the game(displayed hangman and a line where he can guess the letter in a word which is uknown and randomly generated from the list of words)


# Features

## Existing Features
* words are randomly generated from the list of words

* player name is used thru entire game

![player_name](assets/images/player_name.png)

* counts number of left tries

![display_hangman](assets/images/hangman_display.png)
* player must enter letters from alphabet

![guess_the_word](assets/images/guess_the_word.png)

* player is informed of wrongly guessed letter

![wrong_guess](assets/images/wrong_letter.png)

* player is informed when he guessed the same letter again

![same_guess](assets/images/already_guessed.png)

* player is informed when the gamme is won

![game_won](assets/images/game_won.png)

* player is informed when the game is lost

![game_lost](assets/images/game_lost.png)



# Data model

There is a word_list of 50 words in a separate file words.py from which random words are generated.
Another separate file game.py holds hangman steps which is a list.png

## Testing

I manually tested the game by doing following
* I gave invalid inputs like numbers
* I tested the game in heroku app

## Bugs

* displaying a word "players" instead of "player" in a welcoming sentence
* displaying words without a space when the game was lost

## Remaining bugs

* none

# Deployment

project was deplpoyed thru heroku app
* heroku app is set to automatic pull from github
* click on Deployment button in a dashboard
* set the buildbbacks python amd node.js in that order
* click Deploy


# Credits
codeinstitute for lessons and help with Deployment
codecademy for extra lessons in functions and manupulating lists
my mentor simen for his knowledge and experience as always