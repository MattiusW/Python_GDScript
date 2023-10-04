# Which number do you want to check?
number = int(input())

# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

'''Task 2 '''
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height**2)
if bmi < 18.5:
  print(f"Your BMI {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

##############################################
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combine_name = name1 + name2
lover_name = combine_name.lower()

t = lover_name.count("t")
r = lover_name.count("r")
u = lover_name.count("u")
e = lover_name.count("e")
first_digit = t + r + u + e

l = lover_name.count("l")
o = lover_name.count("o")
v = lover_name.count("v")
e = lover_name.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
