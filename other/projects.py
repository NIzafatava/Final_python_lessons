# 1. Hangman Game in Python

import random
from collections import Counter

someWords = 'apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry'
someWords_splited = someWords.split(' ')
main_word = random.choice(someWords_splited)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in main_word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

letterGuessed = ''
chances = len(main_word) + 2
correct = 0
flag = 0

try:
    while (chances != 0) and flag == 0:  # flag is updated when the word is correctly guessed
        print()
        chances -= 1

        try:
            guess = str(input('Enter a letter to guess: '))
        except:
            print('Enter only a letter!')
            continue

        if not guess.isalpha():
            print('print only a letter')
            continue
        elif len(guess) != 1:
            print('print only a single letter')
            continue
        elif guess in letterGuessed:
            print('you ve already guessed this letter')
            continue


        if guess in main_word:
            k = main_word.count(guess)
            for _ in range(k):
                letterGuessed += guess

        for char in main_word:
            if char in letterGuessed and (Counter(letterGuessed) != Counter(main_word)):
                print(char, end=' ')
                correct += 1
            elif (Counter(letterGuessed) == Counter(main_word)):
                print(f'you won. the word is {main_word}')
                flaf = 1
                break
                break

    if chances == 0 and (Counter(letterGuessed) != Counter(main_word)):
                print('You lost! Try again..')
                print(f'the word is {main_word} ')

except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        print(f'the word is {main_word} ')
        exit()


