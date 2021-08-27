word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list) #or:(word_list[random.randint(0, len(word_list)-1)])
print(chosen_word)

display = []

for letter in chosen_word:
  display.append('_')

print(display) 
guess = input('Guess a letter!').lower()

for index in range(len(chosen_word)):
  if chosen_word[index] == guess:
    display[index]=guess
     
 
print(display)
