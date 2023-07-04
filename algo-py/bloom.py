def bloom(n):
    arr = [[0 for x in range(n)] for y in range(n)]
    
    mid = int(n / 2)
    
    for i in range(n):
        for j in range(n):
            distance = max(abs(i - mid), abs(j - mid))
            arr[i][j] = distance + 1
    
    return arr

usr = int(input("enter length: "))

for row in bloom(usr):
    print(row)
