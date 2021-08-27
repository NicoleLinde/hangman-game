import random
from hangman_art import logo, stages
import hangman_words
from replit import clear

chosen_word = random.choice(hangman_words.word_list) #or:(word_list[random.randint(0, len(word_list)-1)])
#print(chosen_word) (for testing)

display = []
lives=6


for letter in chosen_word:
  display.append('_')

print(logo)
print(display)
already_guessed=[]

while '_' in display and lives>0:
  guess = input('Guess a letter!').lower()
  clear()
  if guess in already_guessed:
    print('You already had that one.')
  already_guessed.append(guess)
 
  for index in range(len(chosen_word)):
    if chosen_word[index] == guess:
      display[index]=guess
      print(f'You guessed:{guess}')

 
  if guess not in chosen_word and lives>0:
      lives-=1
      print(f'You guessed the letter: {guess}. That letter is not in the word- you loose a life.')
  
  print(display)
  print(stages[lives])
 
  if lives== 0:
    print('You lost') 

if '_' not in display:
  print('You win') 

