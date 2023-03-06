def exp(x,n):
    if n == 0:
        return(1)

    else:
        return(exp(x, n-1) * x)



x = input("Entrez un nombre entier : ")
n = input("Entrez la puissance à laqulle élever l'entier : ")
print(exp(int(x), int(n)))