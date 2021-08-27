#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

chosen_word = (word_list[random.randint(0, len(word_list)-1)])
print(chosen_word)

called_guess = input('Guess a letter!').lower()
print(called_guess)

def check ():
  if (called_guess in chosen_word):
    print('yes')
  else:
    print('NO')

check()