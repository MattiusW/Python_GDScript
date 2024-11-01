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

def uncrypy(code_text, shift_amount):
    encode_text = ""
    for i in code_text:
        ascii_value = ord(i)
        ascii_shift = ascii_value - shift_amount
        if (shift_amount != 0):
            if (ascii_shift < 65):
                gap = 65 - ascii_shift
                ascii_new_shift = 91 - gap
                encode_text += chr(ascii_new_shift)
            else:
                encode_text += chr(ascii_shift)
        else:
            encode_text = code_text

    return encode_text

def main():

    text = str(input("Give text to code: "))
    shift = int(input("How many shift?: "))
    lower_text = text.upper()
    cast_int = int(shift)
    ascii_value = chr(cast_int)

    code = encrypy(lower_text, cast_int)

    print("Code text: ", code)

    en_text = input("Give text to code: ")
    en_shift = input("How many shift?: ")
    en_lower_text = en_text.upper()
    en_cast_int = int(en_shift)
    en_ascii_value = chr(en_cast_int)

    uncode = uncrypy(en_lower_text, en_cast_int)

    print("Uncode text: ", uncode)

if __name__ == "__main__":
    main()


# ASCII ALPHABET 65 until 90
