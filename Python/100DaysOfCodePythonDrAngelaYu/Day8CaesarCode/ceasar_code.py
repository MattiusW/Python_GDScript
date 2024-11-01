def encrypy(orginal_text, shift_amount):
    print("Orginal text:", orginal_text)
    code_text = ""
    for i in orginal_text:
        ascii_value = ord(i)
        print("ASCCI VALUE: ", ascii_value)
        ascii_shift = ascii_value + shift_amount
        code_text += chr(ascii_shift)
        print("ASCCI After loop: ", ascii_value)
        print(ord(i))
        print(f"Dodawane wartosci {ascii_value}")

    return code_text

def main():
    text = input("Give text to code: ")
    shift = input("How many shift?: ")
    lower_text = text.upper()
    cast_int = int(shift)
    ascii_value = chr(cast_int)
    print(f"Input value: {ascii_value}")

    print(encrypy(lower_text, cast_int))

if __name__ == "__main__":
    main()


# ASCII ALPHABET 65 until 90
