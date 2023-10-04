def main():
    print("Welcome to Treasure Island. Your mission is to fing the treasure.")
    leftOrRight = input('Take a choice "left" or "right" ').lower()

    if (leftOrRight == "left"):
        swimOrWait = input('Now you "swim" or "wait "? ').lower()
        if (swimOrWait == "wait"):
            doorChoice = input('Wchich door? "red", "blue" or "yellow"? ').lower()
            if (doorChoice == "red"):
                print("Burned by Fire. Game over")
            elif (doorChoice == "blue"):
                print("Eaten by beast. Game over")
            elif (doorChoice == "yellow"):
                print("You win!")
            else:
                print("Game Over! ")
        else:
            print("Attacked by trout. Game over!")
    else:
        print("Fall into a hole. Game over!")

if __name__ == "__main__":
    main()