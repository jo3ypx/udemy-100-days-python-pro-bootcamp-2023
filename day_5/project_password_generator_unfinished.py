# not finished

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
generated_password = ""
password_to_list = ""
final_generated_password = ""

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for letter in range(num_letters):
    index = random.randint(0, len(letters))
    generated_password += letters[index]

# for symbol in range(0, num_symbols):
#    index = random.randint(0, len(symbols))
#    generated_password += symbols[index]

# for number in range(0, num_numbers):
#    index = random.randint(0, len(numbers))
#    generated_password += numbers[index]

# print(f"Here's your password: {generated_password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#password_to_list = generated_password.split()
# random.shuffle(password_to_list)
#final_generated_password = "".join(password_to_list)

#print(f"Here's your password: {final_generated_password}")
