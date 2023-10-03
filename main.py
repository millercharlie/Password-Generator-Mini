# In this project, we are going to practice with using other files

# We also want to solidify our knowledge of functions and how they work in Python

# The Steps are:
#   1. Find the word list (go to github.com/millercharlie)
#   2. Download the words.txt file from the cleanwordlist repository
#   3. Import it into Repl.it
#   4. Write the password generator!

# The password generator should work like this:
# Ask the user how many words they want in the password and store the number in a variable
# Ask the user if they want to add numbers to the end of the password
# Optional: Ask the user if they want to add symbols to the end of the password

# Here is some starter code to get you going!

import random

# represents a list of symbols
symbols_list = ['%', '$', ...]

# opens the file
file = open('words.txt')
all_words = file.readlines()

# sets an initial password
password = ''

# At the end
print('Your password is:\n' + password)
