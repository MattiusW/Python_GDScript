def main():
    palindrome = "Potop"
    print(isPalindrome(palindrome))

def isPalindrome(palind):
    pal = palind.upper()
    if (pal == pal[::-1]):
       return True
    else:
        return False

if __name__ == "__main__":
    main()