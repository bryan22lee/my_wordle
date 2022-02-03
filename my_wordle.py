import sys
import enchant
from getpass import getpass
from collections import Counter
from random_word import RandomWords
import time

# Replace alphabetical character with □ character
def replace_alpha(s):
  res = []
  for c in s:
    if c.isalpha():
      res.append("□")
    else:
      res.append(c)
  return "".join(res)

d = enchant.Dict("en_US")

print("WORDLE, THE SEQUEL")
print("(\'q\' to exit)\n")

# User can input the secret word
# word = getpass("Secret word: ")
# print()

# Get a random 5 letter word
r = RandomWords().get_random_word(minLength=5, maxLength=5)
# Make sure secret word is valid pyenchant library recognizes it
while not r or not r.isalpha() or not d.check(r.lower()):
  time.sleep(0.00005)
  r = RandomWords().get_random_word(minLength=5, maxLength=5)
word = r.lower()

# print(word)

# Exit program
if word == 'q':
  sys.exit()

while len(word) != 5 or not d.check(word):
  if len(word) != 5:
    print("Word should have 5 characters\n")
  else:
    try:
      if not d.check(word):
        print("Word should be a valid English word\n")
    except:
      pass # Handeled by the first if-statement
  word = getpass("Secret word: ")
  # Exit program
  if word == 'q':
    sys.exit()
  print()
  
print("Guess the word in 6 tries!")
print("Hint: { ⏟ : wrong char, * : right char and wrong place }\n")

correct_placements = {}
for i, c in enumerate(word):
  if c in correct_placements:
    correct_placements[c].add(i)
  else:
    correct_placements[c] = set([i])
  

hint = []
hint_history = []
count = 0
win_flag = False
# Guess the word
while count < 6 and "".join(hint) != word:
  guess = input()
  # Exit program
  if guess == 'q':
    sys.exit()
  
  while len(guess) != 5 or not d.check(guess):
    if len(guess) != 5:
      print("Guess should have 5 characters!\n")
    else:
      try:
        if not d.check(guess):
          print("Not a valid word!\n")
      except:
        pass
    guess = input()
    # Exit program
    if guess == 'q':
      sys.exit()
    
  if guess == word:
    print(guess+"\n")
    hint_history.append(word)
    win_flag = True
    count += 1
    break
  
  # First pass
  guess_counts = Counter()
  for c in guess:
    guess_counts[c] += 1
  
  letter_counts = Counter()
  # Second pass
  for i, c in enumerate(guess):
    letter_counts[c] += 1
    # Case where i is the correct index of the secret word
    if c==word[i]:
      hint.append(c)
    elif c in word:
      if guess_counts[c] <= word.count(c):
        hint.append("*")
      elif guess_counts[c] > word.count(c) and i not in correct_placements[c]:
        if letter_counts[c] > word.count(c):
          hint.append("*")
        else:
          hint.append("⏟")
      else:
        hint.append("⏟")
    else:
      hint.append("⏟")
  h = "".join(hint)
  hint_history.append(h)
  print(h+"\n")
  hint = []
  count += 1

if count >= 6:
  if win_flag:
    print("Congrats, you got the word!\n")
  else:
    print("Sorry, you failed 😔")
    print("The word was {}\n".format(word))
else:
  print("Congrats, you got the word!\n")
  
print("Post to Twitter!\n")
print("my_wordle, {}/6\n".format(count))

for i in hint_history:
  print(replace_alpha(i))
  
print()