def calculate_love_score(name1, name2):
    check_true = ["t", "r", "u", "e"]
    check_love = ["l", "o", "v", "e"]
    count_true = 0
    count_love = 0
    name_lower1 = name1.lower()
    name_lower2 = name2.lower()
    # Check TRUE
    for letter_name in name_lower1:
        for check_letter in check_true:
            if letter_name == check_letter:
                count_true += 1
    for letter_name2 in name_lower2:
        for check_letter2 in check_true:
            if letter_name2 == check_letter2:
                count_true += 1
    # Check LOVE
    for letter_name in name_lower1:
        for check_letter in check_love:
            if letter_name == check_letter:
                count_love += 1
    for letter_name2 in name_lower2:
        for check_letter2 in check_love:
            if letter_name2 == check_letter2:
                count_love += 1

    print(f"Love Score = {count_true}{count_love}")

calculate_love_score("Kanye West", "Kim Kardashian")
