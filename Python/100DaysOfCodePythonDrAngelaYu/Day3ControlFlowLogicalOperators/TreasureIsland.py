tab = [2,4,1,3,6]


for i in range(1, len(tab)):
    for j in range(len(tab)):
        if tab[j] > tab[i]:
            tab[j], tab[i] = tab[i], tab[j]
    print(tab)
print(tab)
       
        