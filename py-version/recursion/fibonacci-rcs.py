def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

length = int(input("Enter length: "))

if length < 0:
    print("Invalid")
else:
    print("Fibonacci sequence (with recursion): ")
    for i in range(length):
        print(fibonacci(i), end=' ')
    
print()

'''
T(n <= 1) = O(1)
T(n) = T(n - 1) + T(n - 2) + O(1)       // O(1) is the time to add them together

Assuming T(n - 2) ~ T(n - 1) 
T(n) = 2T(n - 1) + 1
So T(n - 1) = 2T(n - 2) + 1
T(n) = 2(2T(n - 2) + 1) + 1 = 4T(n -2) + 3
So T(n - 2) = 2T(n - 3) + 1
T(n) = 8T(n - 3) + 7
So T(n - 3) = 2T(n - 4) + 1
T(n) = 16T(n - 4) + 15

We can see a pattern here: T(n) = 2^kT(n - k) + ((2^k) - 1)
And T(0) = n - k = 0 so k = n
So T(n) = 2^nT(n - n) + ((2^k) - 1) = 2^n + 2^n - 1 = O(2^n)
'''
