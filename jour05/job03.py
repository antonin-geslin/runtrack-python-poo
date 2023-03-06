def len_rec(str):
    if str == '':
        return 0
    return(1 + len_rec(str[:-1]))



str = 'Hello'
print(len_rec(str))
