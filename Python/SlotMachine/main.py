MAX_LINES = 3 # Constant value

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount mus be grater than 0.")
        else:
            print("Please enter a number.")

    return amount

def main():
    balance = deposit()

if __name__ == "__main__":
    main()
