# Password Generator Project
import random

num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "@", "*", "^"]

password_list = [] # Making a list to contain the password characters
for char in range(1, num_letters + 1):
    password_list += random.choice(letters)

for num in range(1, num_numbers + 1):
    password_list += random.choice(numbers)

for sym in range(1, num_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list) # Get random combination of password

password = "" # Making a string to convert from list to a string
for char in password_list:
    password += char

print(f"Your password is: {password}") # The final output
