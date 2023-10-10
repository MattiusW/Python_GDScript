def main():
    tab = [2,5,1,3]
    print(insertSortv1(tab))
    print(insertSortv2(tab))    

def insertSortv1(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

def insertSortv2(tab):
    i = 1
    while (i < len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
        i += 1
    return tab

if __name__ == "__main__":
    main()