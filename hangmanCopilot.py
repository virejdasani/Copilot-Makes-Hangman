# make a hangman game with a copilot

# import modules
import random
import time

# define variables
wordList = ['subscribe']
word = random.choice(wordList)
guess = ''
guessList = []
guessCount = 0

# define functions
def print_hangman(guessCount):
    if guessCount == 0:
        print('_________')
        print('|       |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 1:
        print('_________')
        print('|       |')
        print('|       O')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 2:
        print('_________')
        print('|       |')
        print('|       O')
        print('|       |')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 3:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 4:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|')
        print('|')
        print('|')
        print('|')
    elif guessCount == 5:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|      /')
        print('|')
        print('|')
        print('|')
    elif guessCount == 6:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|      / \\')
        print('|')
        print('|')
        print('|')

# main program
print('Welcome to Hangman!')
print('The word has', len(word), 'letters')
print('You have 6 guesses')
print('Good luck!')

# loop until the word is guessed
while guess != word:
    # get a guess from the user
    guess = input('Guess a letter: ')
    guess = guess.lower()

    # check if the guess is valid
    if len(guess) != 1:
        print('You can only guess a single letter!')
    elif guess in guessList:
        print('You already guessed the letter', guess)
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('You can only guess letters!')
    else:
        # check if the guess is correct
        if guess in word:
            print('Good job!', guess, 'is in the word')
        else:
            print('Sorry', guess, 'is not in the word')
            guessList.append(guess)
            guessCount += 1

    # print the hangman
    print_hangman(guessCount)

    # check if the user has guessed too many times
    if guessCount == 6:
        print('Sorry, you ran out of guesses. The word was', word)
        break

    # check if the user has guessed the word
    if guess == word:
        print('Congratulations, you guessed the word!')
        print('You guessed the word in', guessCount, 'guesses')
        print('The word was', word)

# check if the user wants to play again
playAgain = input('Do you want to play again? (y/n) ')
if playAgain == 'y':
    guess = ''
    guessList = []
    guessCount = 0
    word = random.choice(wordList)
    print('Welcome to Hangman!')
    print('The word has', len(word), 'letters')
    print('You have 6 guesses')
    print('Good luck!')

# check if the user wants to quit
elif playAgain == 'n':
    print('Thanks for playing!')

# check if the user has entered an invalid response
else:
    print('Invalid response!')