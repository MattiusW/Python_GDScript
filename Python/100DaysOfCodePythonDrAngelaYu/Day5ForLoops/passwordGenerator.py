import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']
rand_letters = ""
rand_symbols = ""
rand_numbers = ""
easy_solution_password = ""
hard_solution_password = ""

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How symbols would you like in your password?\n"))
nr_numbers = int(input("How numbers would you like in your password?\n"))

how_many_input = nr_letters + nr_symbols + nr_numbers

draw_list = [letters, numbers, symbols]
rand_draw_list = random.randint(0, len(draw_list) - 1)

for i in range(0, nr_letters):
    rand_letters += letters[random.randint(0, len(letters) - 1)]
easy_solution_password += rand_letters

for j in range(0, nr_symbols):
    rand_symbols += symbols[random.randint(0, len(symbols) - 1)]
easy_solution_password += rand_symbols

for k in range(0, nr_numbers):
    rand_numbers += numbers[random.randint(0, len(numbers) - 1)]
easy_solution_password += rand_numbers

print(rand_letters)
print(rand_symbols)
print(rand_numbers)
print(how_many_input)
print("Easy solution password is: ", easy_solution_password)
print("Hard solution password is: ", hard_solution_password)



