def main():
    print("Find two number where total amount is 10")
    tab = [3,4,5,1,0,5]
    print(tab)
    findNumber = 10
    pairs = totalCount(tab, findNumber)
    print(pairs)
    
def totalCount(table, key):
    total = []
    for i in range(len(table)):
        for j in range(i + 1, len(table)):  #Increase loop to skip compare same element
            if table[i] + table[j] == key:
                total.append([table[i], table[j]])
    return total

if __name__ == "__main__":
    main()