import sys
from getpass import getpass
import enchant

d = enchant.Dict("en_US")

print("WORDLE, THE SEQUEL")
print("(\'quit\' to exit)\n")

word = getpass("Secret word: ")
print()

# Exit program
if word == 'quit':
  sys.exit()

while len(word) != 5 or not d.check(word):
  # Exit program
  if word == 'quit':
    sys.exit()
  
  if len(word) != 5:
    print("Word should have 5 characters")
  try:
    if not d.check(word):
      print("Word should be a valid English word")
  except:
    pass # Handeled by the first if-statement
  word = getpass("Enter secret word here: ")
  print()
  
print("Word accepted. Guess the word below in 6 tries!")
print("Hint: { ⏟ : wrong char, * : right char and wrong place }\n")

hint = []
count = 0
# Guess the word
while count < 6 and "".join(hint) != word:
  # Exit program
  if word == 'quit':
    sys.exit()
  
  guess = input()
  for i, c in enumerate(guess):
    if c==word[i]:
      hint.append(c)
    elif c in word:
      hint.append("*")
    else:
      hint.append("⏟")
  print("".join(hint)+"\n")
  hint = []
  count += 1

print("Congrats, you got the word!")