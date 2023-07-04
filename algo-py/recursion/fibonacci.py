length = int(input("Enter length of sequence: "))
first, second = 0, 1
count = 0

print("Fibonacci sequence (no recursion): ")
while count < length:
    print(first, end=' ')
    tmp = second
    second += first
    first = tmp
    count += 1

print()

'''
Firstly, our assignemt of F[0] and F[1] cost O(1) each
Secondly, our loop will be O(n)
So our time complexity will be O(1) + O(1) + O(n) = O(n)
'''
