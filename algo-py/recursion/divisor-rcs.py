# Euclidean algorithm (recursive version)

def gcd(x: int, y: int) -> int:
    if (y == 0):
        return x
    return gcd(y, x % y)

print(gcd(28, 8))

'''
This is basically the same thing as the non recursive function
'''
