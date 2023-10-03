import random

# represents a list of symbols
symbols_list = ['%', '$', '@', '#', '£', '?', '^', '*', ':', ';', '+', '=']

# opens the file
file = open('words.txt')
all_words = file.readlines()
# print(all_words)

# sets an initial password
password = ''

def add_numbers(num):
  global password
  for integer in range(0, num):
    rand = random.randint(0, 9)
    password += str(rand)


def add_symbols(num):
  global password
  global symbols_list
  for integer in range(0, num):
    rand = random.randint(0, len(symbols_list))
    password += symbols_list[rand]

# word_count represents the number of words that are
# to be in the password
word_count = input('How many words would you like your password to have? ')
num_count = input(
  'How many numbers would you like to add to the end of the password? ')
symbol_count = input(
  'How many symbols would you like to add to the end of the password? ')

for x in range(0, int(word_count)):
  rand = random.randint(1, 111)
  password += all_words[rand].rstrip()

if int(num_count) > 0:
    add_numbers(int(num_count))

if int(symbol_count) > 0:
  add_symbols(int(symbol_count))

print('Your password is:\n' + password)
