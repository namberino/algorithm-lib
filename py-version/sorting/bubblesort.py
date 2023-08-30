# time complexity: O(n^2) (worst case) and O(n) (best case)
def bubbleSort(array):
    if (len(array) > 1 and array != None):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if (array[j] > array[j + 1]):
                    array[j], array[j + 1] = array[j + 1], array[j];

    return array



array = [42, 26, 75, 37, 14, 68, 51, 9, 11];
bubbleSort(array);
print(array);
