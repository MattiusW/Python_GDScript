def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        elif year % 100 == 1:
            return True

    return False

print(f"2400 Leap year?: {is_leap_year(2400)}")
print(f"1989 Leap year?: {is_leap_year(1989)}")
