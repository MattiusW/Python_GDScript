def main():
    table = [4, 1, 5, 2, 3, 6, 7]
    print("Table:", table)
    sorted = bubbleSort(table)
    print("Sorted table:", sorted)    

def bubbleSort(tab):
    i = 0 
    while i < len(tab) - 1:
        j = 0
        #print(tab)
        while j < len(tab) - 1 - i:
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j] #Must swap in this way
            j += 1
        i += 1
    return tab

if __name__ == "__main__":
    main()