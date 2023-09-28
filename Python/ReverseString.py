def main():
    stringToReverse = "Example String to reverse"
    print(reverseString(stringToReverse))
    simplyMethod = "Simply method to reserve string"
    print(simplyMethod[::-1])

def reverseString(example):
    reverseString = ""
    
    for word in example[::-1]:
        reverseString += word
    
    return reverseString

if __name__ == "__main__":
    main()