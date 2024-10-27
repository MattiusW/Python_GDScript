import random

def pick_word(words):
    draw_word = random.randint(0, len(words) - 1)
    word = words[draw_word]
    guess = []

    for letter in word:
        guess.append(letter)
    return guess

def check_letter_in_word(word, guess_word):
    chance = 3
    word_lenght = len(word) - 1
    found = False


    while(chance >= 0):
        print("Life: ", chance)
        guess_letter_by_user = input("Pick letter: ").lower()
        for i in range(0, len(word)):
            if guess_letter_by_user == word[i]:
                guess_word[i] = word[i]
                print(f"Guest a letter: {guess_letter_by_user}")
                found = True

        if not found:
            chance -= 1

        print(guess_word)


def make_empty_table(word):
    word_lenght = len(word)
    empty_table = []

    for i in range(0, word_lenght):
        empty_table.append('_')

    return empty_table

def main():
    words = ["turtle", "ant", "panda"]
    guess_word = pick_word(words)
    print(guess_word)
    empty_word_table = make_empty_table(guess_word)
    print(empty_word_table)
    check_letter_in_word(guess_word, empty_word_table)

if __name__ == "__main__":
    main()
