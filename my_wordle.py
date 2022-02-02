import sys
from getpass import getpass
import enchant

d = enchant.Dict("en_US")

print("WORDLE THE SEQUEL")
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
  
print("Word accepted\n")

print(word)