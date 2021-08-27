word_list = ["aardvark", "baboon", "camel"]

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list) #or:(word_list[random.randint(0, len(word_list)-1)])
print(chosen_word)

display = []
lives=6

for letter in chosen_word:
  display.append('_')

print(display) 

while '_' in display and lives>0:
  guess = input('Guess a letter!').lower()

  for index in range(len(chosen_word)):
    if chosen_word[index] == guess:
      display[index]=guess

 
  if guess not in chosen_word and lives>0:
      lives-=1
  
  
  print(stages[lives])
  print(display)

  if lives== 0:
    print('You lost') 

if '_' not in display:
  print('You win') 

