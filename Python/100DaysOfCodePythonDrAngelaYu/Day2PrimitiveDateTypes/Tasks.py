'''
Task1.
Write a program that adds the digits in a 2 digit number. e.g. if the 
input was 35, then the output should be 3 + 5 = 8
'''
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
numberOne = int(two_digit_number[0])
numberTwo = int(two_digit_number[-1])
print(numberOne + numberTwo)

'''
Task2.
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
'''
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightFloat = float(height)
weightFloat = float(weight)
bmi = weightFloat / (heightFloat**2)
print(int(bmi))
