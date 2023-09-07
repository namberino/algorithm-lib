def exponant(num, n):
    if n == 0:
        return 1
    if n == 1:
        return num
    
    return num * exponant(num, n - 1)


print(exponant(5, 4))
