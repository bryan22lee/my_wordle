import sys
import enchant
from getpass import getpass
from collections import Counter

d = enchant.Dict("en_US")

print("WORDLE, THE SEQUEL")
print("(\'quit\' to exit)\n")

word = getpass("Secret word: ")
print()

# Exit program
if word == 'quit':
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
  if word == 'quit':
    sys.exit()
  print()
  
print("Word accepted. Guess the word below in 6 tries!")
print("Hint: { ⏟ : wrong char, * : right char and wrong place }\n")

correct_placement = {}
for i, c in enumerate(word):
  if c in correct_placement:
    correct_placement[c].add(i)
  else:
    correct_placement[c] = set([i])
  

hint = []
count = 0
# Guess the word
while count < 6 and "".join(hint) != word:
  guess = input()
  # Exit program
  if guess == 'quit':
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
    if guess == 'quit':
      sys.exit()
    
  if guess == word:
    break
  
  letter_count = Counter()
  for i, c in enumerate(guess):
    letter_count[c] += 1
    if c==word[i]:
      hint.append(c)
    elif c in word:
      if letter_count[c] <= word.count(c) and i in correct_placement[c]:
        hint.append("*")
      else:
        hint.append("⏟")
    else:
      hint.append("⏟")
  print("".join(hint)+"\n")
  hint = []
  count += 1

if count == 6:
  print("Sorry, you failed 😔")
else:
  print("Congrats, you got the word!")