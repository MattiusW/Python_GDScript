for number in range(1,11,3):
    print("3 steps: ", number)

# Gauss solution

gaussSum = 0

for number in range(1, 101):
    gaussSum += number
    print(gaussSum)

print("Gauss solution: ", gaussSum)
