# 2D array blooming pattern
def bloom(n):
    arr = [[0 for column in range(n)] for row in range(n)];
    mid = int(n / 2);
    
    # get distance from mid point (the middle value of the middle array)
    for i in range(n):
        for j in range(n):
            distance = max(abs(i - mid), abs(j - mid));
            arr[i][j] = distance + 1;
    
    return arr;

n = int(input("enter length: "));

for row in bloom(n):
    print(row);
