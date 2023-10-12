'''You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails'''
import random

money = random.randint(0,1)

if money == 0:
    print("Tails")
else:
    print("Heads")

'''You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.'''

names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
rand = random.randint(0, len(names) - 1)
whoPay = names[rand]
print(f"{whoPay} is going to buy the meal today!")
