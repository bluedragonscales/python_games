#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
assembled_password = ""

for letter in range(1, nr_letters + 1):
  # new_letter = letters[random.randint(0, len(letters)-1)]
  new_letter = random.choice(letters)
  assembled_password += new_letter


for symbol in range(1, nr_symbols + 1):
  # new_symbol = str(symbols[random.randint(0, len(symbols)-1)])
  new_symbol = random.choice(symbols)
  assembled_password += new_symbol


for number in range(1, nr_numbers + 1):
  # new_number = str(numbers[random.randint(0, len(numbers)-1)])
  new_number = random.choice(numbers)
  assembled_password += new_number


print(f"Your new password: {assembled_password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Turn the password into a list of characters.
password_list = list(assembled_password)

# Use the shuffle function to shuffle the items in the list.
random.shuffle(password_list)

# Now join the list items back into a string for the shuffled password.
shuffled_password = ''.join(password_list)
print(f"The shuffled version: {shuffled_password}")