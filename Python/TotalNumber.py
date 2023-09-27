def main():
    print("Find two number where total amount is 9")
    tab = [3,4,5,1,0,5]
    print(tab)
    findNumber = 9
    amount = totalCount(tab, findNumber)
    print(amount)
    
def totalCount(table, key):
    total = []
    for i in table:
        for j in table:
            if i + j == key:
                total.append(i)
                total.append(j)
                return total

if __name__ == "__main__":
    main()