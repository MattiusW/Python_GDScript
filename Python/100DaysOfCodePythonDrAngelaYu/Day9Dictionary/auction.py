import os

def auction():
    auctioners = {}
    yes_anserw = "y"
    again = "y"

    while(again == yes_anserw):
        try:
            user = str(input("Get name: "))
            bid = float(input("Get bid: $"))
        except:
            print("Get good value!")
            continue

        auctioners[user] = bid

        print("Add another user?: ")
        again = input("y or n?")

        if again.lower() == yes_anserw:
            os.system('cls||clear') # Clear terminal

    return auctioners

def main():
    os.system('cls||clear') # Clear terminal
    auctioners = auction()
    print(auctioners)

    high_user = max(auctioners, key=auctioners.get)
    high_value = auctioners[high_user]
    print(f"User with high bit: {high_user}, bit: {high_value}")

if __name__ == "__main__":
    main()
