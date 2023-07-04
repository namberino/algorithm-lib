import random

arr = [];

for i in range(10):
    randomInt = random.randint(1, 1000);
    arr.append(randomInt);
 
def bogoSort(arr):
    while (isSorted(arr) == False):
        shuffle(arr);
    return arr;
 
def isSorted(arr):
    for i in range(0, len(arr) - 1):
        if (arr[i] > arr[i + 1]):
            return False;
    return True;
 
def shuffle(arr):
    for i in range(0, len(arr)):
        r = random.randint(0, len(arr) - 1);
        arr[i], arr[r] = arr[r], arr[i];

print("The array:", arr);
print("The sorted array:", bogoSort(arr));

