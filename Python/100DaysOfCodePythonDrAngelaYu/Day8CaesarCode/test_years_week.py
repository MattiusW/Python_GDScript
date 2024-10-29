def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

def main():
    life_in_weeks(56)

if __name__ == "__main__":
    main()
