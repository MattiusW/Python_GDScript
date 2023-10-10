def main():
    tab = [2,5,1,3]
    insertSortv1(tab)
    
def insertSortv1(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    print(A)

if __name__ == "__main__":
    main()