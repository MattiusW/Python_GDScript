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
    new_guess_string = ''.join(guess_word)
    print("Guess word: ", new_guess_string)
    check_win = ''.join(word)

    while(chance >= 0):
        found = False
        repeat_word = False
        print("Life: ", chance)
        guess_letter_by_user = input("Pick letter: ").lower()

        for j in new_guess_string:
            if guess_letter_by_user in new_guess_string:
                repeat_word = True

        for i in range(0, len(word)):
            if guess_letter_by_user == word[i]:
                guess_word[i] = word[i]
                new_guess_string = ''.join(guess_word)
                print(f"Guest a letter: {guess_letter_by_user}")
                found = True

        if not found or repeat_word == True:
            chance -= 1

        elif new_guess_string == check_win:
            print("You Win!")
            print(new_guess_string)
            return

        draw_hangman(chance)
        print(new_guess_string)

def make_empty_table(word):
    word_lenght = len(word)
    empty_table = []

    for i in range(0, word_lenght):
        empty_table.append('_ ')

    return empty_table

def draw_hangman(life):
    if life == 2:
        print("""
                 _ _
                 o  |
                    |
                    |
              """)
    elif life == 1:
        print("""
                 _ _
                 o  |
                 |  |
                    |
              """)
    elif life == 0:
        print("""
                 _ _
                 o  |
                ;|; |
                    |
              """)
    elif life < 0:
        print("""
                 _ _
                 o  |
                ;|; |
                ; ; |

              YOU LOSE!
              """)
        return

def main():
    words = ["turtle", "ant", "panda"]
    guess_word = pick_word(words)
    empty_word_table = make_empty_table(guess_word)
    check_letter_in_word(guess_word, empty_word_table)

if __name__ == "__main__":
    main()
