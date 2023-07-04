# Euclidean algorithm

def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    
    return abs(x)

print(gcd(28, 8))

'''
If y >= x / 2 then x, y = y, x % y will always make y less than or equal to half of it's previous value
If y < x / 2 then x, y = y, x % y will always make x less than or equal to half of it's previous value

So at every step the algorithm will reduce one of the numbers to at least half less
Therefore O(log2a) + O(log2b) is the worst case
Assume n is the upper limit of a and b, we have O(log2n)
'''
