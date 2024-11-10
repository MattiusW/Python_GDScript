def unique_value(table):
    j = 0
    unique = 0
    is_unique = False
    end_table = table[-1]
    unique_numbers = []
    is_end = False

    while(is_end == False):
        number = table[j]
        count = 0

        for i in table:
            if i != number:
                unique = number
            elif i == number:
                count += 1
        if count == 1:
            unique_numbers.append(unique)
        if number == end_table:
            count += 1
            is_end = True
        j += 1

    return unique_numbers

def main():
    table = [1,2,2,3,4,3,3,5,5,7,8,8,9]
    print(table)
    unique_numbers = unique_value(table)
    print(unique_numbers)

if __name__ == "__main__":
    main()
