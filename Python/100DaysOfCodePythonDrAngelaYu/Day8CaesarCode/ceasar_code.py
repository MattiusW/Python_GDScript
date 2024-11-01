def encrypy(orginal_text, shift_amount):
    code_text = ""
    for i in orginal_text:
        ascii_value = ord(i)
        ascii_shift = ascii_value + shift_amount
        if (shift_amount != 0):
            if (ascii_shift > 90):
                gap = ascii_shift - 90
                ascii_new_shift = 64 + gap
                code_text += chr(ascii_new_shift)
            else:
                code_text += chr(ascii_shift)
        else:
            code_text = orginal_text

    return code_text

def main():
    text = input("Give text to code: ")
    shift = input("How many shift?: ")
    lower_text = text.upper()
    cast_int = int(shift)
    ascii_value = chr(cast_int)

    print(encrypy(lower_text, cast_int))

if __name__ == "__main__":
    main()


# ASCII ALPHABET 65 until 90
