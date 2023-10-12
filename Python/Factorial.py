def main():    
    try:
        number = int(input("Input int number: "))
    except ValueError:
        print("Get integer number!")
        
    factorialNum = factorial(number)
    print(factorialNum)

def factorial(num): 
    fact = 1
    for i in range(1, num + 1): 
        fact *= i
    return fact 

if __name__ == "__main__":
    main()

