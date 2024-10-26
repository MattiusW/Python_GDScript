import random

def pick_word(words):
    draw_word = random.randint(0, len(words) - 1)
    word = words[draw_word]
    return word

def check_letter_in_word(word):
    chance = 3
    word_lenght = len(word) - 1

    while(chance > 0):
        guess_letter_by_user = input("Pick letter: ")
        if guess_letter_by_user in word:
             print("You guest")
        else:
            chance -= 1
            print(chance)

def main():
    words = ["turtle", "ant", "panda"]
    guess_word = pick_word(words)
    print(guess_word)
    check_letter_in_word(guess_word)

if __name__ == "__main__":
    main()
