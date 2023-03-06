def fibonnaci(n):
    if n == 0:
        return(0)
    elif n == 1:
        return(1)
    else:
        return(fibonnaci(n-2) + fibonnaci(n-1))


n = 0
while n <=10:
    print(fibonnaci(int(n)))
    n += 1
