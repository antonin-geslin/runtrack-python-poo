def bign(list, i, max):
    if i < len(liste):
        if i == 0 or liste[i] > max:
            max = liste[i]
        max = bign(liste, i+1, max)
    return(max)






liste = [2,4,1,0,10]
n = 0
print(bign(liste, 0, 0))