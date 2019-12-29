import random
import string
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

with open('hangman.txt', 'r') as file:
    data = file.read()
    word_list = data.lower().split()


MAX_GUESSES = 6
secret_word = list(random.choice(word_list))
not_secret_word = ['_' for _ in secret_word]

correct_guess_history = []
guess_history = []


while MAX_GUESSES >= 0:
    clear()
    if MAX_GUESSES == 0:
        print('You lost!')
        print(f"The word was: {''.join(secret_word)}")
        break

    print(' '.join(not_secret_word))
    print(f'Number of guesses left {MAX_GUESSES}')
    print('Guess history:', ' '.join(guess_history))
    guess = input('Your letter guess? ').lower()

    if guess not in string.ascii_letters:
        print('That is not a letter!')
    elif guess in guess_history:
        print('You already guessed that letter')
    elif guess in secret_word:
        print('You guessed right!')
        correct_guess_history.append(guess)
        not_secret_word = [letter if letter in correct_guess_history else '_' for letter in secret_word]
        if '_' not in not_secret_word:
            print('Congratulations! You won')
            print(f"The word was: {''.join(secret_word)}")
            break
    elif guess is '':
        print('You did not enter a letter!')
    else:
        print('Your guess was wrong!')
        MAX_GUESSES -= 1
    if guess not in guess_history and guess in string.ascii_letters:
        guess_history.append(guess)
    input('Press Enter to try again...')

