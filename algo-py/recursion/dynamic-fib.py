lookup = [None] * 100

def dynamic_fib(n):
    global lookup

    if n == 0 or n == 1:
        return 1
    
    if lookup[n] is not None:
        return lookup[n]
    
    lookup[n] = dynamic_fib(n - 1) + dynamic_fib(n - 2)

    return lookup[n]

print(dynamic_fib(5))
